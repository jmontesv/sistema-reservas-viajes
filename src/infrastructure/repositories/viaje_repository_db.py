from infrastructure.db_config import SessionLocal
from infrastructure.models import ViajeModel

class ViajeRepositoryDB:
    def get_by_id(self, viaje_id):
        session = SessionLocal()
        try:
            return session.query(ViajeModel).filter_by(id=viaje_id).first()
        finally:
            session.close()

    def update(self, viaje_model):
        session = SessionLocal()
        try:
            session.merge(viaje_model)
            session.commit()
        finally:
            session.close()
