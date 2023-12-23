from sqlalchemy import create_engine, URL
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = URL.create(
    drivername="postgresql",
    username='postgres',
    password='ashish',
    host='localhost',
    database='user_db',
    port=5432
)

