from domain.viaje import Viaje
from infrastructure.models import ViajeModel

def viaje_model_to_entity(viaje_model: ViajeModel) -> Viaje:
    return Viaje(
        id=viaje_model.id,
        origen=viaje_model.origen,
        destino=viaje_model.destino,
        fecha=viaje_model.fecha,
        asientos_totales=viaje_model.asientos_totales,
        asientos_disponibles=viaje_model.asientos_disponibles,
        precio=viaje_model.precio
    )

def entity_to_viaje_model(viaje: Viaje, viaje_model: ViajeModel) -> ViajeModel:
    viaje_model.asientos_disponibles = viaje.asientos_disponibles
    viaje_model.precio = viaje.precio
    return viaje_model
