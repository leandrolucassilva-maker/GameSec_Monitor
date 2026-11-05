#MÉTRICAS GLOBALES DE OPERACIÓN
def calcular_promedios_generales(lista_partidas):
    total_partidas = len(lista_partidas)
    suma_ping = 0
    suma_duracion = 0
    cantidad_competitivas = 0

    suma_ping, suma_duracion, cantidad_competitivas = suma_de_estadisticas(suma_ping, suma_duracion, cantidad_competitivas, lista_partidas)
    promedio_ping, promedio_duracion, porcentaje_competitivas = promedios_totales(suma_ping, suma_duracion, cantidad_competitivas, total_partidas)

    return {
        "total": total_partidas,
        "ping_promedio": round(promedio_ping, 2),
        "duracion_promedio": round(promedio_duracion, 2),
        "porcentaje_competitivas": round(porcentaje_competitivas, 2)
    }

def suma_de_estadisticas(ping, duracion, competitivas, lista_partidas):                               #Totales ping, duración y competitivas
    for partida in lista_partidas:
        ping = ping + partida["ping"]
        duracion = duracion + partida["duracion"]
        if partida["tipo"] == "Competitiva" or partida["tipo"] == "Torneo":
            competitivas = competitivas + 1
    return ping, duracion, competitivas
def promedios_totales(ping, duracion, partidas, jugadores):             #Promedios ping, duración y competitivas
    promedio_ping = ping/jugadores
    promedio_duracion = duracion/jugadores
    porcentaje_competitivas = (partidas/jugadores) * 100
    return promedio_ping, promedio_duracion, porcentaje_competitivas


#AGRUPAMIENTO POR REGIÓN DEL SERVIDOR
def analizar_servidores(lista_partidas):
    datos_servidores = {}
    resultado_final = {}

    for partida in lista_partidas:                                      #Suma los datos de cada región
        nombre_servidor = partida["servidor"]
        if nombre_servidor not in datos_servidores:                     #Si no existe la región en el dict, la crea
            datos_servidores[nombre_servidor] = {
                "cantidad": 0,
                "suma_ping": 0,
                "suma_fps": 0
            }
        datos_servidores[nombre_servidor]["cantidad"] += 1
        datos_servidores[nombre_servidor]["suma_ping"] += partida["ping"]
        datos_servidores[nombre_servidor]["suma_fps"] += partida["fps"]
    resultado_final = promedios_regiones(datos_servidores, resultado_final)

    return resultado_final

def promedios_regiones(datos_servidores, final):                        #Promedia los datos de cada región
    for servidor, datos in datos_servidores.items():
        cant = datos["cantidad"]
        final[servidor] = {
            "cantidad_partidas": cant,
            "ping_promedio": round(datos["suma_ping"] / cant, 2),
            "fps_promedio": round(datos["suma_fps"] / cant, 2)
        }
    return final


#MOTOR DE CLASIFICACIÓN DE INCIDENTES
def buscar_jugadores_sospechosos(lista_partidas):
    conteo_estados = {"Normal": 0, "Sospechoso": 0, "Critico": 0}
    lista_criticos = []

    for partida in lista_partidas:
        reportes = partida["reportes_trampa"]
        intentos = partida["intentos_fallidos"]

        if reportes >= 3 or intentos >= 4:                              #Casos críticos
            conteo_estados["Critico"] += 1
            lista_criticos.append({
                "id": partida["id"],
                "jugador": partida["jugador"],
                "servidor": partida["servidor"],
                "reportes": reportes,
                "intentos": intentos
            })
        elif reportes == 2 or intentos == 2:                            #Casos sospechosos
            conteo_estados["Sospechoso"] += 1
        else:
            conteo_estados["Normal"] += 1                               #Casos normales

    return conteo_estados, lista_criticos