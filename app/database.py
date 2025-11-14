from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# The general format for the 'connection string' is:
# SQLALCHEMY_DATABASE_URL = 'postgresql://<usename>:<password>@ip-address/<database_name>'

# But in our case, we have this setting
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:new_password@localhost/fastapi'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# The engine is responsible for establishing the connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Whenever we wanna talk to the SQL database, we have to make use of a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for all our models
Base = declarative_base()


# We will create a session/dependency to connect to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# # here we will connect to the database and give its details using raw SQL
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database='fastapi', user = 'postgres', 
#                             password = 'new_password', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print('Connection to database failed')
#         print('Error:', error)
#         time.sleep(10)



        
