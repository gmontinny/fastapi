from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import Curso
from repositories import CursoRepository
from schemas import CursoRequest, CursoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
async def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.model_validate(curso)

@app.get("/api/cursos", response_model=list[CursoResponse])
async def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.model_validate(curso) for curso in cursos]

@app.get("/api/cursos/query")
async def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_query(db)
    for curso in cursos:
        print(curso[0])
    return {"count": len(cursos)}

@app.get("/api/cursos/type", response_model=list[CursoResponse])
async def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_query(db)
    return [CursoResponse.model_validate(curso) for curso in cursos]


@app.get("/api/cursos/return", response_model=dict)
async def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_query(db)
    return {"cursos": [CursoResponse.model_validate(curso) for curso in cursos]}

@app.get("/api/cursos/{id}", response_model=CursoResponse)
async def find_by_id(id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, id)
    if not curso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    return CursoResponse.model_validate(curso)

@app.delete("/api/cursos/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    CursoRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/cursos/{id}", response_model=CursoResponse)
async def update(id: int, request: CursoRequest, db: Session = Depends(get_db)):
    if not CursoRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )
    curso = CursoRepository.save(db, Curso(id=id, **request.dict()))
    return CursoResponse.model_validate(curso)

