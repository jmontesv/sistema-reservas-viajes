
class CancelacionNoPermitida(Exception):
    """Se lanza cuando se intenta cancelar una reserva con menos de 24h de antelación."""
    pass


class ReservaNoEncontrada(Exception):
    """Se lanza cuando no se encuentra una reserva por ID."""
    pass
