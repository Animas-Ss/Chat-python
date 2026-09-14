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
    guardar_mensaje
)



def generar_respuesta():
    # genera la respuesta que recibira el cliente
    fecha = datetime.now().isoformat()
    return f"Hora del servidor: {fecha}"

if __name__ == "__main__":
    crear_tabla()
    servidor = crear_socket()

    asociar_socket(servidor)
    escuchar_conexiones(servidor)
    print("Servidor escuchando en localhost:5000")

    conexion, direccion = aceptar_conexion(servidor)
    print(f"Cliente conectado: {direccion}")

    while True:
        mensaje = recibir_mensaje(conexion)
        print(f"Mensaje recibido: {mensaje}")
     
        if mensaje == "exito":
            break

        guardar_mensaje(mensaje,direccion[0])

        respuesta = generar_respuesta()
        enviar_mensaje(conexion, respuesta)

    conexion.close()
    servidor.close()