from domain.exceptions import ReservaNoEncontrada
from mappers.reserva_mapper import reserva_model_to_entity, entity_to_reserva_model


class CancelarReserva:
    
    def __init__(self, reserva_repository):
        self.reserva_repository = reserva_repository

    def execute(self, reserva_id):
        reserva_model = self.reserva_repository.get_by_id(reserva_id)
        if not reserva_model:
            raise ReservaNoEncontrada("Reserva no encontrada")
        
        # Convertir modelo a entidad de dominio
        reserva = reserva_model_to_entity(reserva_model)

        # Cancelar reserva 
        from datetime import datetime
        reserva.cancelar_reserva(datetime.now())

        # Convertir la entidad de nuevo a modelo ORM y persistir cambios
        reserva_model = entity_to_reserva_model(reserva, reserva_model)
        self.reserva_repository.update(reserva_model)
        return reserva

      