import socket

def crear_socket():
    #Crea y devuelve un socket TCP para el servidor.
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def asociar_socket(servidor):
    #Asocia el socket a la dirección IP y puerto especificados.
    servidor.bind(("localhost", 5000))

def escuchar_conexiones(servidor):
    #El servidor empieza a escuchar conexiones entrantes.
    servidor.listen(5)
    
def aceptar_conexion(servidor):
    #Espera y acepta una conexion entrante
    conexion, direccion = servidor.accept()
    return conexion, direccion

def recibir_mensaje(conexion):
    #Recibe un mensaje del socket
    return conexion.recv(1024).decode('utf-8')

def enviar_mensaje(conexion, mensaje):
    #Envia un mensaje al socket
    datos = mensaje.encode('utf-8')
    conexion.sendall(datos)


