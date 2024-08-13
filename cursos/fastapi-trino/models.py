from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from database import Base


class Trilha(Base):
    __tablename__ = "o_gp_tri_trilha"

    id: str = Column('tri_id', String(20))
    situacao: str = Column('tri_sit_email', String(5), nullable=False)
    email: str = Column('tri_nm_email', String(255), nullable=False)
    sub_orgao: int = Column('tri_sub_orgao', Integer)
    nm_orgao: str = Column('tri_nm_orgao', String(255))
    origem: str = Column('tri_orig', String(20))
    dtca: datetime = Column('tri_dtca', DateTime)
    dtde: datetime = Column('tri_dtde', DateTime, nullable=True)
    hash: str = Column('tri_hash', String(255))