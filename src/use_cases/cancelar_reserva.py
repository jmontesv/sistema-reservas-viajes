
class CancelarReserva:
    
    def __init__(self, reserva_repository):
        self.reserva_repository = reserva_repository

    def execute(self, reserva_id):
        reserva = self.reserva_repository.get_by_id(reserva_id)
        if not reserva:
            raise Exception("Reserva no encontrada")
        self.reserva_repository.cancel(reserva)
        reserva.viaje.cancelar_asiento() 
        return reserva