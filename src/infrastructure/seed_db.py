from infrastructure.db_config import SessionLocal
from infrastructure.models import UsuarioModel, ViajeModel
from datetime import datetime, timedelta
import uuid

session = SessionLocal()

# ---- Crear usuario de prueba ----
usuario = UsuarioModel(
    id=str(uuid.uuid4()),
    nombre="Javi",
    apellido_1="Montes",
    apellido_2="V",
    email="javi@example.com",
    contrasena="1234"
)
session.add(usuario)

# ---- Crear viaje de prueba ----
viaje = ViajeModel(
    id=str(uuid.uuid4()),
    origen="Madrid",
    destino="Barcelona",
    fecha=datetime.now() + timedelta(days=10),  # viaje dentro de 10 días
    asientos_totales=40,
    asientos_disponibles=40,
    precio=50.0
)
session.add(viaje)

session.commit()
print("Datos de prueba creados correctamente!")
print(f"Usuario ID: {usuario.id}")
print(f"Viaje ID: {viaje.id}")
session.close()

