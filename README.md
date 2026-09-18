# Chat Cliente-Servidor con Sockets y SQLite

## Descripción

Este proyecto implementa una aplicación básica de comunicación **cliente-servidor** desarrollada en Python utilizando **sockets TCP** y **SQLite**.

El cliente permite ingresar múltiples mensajes y enviarlos al servidor. El servidor recibe cada mensaje, registra la información en una base de datos SQLite y devuelve una respuesta indicando la fecha y hora en la que recibió el mensaje.

La comunicación finaliza cuando el cliente envía `exito` o `éxito`.

---

## Tecnologías utilizadas

* **Python 3**
* **Sockets TCP**
* **SQLite**
* **pytest**
* **Git / GitHub**

---

## Arquitectura del proyecto

```text
chat-python/
│
├── client/
│   └── client.py
│
├── server/
│   ├── __init__.py
│   ├── server.py
│   ├── socket_manager.py
│   ├── database.py
│   └── error_handler.py
│
├── database/
│   └── mensajes.db
│
├── tests/
│   ├── __init__.py
│   ├── test_database.py
│   └── test_integration.py
│
├── README.md
├── PLAN_DE_TRABAJO.md
└── requirements.txt
```

### Descripción de los componentes

#### `client/client.py`

Contiene la implementación del cliente.

Sus principales responsabilidades son:

* Crear el socket del cliente.
* Conectarse al servidor.
* Solicitar mensajes al usuario.
* Enviar mensajes.
* Recibir respuestas del servidor.
* Finalizar la comunicación mediante `exito` o `éxito`.

#### `server/server.py`

Es el punto principal de ejecución del servidor.

Sus responsabilidades son:

* Inicializar la base de datos.
* Crear el socket del servidor.
* Asociar el socket a `localhost` y al puerto correspondiente.
* Escuchar conexiones.
* Aceptar al cliente.
* Recibir mensajes.
* Guardar los mensajes en SQLite.
* Generar y enviar respuestas.
* Gestionar errores durante la ejecución.

El servidor utiliza el puerto `5000` por defecto, aunque la función permite especificar otro puerto para facilitar las pruebas:

```python
iniciar_servidor(puerto=5000)
```

#### `server/socket_manager.py`

Centraliza las operaciones relacionadas con sockets:

* Crear sockets.
* Asociar el servidor a una dirección y puerto.
* Escuchar conexiones.
* Aceptar conexiones.
* Recibir mensajes.
* Enviar mensajes.

#### `server/database.py`

Gestiona la comunicación con SQLite.

Se encarga de:

* Crear la conexión con la base de datos.
* Crear la tabla `mensajes`.
* Guardar los mensajes recibidos.
* Registrar la fecha de envío.
* Registrar la dirección IP del cliente.
* Gestionar errores de SQLite.

#### `tests/`

Contiene las pruebas automatizadas del proyecto.

Se utilizan pruebas unitarias para la base de datos y una prueba de integración para verificar la comunicación completa entre cliente, servidor y SQLite.

---

## Base de datos

El proyecto utiliza SQLite mediante el módulo estándar `sqlite3` de Python.

La base de datos se encuentra en:

```text
database/mensajes.db
```

La tabla utilizada es:

```sql
CREATE TABLE mensajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contenido TEXT NOT NULL,
    fecha_envio TEXT NOT NULL,
    ip_cliente TEXT NOT NULL
);
```

### Campos

| Campo         | Tipo    | Descripción                                |
| ------------- | ------- | ------------------------------------------ |
| `id`          | INTEGER | Identificador único del mensaje            |
| `contenido`   | TEXT    | Contenido enviado por el cliente           |
| `fecha_envio` | TEXT    | Fecha y hora en que se registra el mensaje |
| `ip_cliente`  | TEXT    | Dirección IP del cliente                   |

---

## Instalación

### Requisitos

Se necesita tener instalado:

* Python 3
* pip

SQLite no requiere una instalación adicional porque se utiliza el módulo `sqlite3` incluido en Python.

### Instalar dependencias

Desde la carpeta raíz del proyecto:

```bash
pip install -r requirements.txt
```

Las dependencias utilizadas para las pruebas se encuentran en:

```text
requirements.txt
```

---

## Ejecución

### 1. Iniciar el servidor

Desde la raíz del proyecto:

```bash
python -m server.server
```

El servidor debería mostrar:

```text
Tabla creada correctamente
Servidor escuchando en localhost:5000
```

### 2. Ejecutar el cliente

En otra terminal, desde la raíz del proyecto:

```bash
python client/client.py
```

El cliente mostrará:

```text
Cliente conectado al servidor
Ingrese su mensaje:
```

### 3. Enviar mensajes

Por ejemplo:

```text
Ingrese su mensaje: Hola servidor
Respuesta del servidor: Mensaje recibido: 2026-09-18T15:00:00...
```

Se pueden enviar múltiples mensajes durante la misma conexión.

### 4. Finalizar la comunicación

Para finalizar, ingresar:

```text
exito
```

o:

```text
éxito
```

El cliente enviará el mensaje de finalización y cerrará la conexión.

---

## Funcionamiento

El flujo principal de la aplicación es:

```text
┌──────────────┐
│    CLIENTE   │
└──────┬───────┘
       │
       │ Mensaje
       ▼
┌──────────────┐
│   SERVIDOR   │
└──────┬───────┘
       │
       ├───────────────┐
       │               │
       ▼               ▼
┌──────────────┐  ┌──────────────┐
│    SQLite    │  │  Respuesta   │
│              │  │  timestamp   │
└──────────────┘  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │    CLIENTE   │
                  └──────────────┘
```

Cada mensaje recibido por el servidor se almacena con:

* Contenido.
* Fecha y hora.
* Dirección IP del cliente.

---

## Manejo de errores

El proyecto contempla diferentes situaciones de error.

### Error de base de datos

Los errores producidos por SQLite son capturados mediante:

```python
except sqlite3.Error as e:
```

Esto permite informar el problema y evitar que el error quede sin controlar.

### Puerto ocupado

Si el puerto utilizado por el servidor ya está ocupado, se captura el error producido por el socket:

```python
except OSError as e:
```

El servidor informa el problema y finaliza correctamente.

### Cierre de recursos

Al finalizar la comunicación se cierran:

* Conexión del cliente.
* Conexión del servidor.

De esta forma se liberan los recursos utilizados por los sockets.

---

## Pruebas

El proyecto utiliza **pytest** para realizar pruebas automatizadas.

Para ejecutar todas las pruebas:

```bash
pytest -v
```

Actualmente se dispone de **7 pruebas automatizadas**.

### Pruebas de base de datos

Se verifica:

* Creación de la tabla.
* Existencia de las columnas requeridas.
* Guardado de mensajes.
* Guardado de la dirección IP.
* Generación y almacenamiento de la fecha.
* Manejo de errores de conexión.
* Manejo de errores durante el guardado.
* Manejo de errores durante la creación de la tabla.

### Prueba de integración

También se dispone de una prueba que verifica el funcionamiento conjunto de:

```text
Socket
   ↓
Servidor
   ↓
SQLite
   ↓
Respuesta al cliente
```

La prueba comprueba que:

* El servidor acepta la conexión.
* El cliente puede enviar un mensaje.
* El servidor procesa el mensaje.
* El mensaje se almacena en SQLite.
* La fecha almacenada tiene un formato válido.
* Se registra la IP del cliente.
* El servidor devuelve una respuesta con timestamp.

Resultado esperado:

```text
7 passed
```

---

## Ejecución de una prueba específica

Para ejecutar solamente las pruebas de base de datos:

```bash
pytest tests/test_database.py -v
```

Para ejecutar solamente la prueba de integración:

```bash
pytest tests/test_integration.py -v
```

---

## Flujo de trabajo

El desarrollo del proyecto se realizó de forma incremental:

```text
Estructura del proyecto
        ↓
Base de datos SQLite
        ↓
Pruebas de base de datos
        ↓
Servidor Socket
        ↓
Integración Socket + SQLite
        ↓
Cliente
        ↓
Manejo de errores
        ↓
Pruebas de integración
        ↓
Documentación
```

Cada etapa fue probada antes de continuar con la siguiente.

---

## Estado del proyecto

Actualmente se encuentran implementados:

* [x] Cliente TCP.
* [x] Servidor TCP.
* [x] Comunicación cliente-servidor.
* [x] Envío de múltiples mensajes.
* [x] Finalización mediante `exito` o `éxito`.
* [x] Persistencia de mensajes mediante SQLite.
* [x] Registro de fecha y hora.
* [x] Registro de IP del cliente.
* [x] Manejo de errores de SQLite.
* [x] Manejo de errores de socket.
* [x] Pruebas unitarias.
* [x] Prueba de integración.
* [x] Documentación del proyecto.

---

## Autor

**Sebastián Sosa**

Proyecto académico desarrollado en Python para la implementación de una comunicación básica cliente-servidor mediante sockets y base de datos SQLite.
