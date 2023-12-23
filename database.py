from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import url
from models import Base


engine = create_engine(url,echo=True) 
Session=sessionmaker(bind=engine)

def prepare_database():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session=Session()

    session.commit()
    session.close()