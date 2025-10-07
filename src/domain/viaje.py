from datetime import datetime

class Viaje:
    def __init__(self, id, origen, destino, fecha, asientos_totales, asientos_disponibles, precio):
        self.id = id
        self.origen = origen
        self.destino = destino
        # Convertimos fecha a datetime si viene como string
        if isinstance(fecha, str):
            self.fecha = datetime.fromisoformat(fecha)
        else:
            self.fecha = fecha
        self.asientos_totales = asientos_totales
        self.asientos_disponibles = asientos_disponibles
        self.precio = precio

    def tiene_asientos_disponibles(self):
        return self.asientos_disponibles > 0
    
    def reservar_asiento(self):
        if not self.tiene_asientos_disponibles():
            raise Exception("No quedan asientos disponibles")
        self.asientos_disponibles -= 1

    def cancelar_asiento(self):
        if self.asientos_disponibles < self.asientos_totales:
            self.asientos_disponibles += 1

    def calcular_precio(self):
        ocupacion = (self.asientos_totales - self.asientos_disponibles) / self.asientos_totales
        if ocupacion >= 0.8:
            return self.precio * 1.2
        return self.precio