import json

try:
    with open("dispositivos.json", "r") as archivo:
        dispositivos_data = json.load(archivo)
    print("Informacion de Dispositivos:\n")
    for dispositivo in dispositivos_data["dispositivos"]:
        nombre = dispositivo.get("nombre", "Desconocido")
        ip = dispositivo.get("ip", "Sin ip")
        estado = dispositivo.get("estado", "Desconocido")
        print(f"Dispositivo: {nombre}")
        print(f"IP: {ip}")
        print(f"Estado: {estado}")
        print("-" * 30)

except FileNotFoundError:
    print("El archivo dispositivos.json no fue encontrado")
except json.JSONDecodeError:
    print("Error al leer el archivo JSON")
except KeyError:
    print("El archivo JSON no contiene la clave esperada 'dispositivos'")
