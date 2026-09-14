import sqlite3
import pytest
from datetime import datetime
import server.database as database

@pytest.fixture
def db_path(tmp_path, monkeypatch):
    db_file = tmp_path / "test_mensajes.db"
    monkeypatch.setattr(database, "DB_PATH", db_file)
    return db_file

def test_create_table(db_path):
    database.crear_tabla()
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("PRAGMA table_info(mensajes)")
    columnas = {fila[1] for fila in cursor.fetchall()}
    conexion.close()
    assert columnas == {"id","contenido","fecha_envio","ip_cliente"}

def test_save_message(db_path):
    database.crear_tabla()
    database.guardar_mensaje("Hola servidor", "127.0.0.1")
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT contenido, ip_cliente
        FROM mensajes
        """)
    mensaje =cursor.fetchone()
    conexion.close()
    assert mensaje == ("Hola servidor", "127.0.0.1")

def test_save_message_date(db_path):
    database.crear_tabla()
    database.guardar_mensaje("mensaje con fecha", "127.0.0.1")
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT fecha_envio
        FROM mensajes
    """)
    response = cursor.fetchone()
    conexion.close()
    assert response is not None
    fecha = response[0]
    fecha_obtenida = datetime.fromisoformat(fecha)
    assert fecha_obtenida is not None

def test_database_error(monkeypatch, tmp_path):
    path_invalido = tmp_path / "carpeta_invalida"
    path_invalido.mkdir()
    monkeypatch.setattr(database, "DB_PATH", path_invalido)
    with pytest.raises(sqlite3.Error):
        database.conectar_db()

def test_save_message_error(monkeypatch):
    def conexion_fallida():
        raise sqlite3.Error("Error de conexion simulado")
    monkeypatch.setattr(database,"conectar_db",conexion_fallida)
    with pytest.raises(sqlite3.Error):
        database.guardar_mensaje("mensaje de prueba","127.0.0.1")