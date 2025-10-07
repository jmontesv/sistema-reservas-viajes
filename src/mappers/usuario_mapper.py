from domain.usuario import Usuario
from infrastructure.models import UsuarioModel

def usuario_model_to_entity(usuario_model: UsuarioModel) -> Usuario:
    return Usuario(
        id=usuario_model.id,
        nombre=usuario_model.nombre,
        apellido_1=usuario_model.apellido_1,
        apellido_2=usuario_model.apellido_2,
        email=usuario_model.email,
        contrasena=usuario_model.contrasena
    )

def entity_to_usuario_model(usuario: Usuario, usuario_model: UsuarioModel) -> UsuarioModel:
    usuario_model.nombre = usuario.nombre
    usuario_model.apellido_1 = usuario.apellido_1
    usuario_model.apellido_2 = usuario.apellido_2
    usuario_model.email = usuario.email
    usuario_model.contrasena = usuario.contrasena
    return usuario_model
