# Plan de Trabajo

## TP: Implementación de un Chat Básico Cliente-Servidor con Sockets y Base de Datos

## 1. Objetivo del proyecto

El objetivo de este trabajo práctico es desarrollar una aplicación básica de comunicación **Cliente-Servidor** utilizando **Sockets en Python**.

El servidor deberá:

* Escuchar conexiones en `localhost:5000`.
* Recibir mensajes enviados por uno o varios clientes.
* Guardar cada mensaje recibido en una base de datos SQLite.
* Registrar información del mensaje:

  * `id`
  * `contenido`
  * `fecha_envio`
  * `ip_cliente`
* Enviar una confirmación al cliente luego de recibir y almacenar correctamente el mensaje.
* Manejar posibles errores, como:

  * Puerto ocupado.
  * Problemas de conexión.
  * Base de datos no accesible.
  * Errores durante el envío o recepción de datos.

El cliente deberá:

* Conectarse al servidor.
* Permitir enviar múltiples mensajes.
* Finalizar la conexión cuando el usuario escriba `éxito`.
* Mostrar la respuesta enviada por el servidor para cada mensaje.

---

# 2. Tecnologías a utilizar

El proyecto será desarrollado utilizando las siguientes tecnologías:

* **Python 3**
* **Socket**
* **SQLite3**
* **Datetime**
* **Git**
* **GitHub o Bitbucket**

---

# Etapa 2.1: Implementación de pruebas automatizadas

## Objetivo

Implementar pruebas automatizadas para verificar que los componentes del proyecto funcionen correctamente antes de integrarlos con el servidor.

Se utilizará **pytest** como framework de testing.

## Dependencia

Agregar al archivo `requirements.txt`:

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

## Estructura de pruebas

Las pruebas estarán separadas del código de producción:

```text
chat-cliente-servidor/
│
├── client/
│   └── cliente.py
│
├── server/
│   ├── servidor.py
│   ├── socket_manager.py
│   ├── database.py
│   └── error_handler.py
│
├── database/
│   └── mensajes.db
│
├── tests/
│   ├── __init__.py
│   └── test_database.py
│
├── README.md
├── PLAN_DE_TRABAJO.md
└── requirements.txt
```

---

## Pruebas de la base de datos

Se deberán comprobar como mínimo:

* [ ] La conexión con SQLite funciona correctamente.
* [ ] La tabla `mensajes` se crea correctamente.
* [ ] La tabla contiene las columnas requeridas.
* [ ] Se puede guardar un mensaje.
* [ ] El mensaje guarda correctamente el contenido.
* [ ] Se registra la fecha de envío.
* [ ] Se registra la IP del cliente.
* [ ] Los errores de conexión son controlados.
* [ ] Los errores al guardar mensajes son controlados.
* [ ] Los tests detectan correctamente un fallo.
* [ ] Los tests muestran `PASSED` cuando la operación es correcta.
* [ ] Los tests muestran `FAILED` cuando la operación no cumple lo esperado.

---

## Criterio de testing

Los tests no deberán determinar el resultado mediante mensajes impresos manualmente como:

```text
OK - Mensaje guardado correctamente.
```

En su lugar, se utilizarán aserciones de `pytest`:

```python
assert resultado == esperado
```

De esta manera, el framework será responsable de determinar si una prueba fue exitosa o falló.

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

Ejemplo esperado:

```text
tests/test_database.py::test_crear_tabla PASSED
tests/test_database.py::test_guardar_mensaje PASSED
```

---

## Objetivo de esta etapa

Antes de conectar SQLite con el servidor, se deberá comprobar automáticamente que el módulo `database.py` funciona correctamente.

El flujo será:

```text
database.py
     │
     ▼
pytest
     │
     ├── test conexión
     ├── test tabla
     ├── test estructura
     └── test inserción
             │
             ▼
        SQLite
```


# 3. Estructura propuesta del proyecto

Se propone organizar el proyecto de la siguiente manera:

```text
chat-cliente-servidor/
│
├── client/
│   └── cliente.py
│
├── server/
│   ├── servidor.py
│   ├── socket_manager.py
│   ├── database.py
│   └── error_handler.py
│
├── database/
│   └── mensajes.db
│
├── README.md
├── PLAN_DE_TRABAJO.md
└── requirements.txt
```

## Descripción de los archivos

### `cliente.py`

Contendrá la lógica necesaria para:

* Crear el socket del cliente.
* Conectarse al servidor.
* Solicitar mensajes al usuario.
* Enviar mensajes.
* Recibir respuestas del servidor.
* Finalizar la conexión cuando el usuario escriba `éxito`.

---

### `servidor.py`

Será el punto principal de ejecución del servidor.

Su responsabilidad será:

* Inicializar los componentes necesarios.
* Configurar el servidor.
* Iniciar la escucha de conexiones.
* Coordinar las funciones del sistema.

---

### `socket_manager.py`

Contendrá las funciones relacionadas con los sockets.

Por ejemplo:

* Inicializar el socket TCP/IP.
* Asociar el socket a `localhost:5000`.
* Escuchar conexiones.
* Aceptar clientes.
* Recibir mensajes.

---

### `database.py`

Contendrá toda la lógica relacionada con SQLite.

Sus responsabilidades serán:

* Crear o conectar con la base de datos.
* Crear la tabla de mensajes si todavía no existe.
* Guardar mensajes recibidos.
* Registrar:

  * Contenido.
  * Fecha y hora.
  * Dirección IP del cliente.

---

### `error_handler.py`

Contendrá funciones o lógica destinada a manejar errores.

Ejemplos:

* Puerto ocupado.
* Error al iniciar el socket.
* Error de conexión con la base de datos.
* Error durante la recepción de mensajes.
* Error al enviar una respuesta al cliente.

---

# 4. Diseño de la base de datos

Se utilizará SQLite como sistema de almacenamiento.

## Tabla: `mensajes`

La tabla tendrá la siguiente estructura:

| Campo         | Tipo    | Descripción                                  |
| ------------- | ------- | -------------------------------------------- |
| `id`          | INTEGER | Identificador único del mensaje              |
| `contenido`   | TEXT    | Contenido enviado por el cliente             |
| `fecha_envio` | TEXT    | Fecha y hora en la que se recibió el mensaje |
| `ip_cliente`  | TEXT    | Dirección IP del cliente                     |

## Propuesta SQL

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

* Crear el repositorio del proyecto.
* Definir la estructura de carpetas.
* Crear los archivos iniciales.
* Configurar Git.

### Tareas

* [ ] Crear el repositorio en GitHub o Bitbucket.
* [ ] Clonar el repositorio localmente.
* [ ] Crear la estructura inicial del proyecto.
* [ ] Crear el archivo `README.md`.
* [ ] Crear el archivo `PLAN_DE_TRABAJO.md`.
* [ ] Realizar el primer commit.

---

# Etapa 2: Implementación de la base de datos

### Objetivos

Implementar SQLite para almacenar los mensajes recibidos por el servidor.

### Tareas

* [ ] Crear la base de datos.
* [ ] Crear la tabla `mensajes`.
* [ ] Implementar la conexión con SQLite.
* [ ] Crear una función para guardar mensajes.
* [ ] Registrar la fecha y hora del mensaje.
* [ ] Registrar la IP del cliente.
* [ ] Manejar errores de acceso a la base de datos.

### Resultado esperado

Cada mensaje recibido por el servidor deberá quedar registrado correctamente en la base de datos.

---

# Etapa 3: Implementación del servidor

### Objetivos

Crear el servidor TCP utilizando el módulo `socket`.

### Configuración requerida

```text
Host: localhost
Puerto: 5000
Protocolo: TCP/IP
```

### Tareas

* [ ] Crear el socket TCP/IP.
* [ ] Configurar la dirección `localhost`.
* [ ] Configurar el puerto `5000`.
* [ ] Asociar el socket utilizando `bind()`.
* [ ] Colocar el servidor en modo escucha utilizando `listen()`.
* [ ] Aceptar conexiones mediante `accept()`.
* [ ] Obtener la IP del cliente.
* [ ] Recibir mensajes mediante `recv()`.
* [ ] Decodificar los mensajes recibidos.
* [ ] Guardar los mensajes en SQLite.
* [ ] Generar una confirmación con timestamp.
* [ ] Enviar la respuesta al cliente.

### Comentarios importantes

El código deberá incluir comentarios explicando las configuraciones principales.

Ejemplo:

```python
# Configuración del socket TCP/IP
```

También deberán explicarse las secciones relacionadas con:

```python
# Asociación del socket con localhost y puerto 5000

# Configuración del servidor en modo escucha

# Recepción de datos enviados por el cliente

# Almacenamiento del mensaje en SQLite

# Envío de confirmación al cliente
```

---

# Etapa 4: Implementación del cliente

### Objetivos

Crear un cliente capaz de enviar múltiples mensajes al servidor.

### Tareas

* [ ] Crear el socket del cliente.
* [ ] Conectarse a `localhost:5000`.
* [ ] Solicitar un mensaje al usuario.
* [ ] Enviar el mensaje al servidor.
* [ ] Esperar la respuesta del servidor.
* [ ] Mostrar la confirmación recibida.
* [ ] Permitir enviar múltiples mensajes.
* [ ] Finalizar cuando el usuario escriba `éxito`.
* [ ] Cerrar correctamente el socket.

### Flujo esperado

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

### Objetivos

Implementar un manejo básico de errores para evitar que la aplicación finalice inesperadamente.

## Errores a considerar

### Puerto ocupado

Puede ocurrir si:

* El servidor ya se encuentra ejecutándose.
* Otro programa está utilizando el puerto `5000`.

Se deberá capturar el error y mostrar un mensaje claro.

---

### Base de datos no accesible

Puede ocurrir si:

* No se puede crear el archivo.
* No existen permisos suficientes.
* La conexión con SQLite falla.

El servidor deberá informar el error sin finalizar inesperadamente.

---

### Error de conexión

Puede ocurrir si:

* El servidor no está ejecutándose.
* El cliente intenta conectarse a un puerto incorrecto.

El cliente deberá informar el problema al usuario.

---

### Error durante la comunicación

Se deberán contemplar errores durante:

* Envío de mensajes.
* Recepción de mensajes.
* Decodificación de datos.

---

# Etapa 6: Pruebas locales

Las pruebas deberán realizarse utilizando dos terminales.

## Terminal 1: Servidor

Ejecutar:

```bash
python servidor.py
```

Resultado esperado:

```text
Servidor iniciado.
Escuchando en localhost:5000...
```

---

## Terminal 2: Cliente

Ejecutar:

```bash
python cliente.py
```

Resultado esperado:

```text
Conectado al servidor.

Ingrese un mensaje:
```

---

## Casos de prueba

### Prueba 1: Envío de un mensaje

```text
Cliente:
Hola servidor
```

Resultado esperado:

```text
Servidor:
Mensaje recibido correctamente.
```

Cliente:

```text
Mensaje recibido: 2026-09-12 14:30:00
```

---

### Prueba 2: Envío de múltiples mensajes

Enviar varios mensajes consecutivos y verificar que:

* El servidor los reciba.
* Se almacenen correctamente.
* El cliente reciba una respuesta por cada mensaje.

---

### Prueba 3: Verificación de base de datos

Verificar que los mensajes se encuentren almacenados en SQLite.

Ejemplo:

| id | contenido       | fecha_envio         | ip_cliente |
| -- | --------------- | ------------------- | ---------- |
| 1  | Hola            | 2026-09-12 14:30:00 | 127.0.0.1  |
| 2  | Segundo mensaje | 2026-09-12 14:31:00 | 127.0.0.1  |

---

### Prueba 4: Finalización del cliente

Ingresar:

```text
éxito
```

Resultado esperado:

```text
Cliente finalizado correctamente.
```

---

### Prueba 5: Puerto ocupado

Intentar iniciar dos servidores utilizando el puerto `5000`.

Resultado esperado:

```text
Error: el puerto 5000 ya se encuentra en uso.
```

---

# 6. Orden recomendado de desarrollo

Se recomienda seguir el siguiente orden:

```text
1. Crear repositorio
        ↓
2. Crear estructura del proyecto
        ↓
3. Implementar SQLite
        ↓
4. Probar almacenamiento de mensajes
        ↓
5. Implementar socket del servidor
        ↓
6. Probar recepción de un mensaje
        ↓
7. Conectar socket + base de datos
        ↓
8. Implementar respuesta con timestamp
        ↓
9. Implementar cliente
        ↓
10. Permitir múltiples mensajes
        ↓
11. Implementar salida con "éxito"
        ↓
12. Implementar manejo de errores
        ↓
13. Realizar pruebas finales
        ↓
14. Documentar el proyecto
        ↓
15. Subir la solución al repositorio
```

---

# 7. División sugerida de responsabilidades

En caso de realizar el trabajo en grupo, se puede dividir de la siguiente manera.

## Integrante 1: Servidor

Responsabilidades:

* Inicialización del socket.
* Configuración de `localhost:5000`.
* Escucha de conexiones.
* Recepción de mensajes.

---

## Integrante 2: Base de datos

Responsabilidades:

* Configuración de SQLite.
* Creación de la tabla.
* Funciones de almacenamiento.
* Registro de fecha e IP.
* Manejo de errores de base de datos.

---

## Integrante 3: Cliente

Responsabilidades:

* Conexión con el servidor.
* Envío de múltiples mensajes.
* Recepción de respuestas.
* Finalización con `éxito`.

---

## Trabajo conjunto

Responsabilidades:

* Integración de los módulos.
* Manejo general de errores.
* Pruebas.
* Documentación.
* README.
* Revisión final del código.

---

# 8. Buenas prácticas a aplicar

Durante el desarrollo se deberán aplicar las siguientes prácticas:

* Utilizar funciones con una única responsabilidad.
* Evitar código duplicado.
* Separar la lógica de sockets y base de datos.
* Utilizar nombres descriptivos para variables y funciones.
* Comentar las configuraciones importantes.
* Manejar excepciones.
* Cerrar correctamente sockets y conexiones a la base de datos.
* Realizar pruebas después de implementar cada módulo.
* Realizar commits frecuentes y descriptivos.

Ejemplos de commits:

```text
feat: crear configuración inicial del servidor

feat: agregar almacenamiento de mensajes en SQLite

feat: implementar cliente con envío múltiple de mensajes

fix: manejar error cuando el puerto está ocupado

docs: agregar instrucciones de ejecución al README
```

---

# 9. Criterio de finalización

El trabajo estará finalizado cuando se cumplan los siguientes requisitos:

* [ ] El servidor escucha correctamente en `localhost:5000`.
* [ ] El cliente puede conectarse al servidor.
* [ ] El cliente puede enviar múltiples mensajes.
* [ ] El servidor recibe correctamente los mensajes.
* [ ] Cada mensaje se guarda en SQLite.
* [ ] Se registra la fecha y hora del mensaje.
* [ ] Se registra la IP del cliente.
* [ ] El servidor responde con:

```text
Mensaje recibido: <timestamp>
```

* [ ] El cliente muestra cada respuesta recibida.
* [ ] El cliente finaliza al escribir `éxito`.
* [ ] Se manejan errores básicos.
* [ ] El código está modularizado.
* [ ] Las configuraciones importantes están comentadas.
* [ ] Se realizaron pruebas locales.
* [ ] El código está subido a GitHub o Bitbucket.
* [ ] El repositorio contiene un README con instrucciones de ejecución.

---

# 10. Entrega

La entrega final consistirá en:

* El enlace al repositorio de GitHub o Bitbucket.

O, en caso de no utilizar un repositorio:

* Un archivo comprimido `.zip` o `.rar` con la solución completa.

## Contenido mínimo de la entrega

```text
chat-cliente-servidor/
│
├── client/
├── server/
├── database/
├── README.md
├── PLAN_DE_TRABAJO.md
└── código fuente completo
```

---

# 11. Resultado final esperado

El resultado será una aplicación funcional donde un cliente pueda enviar mensajes a un servidor mediante sockets.

El servidor deberá recibir cada mensaje, almacenar su información en una base de datos SQLite y responder al cliente con una confirmación que incluya la fecha y hora de recepción.

Este proyecto permitirá aplicar conceptos de:

* Programación de redes.
* Arquitectura cliente-servidor.
* Sockets TCP/IP.
* Comunicación entre procesos.
* Persistencia de datos.
* SQLite.
* Manejo de errores.
* Modularización.
* Buenas prácticas de programación.
* Control de versiones con Git.
