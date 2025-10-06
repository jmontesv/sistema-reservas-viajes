from infrastructure.repositories.reserva_repository import ReservaRepository

class ReservaRepositoryMemory(ReservaRepository):
    def __init__(self):
        self.reservas = []
    
    def add_reserva(self, reserva):
        self.reservas.append(reserva)
    
    def get_by_id(self, id):
        reserva_encontrada = list(filter(lambda r: r.id == id, self.reservas))
        if reserva_encontrada:
            return reserva_encontrada[0]
        return None
    
    def get_by_user(self, usuario_id):
        reservas = list(filter(lambda r: r.usuario.id == usuario_id, self.reservas))
        return reservas

    def cancel(self, reserva):
        reserva.cancelar_reserva()