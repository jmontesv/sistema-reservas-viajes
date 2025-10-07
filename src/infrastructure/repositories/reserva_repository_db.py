from sqlalchemy.orm import joinedload
from domain.reserva import Reserva
from infrastructure.db_config import SessionLocal
from infrastructure.models import ReservaModel

class ReservaRepositoryDB:
    def add_reserva(self, reserva: Reserva):
        session = SessionLocal()
        try:
            reserva_model = ReservaModel(
                id=reserva.id,
                usuario_id=reserva.usuario.id,
                viaje_id=reserva.viaje.id,
                fecha_reserva=reserva.fecha_reserva,
                estado=reserva.estado,
                precio_pagado=reserva.precio_pagado
            )
            session.add(reserva_model)
            session.commit()
        finally:
            session.close()

    def get_by_id(self, id):
        session = SessionLocal()
        try:
            return (
                session.query(ReservaModel)
                .options(joinedload(ReservaModel.usuario), joinedload(ReservaModel.viaje))
                .filter_by(id=id)
                .first()
            )
        finally:
            session.close()

    def get_by_user(self, usuario_id):
        session = SessionLocal()
        try:
            reservas = (
                session.query(ReservaModel)
                .options(joinedload(ReservaModel.usuario), joinedload(ReservaModel.viaje))
                .filter(ReservaModel.usuario_id == usuario_id)
                .all()
            )
            return reservas
        finally:
            session.close()

    def cancel(self, reserva_model):
        session = SessionLocal()
        try:
            reserva_model.estado = "Cancelada"
            session.commit()
        finally:
            session.close()
    
    def update(self, reserva_model):
        session = SessionLocal()
        try:
            session.merge(reserva_model)
            session.commit()
        finally:
            session.close()
            
