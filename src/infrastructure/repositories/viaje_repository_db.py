from infrastructure.db_config import SessionLocal
from sqlalchemy import func
from infrastructure.models import ViajeModel
from infrastructure.repositories.viaje_respository import ViajeRepository

class ViajeRepositoryDB(ViajeRepository):
    
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
    
    def search(self, fecha, origen=None, destino=None):
        session = SessionLocal()
        try:
            query = session.query(ViajeModel).filter(func.date(ViajeModel.fecha) == fecha.date())
            if origen:
                query = query.filter(ViajeModel.origen == origen)
            if destino:
                query = query.filter(ViajeModel.destino == destino)
            return query
        finally:
            session.close()
    
    def add():
        pass
