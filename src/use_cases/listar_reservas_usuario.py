from mappers.reserva_mapper import reserva_model_to_entity
from domain.reserva import Reserva

class ListarReservasPorUsuario:
    
    def __init__(self, reserva_repository):
        self.reserva_repository = reserva_repository

    def execute(self, usuario_id):
        # Obtener reservas 
        reservas_model = self.reserva_repository.get_by_user(usuario_id)
        reservas = []
        for reserva_model in reservas_model:
            reserva = reserva_model_to_entity(reserva_model)
            reservas.append(reserva)
        return reservas