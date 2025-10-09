from infrastructure.repositories.viaje_respository import ViajeRepository
from mappers.viaje_mapper import viaje_model_to_entity

class ListarViajesDisponibles:
    
    def __init__(self, viaje_respository: ViajeRepository):
        self.viaje_repository = viaje_respository
    
    def execute(self, origen=None, destino=None, fecha=None):
        viajes_models = self.viaje_repository.search(origen, destino, fecha)

        # Pasamos los modelos a entidades
        viajes = [viaje_model_to_entity(viaje) for viaje in viajes_models]
        print(viajes)
        return viajes
        
    

