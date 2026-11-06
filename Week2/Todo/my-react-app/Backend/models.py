from sqlalchemy import String,Integer
from database import Base
from datetime import datetime

class Task(Base):
    __tablename__='tasks'

    id:Mapped[int]=mapped_column(
        Integer, primary_key=True,index=True
        
    )

    title:Mapped[str]=mapped_column(String(200),nullable=False)

    description:Mapped[str|None]= mapped_column(String(1000),nullable=True,)


    created_at:Mapped[datetime]=mapped_coumn(Datetime,default=datetimr.utcnow,nullable=False,)