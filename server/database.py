import sqlite3
from pathlib import Path
from datetime import datetime

# Ruta donde se almacenara la base de datos
DB_PATH = Path(__file__).parent.parent / "database" / "mensajes.db"

def conectar_db():
    """
    Crea una conexion con la base de datos SQLite
    """
    return sqlite3.connect(DB_PATH)

def crear_tabla():
    """
    Crea la tabla mensajes si todavia no existe
    """
    try:
        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            );
        """)
        conn.commit()
        print("Tabla creada correctamente")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
        raise

def guardar_mensaje(contenido, ip_client):
    """
    Guardar un mensaje recibido por el servidor
    """
    try:
        
        fecha_envio = datetime.now().isoformat()
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?);
        """,(contenido, fecha_envio, ip_client))
        conn.commit()
        print("Mensaje guardado correctamente")
        conn.close()
    except sqlite3.Error as e:
        print(f"Error al guardar el mensaje: {e}")
        raise