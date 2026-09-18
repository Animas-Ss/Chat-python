# Plan de Trabajo

# TP: Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos

## 1. Objetivo del proyecto

El objetivo de este trabajo práctico es desarrollar una aplicación básica de comunicación **Cliente-Servidor** utilizando **Sockets en Python**.

El servidor deberá:

* [x] Escuchar conexiones en `localhost:5000`.
* [x] Recibir mensajes enviados por un cliente.
* [x] Guardar cada mensaje recibido en una base de datos SQLite.
* [x] Registrar información del mensaje:

  * `id`
  * `contenido`
  * `fecha_envio`
  * `ip_cliente`
* [x] Enviar una confirmación al cliente luego de recibir y almacenar correctamente el mensaje.
* [x] Manejar errores de puerto ocupado.
* [x] Manejar errores de acceso a la base de datos.

El cliente deberá:

* [x] Conectarse al servidor.
* [x] Permitir enviar múltiples mensajes durante la misma conexión.
* [x] Finalizar la comunicación cuando el usuario escriba `exito` o `éxito`.
* [x] Mostrar la respuesta enviada por el servidor para cada mensaje.

> **Nota:** La implementación actual trabaja con un cliente conectado por vez. El servidor acepta una conexión y atiende los mensajes de ese cliente hasta que finaliza la comunicación.

---

# 2. Tecnologías utilizadas

El proyecto utiliza:

* **Python 3**
* **Socket**
* **SQLite3**
* **Datetime**
* **pytest**
* **Git**
* **GitHub o Bitbucket**

---

# 2.1 Implementación de pruebas automatizadas

## Objetivo

Implementar pruebas automatizadas para verificar que los componentes del proyecto funcionen correctamente antes y después de integrarlos con el servidor.

Se utiliza **pytest** como framework de testing.

## Dependencia

Archivo `requirements.txt`:

```text
pytest==8.4.2
```

Instalación:

```bash
pip install -r requirements.txt
```

Verificación:

```bash
pytest --version
```

---

## Estructura actual de pruebas

Las pruebas se encuentran separadas del código de producción:

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
│   └── database.py
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

---

## Pruebas de la base de datos

Actualmente se comprueba:

* [x] La conexión con SQLite funciona correctamente.
* [x] La tabla `mensajes` se crea correctamente.
* [x] La tabla contiene las columnas requeridas.
* [x] Se puede guardar un mensaje.
* [x] El mensaje guarda correctamente el contenido.
* [x] Se registra la fecha de envío.
* [x] Se registra la IP del cliente.
* [x] Los errores de conexión son controlados.
* [x] Los errores al guardar mensajes son controlados.
* [ ] Se realizó una prueba intencional para provocar un `FAILED`.
* [x] Los tests muestran `PASSED` cuando la operación es correcta.

Actualmente existen **6 pruebas relacionadas con la base de datos**.

---

## Prueba de integración

Además de las pruebas individuales de SQLite, se implementó una prueba de integración:

```text
tests/test_integration.py
```

La prueba verifica la comunicación entre:

```text
Cliente
   ↓
Socket
   ↓
Servidor
   ↓
SQLite
   ↓
Respuesta del servidor
```

Se comprueba que:

* [x] El servidor pueda iniciarse en un puerto de prueba.
* [x] El cliente pueda conectarse.
* [x] El cliente pueda enviar un mensaje.
* [x] El servidor reciba el mensaje.
* [x] El mensaje sea almacenado en SQLite.
* [x] Se registre la fecha.
* [x] Se registre la IP del cliente.
* [x] El servidor genere una respuesta.
* [x] El cliente reciba la respuesta.

Actualmente existen:

```text
6 pruebas de base de datos
1 prueba de integración
------------------------
7 pruebas automatizadas
```

Resultado actual:

```text
7 passed
```

---

## Criterio de testing

Los tests no determinan el resultado mediante mensajes impresos manualmente como:

```text
OK - Mensaje guardado correctamente.
```

En su lugar, se utilizan aserciones de `pytest`:

```python
assert resultado == esperado
```

De esta manera, el framework determina automáticamente si una prueba fue exitosa o falló.

---

## Ejecución

Desde la raíz del proyecto:

```bash
pytest
```

Para obtener mayor detalle:

```bash
pytest -v
```

Resultado actual:

```text
7 passed
```

Para ejecutar únicamente las pruebas de base de datos:

```bash
pytest tests/test_database.py -v
```

Para ejecutar la prueba de integración:

```bash
pytest tests/test_integration.py -v
```

---

# 3. Estructura actual del proyecto

La estructura implementada actualmente es:

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
│   └── database.py
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

> `error_handler.py` fue contemplado inicialmente en la planificación, pero finalmente no se implementó como módulo independiente. El manejo de errores se encuentra actualmente dentro de `server.py` y `database.py`.

---

## Descripción de los archivos

### `client/client.py`

Contiene la lógica del cliente.

Responsabilidades implementadas:

* [x] Crear el socket del cliente.
* [x] Conectarse al servidor.
* [x] Solicitar mensajes al usuario.
* [x] Enviar mensajes.
* [x] Recibir respuestas.
* [x] Permitir múltiples mensajes.
* [x] Finalizar con `exito` o `éxito`.
* [x] Cerrar el socket.

---

### `server/server.py`

Es el punto principal de ejecución del servidor.

Responsabilidades implementadas:

* [x] Inicializar la base de datos.
* [x] Crear el socket.
* [x] Asociar el socket a `localhost` y al puerto correspondiente.
* [x] Escuchar conexiones.
* [x] Aceptar al cliente.
* [x] Recibir mensajes.
* [x] Guardar mensajes en SQLite.
* [x] Generar respuestas con timestamp.
* [x] Enviar respuestas al cliente.
* [x] Manejar errores de SQLite.
* [x] Manejar errores de puerto/socket.

El servidor utiliza `5000` como puerto predeterminado:

```python
def iniciar_servidor(puerto=5000):
```

Esto permite utilizar otro puerto durante las pruebas, por ejemplo:

```python
iniciar_servidor(5001)
```

---

### `server/socket_manager.py`

Contiene las funciones relacionadas con los sockets.

Actualmente implementa:

* [x] Crear socket TCP/IP.
* [x] Asociar el socket a localhost y al puerto indicado.
* [x] Escuchar conexiones.
* [x] Aceptar conexiones.
* [x] Recibir mensajes.
* [x] Enviar mensajes.

---

### `server/database.py`

Contiene la lógica relacionada con SQLite.

Responsabilidades:

* [x] Crear/conectar con la base de datos.
* [x] Crear la tabla `mensajes`.
* [x] Guardar mensajes.
* [x] Registrar contenido.
* [x] Registrar fecha y hora.
* [x] Registrar IP del cliente.
* [x] Manejar errores de SQLite.

---

# 4. Diseño de la base de datos

Se utiliza SQLite como sistema de almacenamiento.

## Tabla: `mensajes`

| Campo         | Tipo    | Descripción                                  |
| ------------- | ------- | -------------------------------------------- |
| `id`          | INTEGER | Identificador único del mensaje              |
| `contenido`   | TEXT    | Contenido enviado por el cliente             |
| `fecha_envio` | TEXT    | Fecha y hora en la que se recibió el mensaje |
| `ip_cliente`  | TEXT    | Dirección IP del cliente                     |

## SQL utilizado

```sql
CREATE TABLE IF NOT EXISTS mensajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contenido TEXT NOT NULL,
    fecha_envio TEXT NOT NULL,
    ip_cliente TEXT NOT NULL
);
```

---

# 5. Plan de desarrollo

## Etapa 1: Preparación del proyecto

### Objetivos

* Crear el repositorio.
* Definir la estructura.
* Crear los archivos iniciales.
* Configurar Git.

### Tareas

* [x] Crear el repositorio.
* [x] Clonar el repositorio localmente.
* [x] Crear la estructura inicial.
* [ ] Crear/finalizar el archivo `README.md`.
* [x] Crear `PLAN_DE_TRABAJO.md`.
* [x] Realizar el primer commit.

---

# Etapa 2: Implementación de la base de datos

## Objetivos

Implementar SQLite para almacenar los mensajes recibidos por el servidor.

### Tareas

* [x] Crear la base de datos.
* [x] Crear la tabla `mensajes`.
* [x] Implementar la conexión con SQLite.
* [x] Crear una función para guardar mensajes.
* [x] Registrar la fecha y hora.
* [x] Registrar la IP del cliente.
* [x] Manejar errores de acceso a la base de datos.
* [x] Crear pruebas automatizadas para la base de datos.

### Resultado

Cada mensaje recibido por el servidor queda registrado correctamente en SQLite.

---

# Etapa 3: Implementación del servidor

## Objetivos

Crear el servidor TCP utilizando el módulo `socket`.

### Configuración

```text
Host: localhost
Puerto predeterminado: 5000
Protocolo: TCP
```

### Tareas

* [x] Crear el socket TCP/IP.
* [x] Configurar `localhost`.
* [x] Configurar el puerto `5000`.
* [x] Asociar el socket utilizando `bind()`.
* [x] Colocar el servidor en modo escucha utilizando `listen()`.
* [x] Aceptar conexiones mediante `accept()`.
* [x] Obtener la IP del cliente.
* [x] Recibir mensajes mediante `recv()`.
* [x] Decodificar los mensajes recibidos.
* [x] Guardar los mensajes en SQLite.
* [x] Generar una confirmación con timestamp.
* [x] Enviar la respuesta al cliente.
* [x] Permitir especificar el puerto como parámetro para facilitar las pruebas.

### Comentarios

El código se encuentra separado en funciones y módulos para evitar concentrar toda la lógica en un único archivo.

---

# Etapa 4: Implementación del cliente

## Objetivos

Crear un cliente capaz de enviar múltiples mensajes al servidor.

### Tareas

* [x] Crear el socket del cliente.
* [x] Conectarse a `localhost:5000`.
* [x] Solicitar un mensaje al usuario.
* [x] Enviar el mensaje al servidor.
* [x] Esperar la respuesta.
* [x] Mostrar la confirmación recibida.
* [x] Permitir enviar múltiples mensajes.
* [x] Finalizar cuando el usuario escriba `exito` o `éxito`.
* [x] Cerrar correctamente el socket.

### Flujo implementado

```text
Usuario escribe un mensaje
        ↓
Cliente envía el mensaje
        ↓
Servidor recibe el mensaje
        ↓
Servidor guarda el mensaje en SQLite
        ↓
Servidor genera timestamp
        ↓
Servidor responde:
"Mensaje recibido: <timestamp>"
        ↓
Cliente muestra la respuesta
        ↓
Usuario puede enviar otro mensaje
```

---

# Etapa 5: Manejo de errores

## Objetivos

Implementar un manejo básico de errores para evitar que la aplicación finalice inesperadamente.

### Puerto ocupado

* [x] Detectar cuando el puerto está ocupado.
* [x] Mostrar un mensaje de error.
* [x] Cerrar el socket creado.

Ejemplo:

```text
Error al iniciar el servidor: [WinError 10048] ...
```

### Base de datos no accesible

* [x] Detectar errores de SQLite.
* [x] Informar el problema.
* [x] Evitar continuar con el servidor si la base de datos no puede inicializarse.

### Error durante el guardado

* [x] Capturar errores producidos al guardar mensajes.
* [x] Informar el error.

### Error de conexión del cliente

* [ ] Implementar manejo específico de errores de conexión dentro de `client.py`.

### Error durante envío/recepción

* [ ] Implementar manejo específico de errores de `sendall()` y `recv()`.

> Estos últimos casos no se agregaron porque no forman parte de las pruebas implementadas hasta el momento.

---

# Etapa 6: Pruebas locales

Las pruebas manuales se realizaron utilizando dos terminales.

## Terminal 1: Servidor

Desde la raíz del proyecto:

```bash
python -m server.server
```

Resultado:

```text
Tabla creada correctamente
Servidor escuchando en localhost:5000
```

## Terminal 2: Cliente

Desde la raíz del proyecto:

```bash
python client/client.py
```

Resultado:

```text
Cliente conectado al servidor
Ingrese su mensaje:
```

---

## Casos de prueba realizados

### Prueba 1: Envío de un mensaje

* [x] Enviar un mensaje.
* [x] Recibirlo en el servidor.
* [x] Guardarlo en SQLite.
* [x] Recibir respuesta con timestamp.

---

### Prueba 2: Múltiples mensajes

* [x] Enviar varios mensajes consecutivos.
* [x] Verificar que el servidor los reciba.
* [x] Verificar que se almacenen.
* [x] Verificar que el cliente reciba una respuesta por cada mensaje.

---

### Prueba 3: Verificación de base de datos

* [x] Verificar que los mensajes se almacenen.
* [x] Verificar contenido.
* [x] Verificar fecha.
* [x] Verificar IP.

---

### Prueba 4: Finalización

* [x] Finalizar mediante `exito`.
* [x] Finalizar mediante `éxito`.
* [x] Cerrar la conexión.

---

### Prueba 5: Puerto ocupado

* [x] Ejecutar un servidor en `localhost:5000`.
* [x] Intentar iniciar un segundo servidor utilizando el mismo puerto.
* [x] Verificar que se informe el error.

---

# 6. Pruebas automatizadas finales

Actualmente se dispone de:

```text
tests/test_database.py
        ↓
6 pruebas

tests/test_integration.py
        ↓
1 prueba

Total
        ↓
7 pruebas
```

Resultado:

```text
7 passed
```

Las pruebas fueron ejecutadas mediante:

```bash
pytest -v
```

Resultado obtenido:

```text
tests/test_database.py::test_create_table PASSED
tests/test_database.py::test_save_message PASSED
tests/test_database.py::test_save_message_date PASSED
tests/test_database.py::test_database_error PASSED
tests/test_database.py::test_save_message_error PASSED
tests/test_database.py::test_create_table_database_error PASSED
tests/test_integration.py::test_comunicacion_cliente_servidor PASSED

7 passed
```

---

# 7. Orden de desarrollo realizado

El desarrollo se realizó de manera incremental:

```text
1. Crear estructura del proyecto
        ↓
2. Implementar SQLite
        ↓
3. Crear pruebas de base de datos
        ↓
4. Implementar servidor Socket
        ↓
5. Integrar Socket + SQLite
        ↓
6. Implementar cliente
        ↓
7. Implementar manejo de errores
        ↓
8. Permitir puerto configurable
        ↓
9. Crear prueba de integración
        ↓
10. Verificar Socket + SQLite + respuesta
        ↓
11. Ejecutar las 7 pruebas
        ↓
12. Documentar el proyecto
```

---

# 8. División sugerida de responsabilidades

En caso de realizar el trabajo en grupo, las responsabilidades pueden dividirse de la siguiente manera.

## Servidor

* Inicialización del socket.
* Configuración de `localhost:5000`.
* Escucha de conexiones.
* Recepción de mensajes.

## Base de datos

* Configuración de SQLite.
* Creación de la tabla.
* Funciones de almacenamiento.
* Registro de fecha e IP.
* Manejo de errores de base de datos.

## Cliente

* Conexión con el servidor.
* Envío de múltiples mensajes.
* Recepción de respuestas.
* Finalización con `exito` o `éxito`.

## Trabajo conjunto

* Integración.
* Pruebas.
* Manejo de errores.
* Documentación.
* README.
* Revisión final.

---

# 9. Buenas prácticas aplicadas

Durante el desarrollo se aplicaron las siguientes prácticas:

* [x] Utilizar funciones con responsabilidades específicas.
* [x] Separar la lógica de sockets y base de datos.
* [x] Utilizar nombres descriptivos.
* [x] Manejar excepciones.
* [x] Cerrar sockets y conexiones.
* [x] Realizar pruebas después de implementar cada módulo.
* [x] Utilizar `pytest` para pruebas automatizadas.
* [x] Utilizar una base de datos temporal para la prueba de integración.
* [x] Utilizar parámetros para evitar dependencias innecesarias durante las pruebas.
* [x] Realizar commits durante el desarrollo.

---

# 10. Criterio de finalización

## Implementación

* [x] El servidor escucha correctamente en `localhost:5000`.
* [x] El cliente puede conectarse al servidor.
* [x] El cliente puede enviar múltiples mensajes.
* [x] El servidor recibe correctamente los mensajes.
* [x] Cada mensaje se guarda en SQLite.
* [x] Se registra la fecha y hora.
* [x] Se registra la IP del cliente.
* [x] El servidor responde con:

```text
Mensaje recibido: <timestamp>
```

* [x] El cliente muestra cada respuesta.
* [x] El cliente finaliza al escribir `exito` o `éxito`.
* [x] Se manejan errores de base de datos.
* [x] Se maneja el puerto ocupado.
* [x] El código está modularizado.
* [x] Se realizaron pruebas locales.
* [x] Se realizaron pruebas automatizadas.

## Pendiente

* [ ] Implementar manejo específico de errores de conexión del cliente.
* [ ] Implementar manejo específico de errores de envío/recepción.
* [ ] Completar y revisar el `README.md`.
* [ ] Realizar revisión final del código.
* [ ] Realizar commit final.
* [ ] Subir/verificar la versión final en GitHub o Bitbucket.

---

# 11. Entrega

La entrega final consistirá en:

* El enlace al repositorio de GitHub o Bitbucket.

O, en caso de no utilizar un repositorio:

* Un archivo comprimido `.zip` o `.rar`.

## Contenido de la entrega

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
│   └── database.py
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

---

# 12. Resultado final esperado

El resultado es una aplicación funcional donde un cliente puede enviar múltiples mensajes a un servidor mediante sockets TCP.

El servidor recibe cada mensaje, almacena su información en SQLite y responde al cliente con una confirmación que incluye la fecha y hora de recepción.

El proyecto permite aplicar conceptos de:

* Programación de redes.
* Arquitectura cliente-servidor.
* Sockets TCP/IP.
* Comunicación mediante sockets.
* Persistencia de datos.
* SQLite.
* Manejo de errores.
* Modularización.
* Pruebas automatizadas.
* Buenas prácticas de programación.
* Control de versiones con Git.
