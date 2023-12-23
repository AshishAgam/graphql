from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String ,Integer,create_engine,BigInteger
from sqlalchemy.orm import sessionmaker


Base =declarative_base()

class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True,autoincrement=True)
    name=Column(String)
    contact_email=Column(String)
    mobile=Column(BigInteger)
