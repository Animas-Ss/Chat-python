import sqlite3
from datetime import datetime

from server.socket_manager import (
    crear_socket,
    asociar_socket,
    escuchar_conexiones,
    aceptar_conexion,
    recibir_mensaje,
    enviar_mensaje,
)

from server.database import (
    crear_tabla,
    guardar_mensaje,
)



def generar_respuesta():
    # genera la respuesta que recibira el cliente
    fecha = datetime.now().isoformat()
    return f"Mensaje recibido: {fecha}"

def iniciar_servidor(puerto=5000):
    try:
        crear_tabla()
    except sqlite3.Error as e:
        print(f"No se pudo iniciar el servidor por un error de base de datos: {e}")
        return

    servidor = crear_socket()

    try:
        asociar_socket(servidor, puerto)
    except OSError as e:
        print(f"Error al iniciar el servidor: {e}")
        servidor.close()
        return

    escuchar_conexiones(servidor)
    print(f"Servidor escuchando en localhost:{puerto}")

    conexion, direccion = aceptar_conexion(servidor)
    print(f"Cliente conectado: {direccion}")

    while True:
        mensaje = recibir_mensaje(conexion)
        print(f"Mensaje recibido: {mensaje}")
     
        if mensaje == "exito" or mensaje == "éxito":
            break

        try:
            guardar_mensaje(mensaje, direccion[0])
        except sqlite3.Error as e:
            print(f"Error en base de datos: {e}")
            break

        respuesta = generar_respuesta()
        enviar_mensaje(conexion, respuesta)

    conexion.close()
    servidor.close()


if __name__ == "__main__":
    iniciar_servidor()