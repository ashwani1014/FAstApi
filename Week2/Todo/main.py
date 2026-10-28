import passpy
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,ConfigDict,Field




DATABAse_URL= "sqlite:///./test.db"

engine=create_engine(DATABAse_URL,connect_args={"check_same_thread": False})

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

class TodoModel(Base):
    pass

class TodoModel()










app=FastAPI("Todo app")

@app.get("/")
def tasks():
    if tasks == []:
        return "No tasks found"

    return tasks    