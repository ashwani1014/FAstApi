
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBaes, sessionmaker


DATABAse_URL=" "

engine=create_engine(DATABAse_URL, connect_args={"check_same_thread":False},)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

class Base(DeclarativeBaes):
    pass

def get_db():
    db=SessionLocal()


    try:
        yield db

    finally:
         db.close()   

         
            