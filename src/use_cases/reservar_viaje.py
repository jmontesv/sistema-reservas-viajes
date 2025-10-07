from datetime import datetime
import uuid

from domain.reserva import Reserva
from mappers.viaje_mapper import viaje_model_to_entity, entity_to_viaje_model
from mappers.usuario_mapper import usuario_model_to_entity
from mappers.reserva_mapper import entity_to_reserva_model
from infrastructure.models import ReservaModel

class ReservarViaje:

    def __init__(self, viaje_repository, reserva_repository, usuario_repository):
        self.viaje_repository = viaje_repository
        self.reserva_repository = reserva_repository
        self.usuario_repository = usuario_repository

    def execute(self, usuario_id, viaje_id):
        # 1️⃣ Obtener modelos desde la DB
        usuario_model = self.usuario_repository.get_by_id(usuario_id)
        if not usuario_model:
            raise Exception("Usuario no encontrado")

        viaje_model = self.viaje_repository.get_by_id(viaje_id)
        if not viaje_model:
            raise Exception("Viaje no encontrado")

        # Mapear a entidades de dominio
        usuario = usuario_model_to_entity(usuario_model)
        viaje = viaje_model_to_entity(viaje_model)

        # Lógica de negocio
        viaje.reservar_asiento()
        precio = viaje.precio

        # Crear reserva de dominio
        reserva_id = str(uuid.uuid4())
        fecha_reserva = datetime.now()
        reserva = Reserva(
            id=reserva_id,
            usuario=usuario,
            viaje=viaje,
            asiento=None,
            fecha_reserva=fecha_reserva,
            estado="Activa",
            precio_pagado=precio
        )

        # Persistir cambios
        self.viaje_repository.update(entity_to_viaje_model(viaje, viaje_model))
        reserva_model = ReservaModel(id=reserva.id, usuario=usuario_model, viaje=viaje_model,
                                     fecha_reserva=fecha_reserva, estado="Activa",
                                     precio_pagado=precio)
        self.reserva_repository.add_reserva(reserva_model)

        return reserva
