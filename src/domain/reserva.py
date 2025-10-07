from domain.exceptions import CancelacionNoPermitida

class Reserva:
    def __init__(self, id, usuario, viaje, asiento, fecha_reserva, estado, precio_pagado):
        self.id = id
        self.usuario = usuario
        self.viaje = viaje
        self.asiento = asiento
        self.fecha_reserva = fecha_reserva
        self.estado = estado
        self.precio_pagado = precio_pagado
    
    def cancelar_reserva(self, fecha_actual):
    # Regla de negocio: solo se puede cancelar 24h antes del viaje
        if (self.viaje.fecha - fecha_actual).total_seconds() < 86400:
            raise CancelacionNoPermitida("No se puede cancelar con menos de 24h de antelación")
        self.estado = "Cancelada"
        self.viaje.cancelar_asiento()

    def esta_activa(self):
        return self.estado == "Activa"


    