from infrastructure.db_config import SessionLocal
from infrastructure.models import UsuarioModel

class UsuarioRepositoryDB:
    def get_by_id(self, usuario_id):
        session = SessionLocal()
        try:
            return session.query(UsuarioModel).filter_by(id=usuario_id).first()
        finally:
            session.close()
