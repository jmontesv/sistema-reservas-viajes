from flask import Flask, request, jsonify
from infrastructure.usuario_repository_memory import UsuarioRepositoryMemory
from infrastructure.viaje_repository_memory import ViajeRepositoryMemory
from infrastructure.reserva_repository_memory import ReservaRepositoryMemory
from use_cases.reservar_viaje import ReservarViaje
from use_cases.listar_reservas_usuario import ListarReservasPorUsuario

app = Flask(__name__)


# Crear instancias de los repositorios en memoria
usuario_repository = UsuarioRepositoryMemory()
viaje_repository = ViajeRepositoryMemory()
reserva_repository = ReservaRepositoryMemory()

# Instanciar el caso de uso
reservar_viaje_use_case = ReservarViaje(viaje_repository, reserva_repository, usuario_repository)
listar_reservas_por_usuario = ListarReservasPorUsuario(reserva_repository)

@app.route("/reservar", methods=["POST"])
def reservar():
    data = request.json
    usuario_id = data.get("usuario_id")
    viaje_id = data.get("viaje_id")

    try:
        reserva = reservar_viaje_use_case.execute(usuario_id, viaje_id)
        return jsonify({
            "id": reserva.id,
            "usuario": reserva.usuario.nombre,
            "viaje": reserva.viaje.id,
            "precio_pagado": reserva.precio_pagado,
            "fecha_reserva": reserva.fecha_reserva.isoformat(),
            "estado": reserva.estado
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/reservas/<usuario_id>", methods=["GET"])
def listar_reservas(usuario_id):
    reservas = listar_reservas_por_usuario.execute(usuario_id)
    resultado = [
        {
            "id": r.id,
            "viaje": {
                "origen": r.viaje.origen,
                "destino": r.viaje.destino,
                "fecha": r.viaje.fecha
            },
            "fecha_reserva": r.fecha_reserva.isoformat(),
            "estado": r.estado
        }
        for r in reservas
    ]
    return jsonify(resultado)  

if __name__ == "__main__":
    app.run(debug=True)