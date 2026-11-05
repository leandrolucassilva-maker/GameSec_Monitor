import csv
import os

def cargar_partidas(nombre_archivo):
    if not os.path.exists(nombre_archivo):                              #Verificación de archivo
        print("El archivo no existe.")
        return []

    lista_partidas = []

    with open(nombre_archivo, mode="r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:                                             #Conversión de tipos de datos
            partida = {
                "id": int(fila["id_sesion"]),
                "servidor": fila["servidor"].strip(),
                "jugador": fila["jugador_id"].strip(),
                "tipo": fila["tipo_partida"].strip(),
                "ping": int(fila["ping_promedio"]),
                "fps": int(fila["fps_promedio"]),
                "duracion": float(fila["duracion_minutos"]),
                "intentos_fallidos": int(fila["intentos_fallidos"]),
                "reportes_trampa": int(fila["reportes_trampa"])
            }
            lista_partidas.append(partida)

    return lista_partidas