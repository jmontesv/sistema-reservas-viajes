from domain.usuario import Usuario
from infrastructure.repositories.usuario_repository import UsuarioRepository

class UsuarioRepositoryMemory(UsuarioRepository):
    def __init__(self):
        self.usuarios = []

        # Usuario de prueba
        usuario_prueba = Usuario(
            id="1",
            nombre="Juan",
            apellido_1="Pérez",
            apellido_2="García",
            email="juan@email.com",
            contrasena="1234"
        )
        self.usuarios.append(usuario_prueba)

    def add(self, usuario: Usuario):
        self.usuarios.append(usuario)

    def get_by_id(self, id):
        return next((u for u in self.usuarios if u.id == id), None)

    def get_by_email(self, email):
        return next((u for u in self.usuarios if u.email == email), None)
