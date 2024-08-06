from sqlalchemy import Column, Integer, String

from database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id: int = Column('id', Integer, primary_key=True, index=True)
    titulo: str = Column('titulo', String(100), nullable=False)
    descricao: str = Column('descricao', String(255), nullable=False)
    carga_horaria: int = Column('carga_horaria', Integer, nullable=False)
    qtd_exercicios: int = Column('qtd_exercicios', Integer, nullable=False)
