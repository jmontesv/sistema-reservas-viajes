from abc import ABC, abstractmethod
from domain.reserva import Reserva

class ReservaRepository(ABC):

    @abstractmethod
    def add_reserva(self, reserva: Reserva):
        pass

    @abstractmethod
    def get_by_id(self, id: str):
        pass

    @abstractmethod
    def get_by_user(self, usuario_id: str):
        pass

    @abstractmethod
    def cancel(self, reserva: Reserva):
        pass

    @abstractmethod
    def update(self, reserva: Reserva):
        pass