from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.db_config import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"
    id = Column(String(36), primary_key=True)
    nombre = Column(String(50))
    apellido_1 = Column(String(50))
    apellido_2 = Column(String(50))
    email = Column(String(100), unique=True)
    contrasena = Column(String(100))
    reservas = relationship("ReservaModel", back_populates="usuario")


class ViajeModel(Base):
    __tablename__ = "viajes"
    id = Column(String(36), primary_key=True)
    origen = Column(String(100))
    destino = Column(String(100))
    fecha = Column(DateTime)
    asientos_totales = Column(Integer)
    asientos_disponibles = Column(Integer)
    precio = Column(Float)
    reservas = relationship("ReservaModel", back_populates="viaje")

class ReservaModel(Base):
    __tablename__ = "reservas"
    id = Column(String(36), primary_key=True)
    usuario_id = Column(String(36), ForeignKey("usuarios.id"))
    viaje_id = Column(String(36), ForeignKey("viajes.id"))
    fecha_reserva = Column(DateTime)
    estado = Column(String(20))
    precio_pagado = Column(Float)
    usuario = relationship("UsuarioModel", back_populates="reservas")
    viaje = relationship("ViajeModel", back_populates="reservas")

