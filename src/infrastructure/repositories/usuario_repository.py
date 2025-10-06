from abc import ABC, abstractmethod
from domain.usuario import Usuario

class UsuarioRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id):
        pass
    
    @abstractmethod
    def get_by_email(self, email):
        pass

    @abstractmethod
    def add(self, usuario: Usuario):
        pass