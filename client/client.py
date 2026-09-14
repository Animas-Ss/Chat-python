import socket

def crear_socket():
    #Crea y devuelve un socket TCP para el cliente.
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar_servidor(servidor):
    #Conecta el socket del cliente al servidor.
    servidor.connect(("localhost", 5000))

def enviar_mensaje(cliente, mensaje):
    #Envia un mensaje al servidor
    datos = mensaje.encode("utf-8")
    cliente.sendall(datos)

def recibir_respuesta(cliente):
    #Recibe la respuesta del servidor
    return cliente.recv(1024).decode("utf-8")


if __name__ == "__main__":
    cliente = crear_socket()
    conectar_servidor(cliente)
    print("Cliente conectado al servidor")

    while True:
        mensaje = input("Ingrese su mensaje: ")
        if mensaje == "exito":
            enviar_mensaje(cliente, mensaje)
            break
        
        enviar_mensaje(cliente, mensaje)
        respuesta = recibir_respuesta(cliente)
        print(f"Respuesta del servidor: {respuesta}")
    
    cliente.close()

