from flask import Flask, request, jsonify
from datetime import datetime
from infrastructure.repositories.reserva_repository_db import ReservaRepositoryDB
from infrastructure.repositories.viaje_repository_db import ViajeRepositoryDB
from infrastructure.repositories.usuario_repository_db import UsuarioRepositoryDB
from use_cases.reservar_viaje import ReservarViaje
from use_cases.listar_reservas_usuario import ListarReservasPorUsuario
from use_cases.cancelar_reserva import CancelarReserva
from use_cases.listar_viajes_disponibles import ListarViajesDisponibles
from domain.exceptions import CancelacionNoPermitida
from domain.exceptions import ReservaNoEncontrada

app = Flask(__name__)


# Crear instancias de los repositorios en memoria
usuario_repository = UsuarioRepositoryDB()
viaje_repository = ViajeRepositoryDB()
reserva_repository = ReservaRepositoryDB()

# Instanciar el caso de uso
reservar_viaje_use_case = ReservarViaje(viaje_repository, reserva_repository, usuario_repository)
listar_reservas_por_usuario = ListarReservasPorUsuario(reserva_repository)
cancelar_reserva = CancelarReserva(reserva_repository)
listar_viajes_disponibles = ListarViajesDisponibles(viaje_repository)

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

@app.route("/reservas/<reserva_id>/cancelar", methods=["POST"])
def cancelar_reserva_endpoint(reserva_id):
    try:
        reserva = cancelar_reserva.execute(reserva_id)
        resultado = {
            "id": reserva.id,
            "usuario": reserva.usuario.id,
            "viaje": {
                "origen": reserva.viaje.origen,
                "destino": reserva.viaje.destino,
                "fecha": reserva.viaje.fecha
            },
            "fecha_reserva": reserva.fecha_reserva.isoformat(),
            "estado": reserva.estado,
            "precio_pagado": reserva.precio_pagado
        }
        return jsonify(resultado), 200
    except ReservaNoEncontrada as e:
        return jsonify({"error": str(e)}), 404 
    except CancelacionNoPermitida as e:
        return jsonify({"error": str(e)}), 403 
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/viajes/<fecha>", methods=["GET"])
def listar_viajes(fecha):
    origen = request.args.get("origen")
    destino = request.args.get("destino") 
    fecha_dt = datetime.strptime(fecha.strip(), "%Y-%m-%d") 
    try:
        viajes = listar_viajes_disponibles.execute(fecha_dt, origen, destino)
        viajes_serializados = [viaje.to_dict() for viaje in viajes]
        print(viajes_serializados)

        return jsonify(viajes_serializados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
        


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)