from domain.viaje import Viaje
from infrastructure.repositories.viaje_respository import ViajeRepository

class ViajeRepositoryMemory(ViajeRepository):
    def __init__(self):
        self.viajes = []

        # Viaje de prueba
        viaje_prueba = Viaje(
            id="101",
            origen="Madrid",
            destino="Barcelona",
            fecha="2025-10-10",
            asientos_totales=10,
            asientos_disponibles=10,
            precio=50
        )
        self.viajes.append(viaje_prueba)

    def add(self, viaje: Viaje):
        self.viajes.append(viaje)

    def get_by_id(self, id):
        viaje_encontrado = next((v for v in self.viajes if v.id == id), None)
        return viaje_encontrado

    def update(self, viaje: Viaje):
        for idx, v in enumerate(self.viajes):
            if v.id == viaje.id:
                self.viajes[idx] = viaje
                break

    def search(self, origen: str = None, destino: str = None):
        resultados = self.viajes
        if origen:
            resultados = [v for v in resultados if v.origen == origen]
        if destino:
            resultados = [v for v in resultados if v.destino == destino]
        return resultados