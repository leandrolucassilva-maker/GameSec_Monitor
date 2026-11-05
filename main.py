from carga import cargar_partidas
from procesamiento import (
    calcular_promedios_generales,
    analizar_servidores,
    buscar_jugadores_sospechosos
)

def guardar_reporte_en_texto(lista_partidas):                           #Reporte gamesec.txt
    generales = calcular_promedios_generales(lista_partidas)
    servidores = analizar_servidores(lista_partidas)
    conteo, lista_criticos = buscar_jugadores_sospechosos(lista_partidas)

    with open("reporte_gamesec.txt", "w", encoding="utf-8") as archivo:
        archivo.write("==== REPORTE DE AUDITORIA Y TELEMETRÍA ====\n\n")
        
        archivo.write("1. RESUMEN GLOBAL OPERATIVO\n")
        archivo.write(f"Total de sesiones: {generales['total']}\n")
        archivo.write(f"Ping promedio: {generales['ping_promedio']} ms\n")
        archivo.write(f"Duración media de partida: {generales['duracion_promedio']} min\n")
        archivo.write(f"Porcentaje de partidas de alta competencia: {generales['porcentaje_competitivas']}%\n\n")

        archivo.write("2. RENDIMIENTO REGIONAL POR SERVIDOR\n")
        for srv, info in servidores.items():
            archivo.write(f"Servidor: {srv} | Partidas: {info['cantidad_partidas']} | Ping: {info['ping_promedio']} ms | FPS: {info['fps_promedio']}\n")

        archivo.write("\n3. AUDITORÍA DE SEGURIDAD E INCIDENTES\n")
        archivo.write("Distribución de estados de seguridad:\n")
        archivo.write(f"[*]    Partidas Normales: {conteo['Normal']}\n")
        archivo.write(f"[*]    Partidas Sospechosas: {conteo['Sospechoso']}\n")
        archivo.write(f"[*]    Partidas Criticas: {conteo['Critico']}\n\n")
        
        archivo.write("Detalle de partidas críticas:\n")
        for critico in lista_criticos:
            archivo.write(f"[!]    Sesión #{critico['id']} | Jugador: {critico['jugador']} | Servidor: {critico['servidor']} (Reportes: {critico['reportes']}, Intentos fallidos: {critico['intentos']})\n")

    print("\n[+]    Reporte guardado con exito en 'reporte_gamesec.txt'")


def main():
    lista_partidas = []
    csv_cargado = False

    while True:
        print("\n====    GAMESEC MONITOR - Panel de Control    ====")
        print("[1] Cargar archivo CSV")
        print("[2] Ver promedios generales")
        print("[3] Ver datos por servidor")
        print("[4] Ver partidas sospechosas / criticas")
        print("[5] Guardar reporte en archivo de texto")
        print("[6] Salir")

        opcion = input("Escoja una opcion: ").strip()

        if opcion == "1":
            lista_partidas = carga_de_csv(lista_partidas)
            if len(lista_partidas) > 0:
                print(f"\n[+] Se cargaron {len(lista_partidas)} partidas correctamente.")
            else:
                print("\n[-] No se pudieron cargar los datos.")
            csv_cargado = True

        elif opcion == "2":
            if csv_cargado == False:
                print("\n[?] Procediendo a cargar los datos.")
                lista_partidas = carga_de_csv(lista_partidas)
            datos = calcular_promedios_generales(lista_partidas)
            print("\n--- PROMEDIOS GENERALES ---")
            print("Total partidas: ", datos["total"])
            print("Ping promedio: ", datos["ping_promedio"], "ms")
            print("Duracion promedio: ", datos["duracion_promedio"], "min")
            print("Partidas competitivas: ", datos["porcentaje_competitivas"], "%")

        elif opcion == "3":
            if csv_cargado == False:
                print("\n[?] Procediendo a cargar los datos.")
                lista_partidas = carga_de_csv(lista_partidas)
            datos_srv = analizar_servidores(lista_partidas)
            print("\n--- DATOS POR SERVIDOR ---")
            for srv, info in datos_srv.items():
                print(f"Servidor: {srv} | Partidas: {info['cantidad_partidas']} | Ping: {info['ping_promedio']} ms | FPS: {info['fps_promedio']}")

        elif opcion == "4":
            if csv_cargado == False:
                print("\n[?] Procediendo a cargar los datos.")
                lista_partidas = carga_de_csv(lista_partidas)
            conteo, criticos = buscar_jugadores_sospechosos(lista_partidas)
            print("\n--- AUDITORÍA DE SEGURIDAD ---")
            print(f"Normales: {conteo['Normal']} | Sospechosos: {conteo['Sospechoso']} | Criticos: {conteo['Critico']}")
            print("\nJugadores Criticos:")
            for c in criticos:
                print(f"• Partida #{c['id']} | Jugador: {c['jugador']} | Servidor: {c['servidor']}")

        elif opcion == "5":
            if csv_cargado == False:
                print("\n[?] Procediendo a cargar los datos.")
                lista_partidas = carga_de_csv(lista_partidas)
            guardar_reporte_en_texto(lista_partidas)

        elif opcion == "6":
            print("\nFin del programa")
            break
def carga_de_csv(partidas):
    partidas = cargar_partidas("gamesec_logs.csv")
    return partidas


if __name__ == "__main__":
    main()
