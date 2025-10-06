from abc import ABC, abstractmethod
from domain.viaje import Viaje


class ViajeRepository(ABC):

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod    
    def search(self, origen, destino, fecha):
        pass

    @abstractmethod
    def update(self, viaje: Viaje):
        pass

    @abstractmethod
    def add(self, viaje: Viaje):
        pass
