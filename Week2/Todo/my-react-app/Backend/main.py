from fastapi.telemetry._runtime import lifespan
import passpy
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,ConfigDict,Field
from sqlalchemy import create_engine, String, Boolean, Integer, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker
from .database import get_db
from models import task

DATABAse_URL= "sqlite:///./test.db"

engine=create_engine(DATABAse_URL,connect_args={"check_same_thread": False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass


class TodoModel(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=150)
    completed: bool | None = None


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
 

@asynccontextmanager
async def lifespam(app:FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app=FastAPI(title="TODo ",lifespan=lifespan)



# React development server ko API access dena
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"], 
    )



    

@app.get("/")
def tasks():
    if tasks == []:
        return "No tasks found"

    return tasks    


@app.post("/api/v1/todos",response_model=list[TodoResponse])
def get_Todos(db: Session= Depends(get_db)):
    return db.scalars(select(TodoModel).order_by(TodoModel.id.desc())).all()


@app.post("api/v1/todos",response_model=TodoResponse,status_code=201)
def create_todo(data:TodoCreate,db:Session=Depends(get_db) ):
    todo=TodoModel(title=data.title.strip())


    if not todo.title:
        raise HTTPException(status_code=422,detail="Title cannot be empty")

    db.add(todo)
    db.commit()
    db.refresh(todo)


    return todo 


@app.patch("/api/vi/todos/{todo_id}",response_model=TodoResponse)
def update_todo(
    todo_id:int,
    data:TodoUpdate,
    db:Session=Depends(get_db),):

    todo=db.get(TodoModel,todo_id)

    if todo is None:
        raise HTTPException (status_code=404,detail="Todo not found")
    updates=data.model_dump(exclude_unset=True)

    if "title" in updates:
        if updates["title"] is None or not updates ["title"].strip():
            raise HTTPException (status_code=422,detail="Title cannot be empty")
        updates["title"]=updates["title"].strip()

    for field,value in updates.items():
        setattr(todo,field,value)
    
    db.commit()
    db.refresh(todo)

@app.delete("/api/v1/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.get(TodoModel, todo_id)

    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(todo)
    db.commit()
