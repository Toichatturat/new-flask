from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string , 
  connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobslist = []
    # jobs = []
    jobs = [dict(row._asdict()) for row in result]
  # for row in result.all():
    # Use copy() to create a new dictionary
    # job_dict = row.copy()
    # jobs.append(row._mapping)
    # jobs.append(dict(row))
    return jobs