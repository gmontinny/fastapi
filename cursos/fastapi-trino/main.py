from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db, Base, engine
from repositories import TrilhaRepository
from schemas import TrilhaResponse

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def root(db: Session = Depends(get_db)):
    trilha = TrilhaRepository.find_all(db)
    for row in trilha:
        print(row[0])
    return {"count": len(trilha)}

@app.get("/api/trilha/query", response_model=list[TrilhaResponse])
async def query_trilha(db: Session = Depends(get_db)):
    trilha = TrilhaRepository.find_all(db)
    return [TrilhaResponse.model_validate(row) for row in trilha]

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
