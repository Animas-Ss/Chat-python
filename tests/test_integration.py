

import socket
import threading
import sqlite3
from datetime import datetime
import server.server as servidor
import  server.database as database

def test_comunicacion_cliente_servidor(tmp_path, monkeypatch):
    puerto = 5001
    mensaje_prueba = "Mensaje de prueba"

    ruta_db = tmp_path / "test_mensajes.db"
    monkeypatch.setattr(database, "DB_PATH", ruta_db)

    hilo_servidor = threading.Thread(
        target=servidor.iniciar_servidor,
        args=(puerto,),
        daemon=True
    )

    hilo_servidor.start()
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.connect(("localhost",puerto))

    

    cliente.sendall(mensaje_prueba.encode("utf-8"))
    respuesta = cliente.recv(1024).decode("utf-8")
    cliente.sendall("exito".encode("utf-8"))
    cliente.close()

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT contenido, fecha_envio, ip_cliente
        FROM mensajes
    """)
    
    mensaje_guardado = cursor.fetchone()
    contenido, fecha, ip_cliente = mensaje_guardado

    fecha_obtenida = datetime.fromisoformat(fecha)
    conexion.close()
    


    assert respuesta.startswith("Mensaje recibido:")
    assert contenido == mensaje_prueba
    assert fecha_obtenida is not None
    assert ip_cliente == "127.0.0.1"