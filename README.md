# Sistema de Reservas de Viajes ✈️

Este proyecto es un **ejercicio práctico de Arquitectura Limpia en Python**, donde desarrollo un sistema de reservas de viajes utilizando repositorios en memoria, casos de uso bien definidos y una API con Flask.

El objetivo es aprender y aplicar principios de **Clean Architecture / Arquitectura Hexagonal** en un proyecto realista, empezando simple y evolucionando poco a poco.

---

## 🏗️ Arquitectura

La estructura del proyecto sigue una separación por capas:

```
src/
 ├── domain/              # Entidades del dominio (Usuario, Viaje, Reserva, etc.)
 ├── repositories/        # Interfaces (contratos de repositorios)
 ├── infrastructure/      # Implementaciones concretas (en memoria, DB en el futuro)
 │    └── repositories/
 ├── use_cases/           # Casos de uso (ej: ReservarViaje)
 └── interface/           # Interfaz con el mundo exterior (Flask API)
```

### Componentes clave

* **Dominio**: Define las entidades principales (`Usuario`, `Viaje`, `Reserva`, `Asiento`).
* **Repositorios**: Clases abstractas que actúan como contratos (`UsuarioRepository`, `ViajeRepository`, `ReservaRepository`).
* **Infraestructura**: Implementaciones en memoria (`UsuarioRepositoryMemory`, `ViajeRepositoryMemory`, `ReservaRepositoryMemory`).
* **Casos de uso**: Ejemplo `ReservarViaje`, que orquesta la lógica de negocio.
* **Interfaz**: API Flask que expone endpoints como `/reservar`.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sistema-reservas-viajes.git
cd sistema-reservas-viajes
```

### 2. Crear y activar entorno virtual (ejemplo con conda)

```bash
conda create -n reservas-viajes python=3.13.7 -y
conda activate reservas-viajes
```

### 3. Instalar dependencias

```bash
pip install flask
```

### 4. Ejecutar la app

Desde la carpeta `src/`:

```bash
python -m interface.app
```

La aplicación se ejecutará en `http://127.0.0.1:5000`.

---

## 📌 Ejemplo de uso

### Crear una reserva

**Endpoint:**

```http
POST /reservar
```

**Body (JSON):**

```json
{
  "usuario_id": "1",
  "viaje_id": "101"
}
```

**Respuesta (ejemplo):**

```json
{
  "id": "c0a8027a-bfc1-11ee-a0f6-0242ac120002",
  "usuario": "Juan",
  "viaje": "101",
  "precio_pagado": 45.0,
  "fecha_reserva": "2025-10-05T17:45:30.123456",
  "estado": "Activa"
}
```

---

## 📍 Roadmap

* [x] Entidades del dominio
* [x] Repositorios abstractos
* [x] Implementaciones en memoria
* [x] Caso de uso `ReservarViaje`
* [x] Endpoint `/reservar` con Flask
* [x] Listar reservas de un usuario
* [ ] Persistencia en base de datos real
* [ ] Autenticación de usuarios
* [ ] Pruebas unitarias y de integración

---

## 📖 Aprendizaje

Este proyecto me está ayudando a:

* Comprender cómo aplicar **Arquitectura Limpia** en Python.
* Practicar separación de responsabilidades y bajo acoplamiento.
* Usar repositorios en memoria para simular bases de datos.
* Integrar un dominio rico con Flask como interfaz.

---

## 🤝 Contribuciones

Cualquier sugerencia o idea para mejorar la arquitectura, nuevas funcionalidades o buenas prácticas será más que bienvenida.

---

## 🏷️ Tecnologías

* Python 3.13.7
* Flask
* Arquitectura Limpia / Clean Architecture
