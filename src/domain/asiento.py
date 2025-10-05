
class Asiento:
    ESTADO_LIBRE = "Libre"
    ESTADO_RESERVADO = "Reservado"

    def __init__(self, numero, estado=ESTADO_LIBRE):
        self.numero = numero
        self.estado = estado

    def reservar(self):
        if self.estado == self.ESTADO_RESERVADO:
            raise Exception(f"Asiento {self.numero} ya está reservado")
        self.estado = self.ESTADO_RESERVADO

    def liberar(self):
        if self.estado == self.ESTADO_LIBRE:
            raise Exception(f"Asiento {self.numero} ya está libre")
        self.estado = self.ESTADO_LIBRE

    def esta_disponible(self):
        return self.estado == self.ESTADO_LIBRE