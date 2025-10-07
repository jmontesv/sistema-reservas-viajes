from infrastructure.db_config import Base, engine
from infrastructure.models import UsuarioModel, ViajeModel, ReservaModel

# Crea todas las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)
print("Tablas creadas correctamente!")
