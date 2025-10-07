from domain.reserva import Reserva
from domain.viaje import Viaje
from domain.usuario import Usuario
from infrastructure.models import ReservaModel

def reserva_model_to_entity(reserva_model: ReservaModel) -> Reserva:
    
    usuario_entity = Usuario(
        id=reserva_model.usuario.id,
        nombre=reserva_model.usuario.nombre,
        apellido_1=reserva_model.usuario.apellido_1,
        apellido_2=reserva_model.usuario.apellido_2,
        email=reserva_model.usuario.email,
        contrasena=reserva_model.usuario.contrasena
    )
    
    viaje_entity = Viaje(
        id=reserva_model.viaje.id,
        origen=reserva_model.viaje.origen,
        destino=reserva_model.viaje.destino,
        fecha=reserva_model.viaje.fecha,
        asientos_totales=reserva_model.viaje.asientos_totales,
        asientos_disponibles=reserva_model.viaje.asientos_disponibles,
        precio=reserva_model.viaje.precio
    )
    
    return Reserva(
        id=reserva_model.id,
        usuario=usuario_entity,  
        viaje=viaje_entity,     
        fecha_reserva=reserva_model.fecha_reserva,
        estado=reserva_model.estado,
        precio_pagado=reserva_model.precio_pagado
    )

def entity_to_reserva_model(reserva: Reserva, reserva_model: ReservaModel) -> ReservaModel:
    reserva_model.estado = reserva.estado
    reserva_model.precio_pagado = reserva.precio_pagado
    return reserva_model
