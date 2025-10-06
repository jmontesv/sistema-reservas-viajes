
class ListarReservasPorUsuario:
    
    def __init__(self, reserva_repository):
        self.reserva_repository = reserva_repository

    def execute(self, usuario_id):
        # Obtener reservas 
        reservas = self.reserva_repository.get_by_user(usuario_id)
        return reservas