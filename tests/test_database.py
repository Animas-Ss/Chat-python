from server.database import crear_tabla, guardar_mensaje


print("================================")
print("      TEST DE BASE DE DATOS")
print("================================")


print("\n[1] Creando tabla...")
crear_tabla()
print("OK - Tabla creada correctamente.")


print("\n[2] Guardando mensaje...")
guardar_mensaje(
    "Mensaje de prueba",
    "127.0.0.1"
)
print("OK - Mensaje guardado correctamente.")


print("\n================================")
print("       TEST FINALIZADO")
print("================================")