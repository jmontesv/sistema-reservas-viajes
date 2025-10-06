from domain.reserva import Reserva
import uuid
from datetime import datetime

class ReservarViaje:
    def __init__(self, viaje_repository, reserva_repository, usuario_repository):
        self.viaje_repository = viaje_repository
        self.reserva_repository = reserva_repository
        self.usuario_repository = usuario_repository
    
    def execute(self, usuario_id, viaje_id):
        usuario = self.usuario_repository.get_by_id(usuario_id)
        if not usuario:
            raise Exception("Usuario no encontrado")
        viaje = self.viaje_repository.get_by_id(viaje_id)
        if not viaje:
            raise Exception("Viaje no encontrado")
        viaje.reservar_asiento()
        precio = viaje.calcular_precio()
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
        self.reserva_repository.add_reserva(reserva)
        self.viaje_repository.update(viaje)
        return reserva