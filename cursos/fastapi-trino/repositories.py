from typing import Any, Sequence

from sqlalchemy import text, Row
from sqlalchemy.orm import Session


class TrilhaRepository:
    @staticmethod
    def find_all(db: Session) -> Sequence[Row[Any]]:
        conn = db.connection()
        return conn.execute(text("SELECT tr.tri_id as id, tr.tri_sit_email as situacao, tr.tri_nm_email as email, tr.tri_sub_orgao as sub_orgao, tr.tri_nm_orgao as nm_orgao, tr.tri_orig as origem, tr.tri_dtca as dtca, tr.tri_dtde as dtde, tr.tri_hash as hash FROM o_gestao_pessoas.o_gp_tri_trilha tr")).fetchall()

