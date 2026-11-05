GameSec Monitor - Trabajo Practico Integrador

Este es el proyecto que armamos para el TP de Programacion 1. Se trata de una aplicacion de consola en Python para analizar datos de rendimiento y ciberseguridad de un juego online, usando la informacion que viene en un archivo CSV.

Integrantes del Grupo

Alumno 1: Leandro Lucas Silva
Alumno 2: Santiago Lima

Introducción

El programa lee el archivo gamesec_logs.csv y procesa los datos fila por fila para resolver cuatro cosas concretas:
-Promedios Generales: Nos da los numeros globales de la operacion, como el ping promedio, el tiempo de duracion de las partidas y el porcentaje de partidas que se jugaron en modos competitivos.
-Rendimiento por Servidor: Separa las partidas segun la region (Buenos Aires, Frankfurt, Virginia o San Pablo) para mostrarnos la latencia y los FPS promedio que tiene cada lugar.
-Auditoria de Seguridad: Aplica reglas simples para buscar jugadores con muchas denuncias por trampa o con varios reintentos fallidos de contraseña, dividiendo las partidas en Normales, Sospechosas o Criticas.
-Generacion de Reportes: Toma todos estos analisis y los guarda de forma prolija en un archivo de texto llamado reporte_gamesec.txt.

Como organizamos el codigo
Para una resolución ordenada y modular, dividimos el programa en tres archivos Python:
-carga.py: Se encarga unicamente de la lectura del archivo CSV. Revisa que el archivo exista, quita espacios molestos y convierte los datos que vienen como texto a numeros enteros o decimales.
-procesamiento.py: Es la parte donde se hacen los calculos. Aca estan las funciones que sacan los promedios globales, los promedios por region y las condiciones para filtrar a los usuarios sospechosos.
-main.py: Es el archivo principal. Muestra el menu en pantalla para interactuar con el usuario y se asegura de cargar los datos automaticamente en caso de que alguien intente pedir un analisis antes de haber cargado el CSV.

Ejecución del programa
Por cli, nos dirigimos a la ruta donde está el proyecto, ejemplo cd C:\TP1-Taller_Prog_1

Correr el programa con Python:
py main.py

Elegir una opcion del menu (del 1 al 6):
Opcion 1: Carga los datos del archivo CSV.
Opcion 2: Muestra en pantalla los promedios generales.
Opcion 3: Muestra las metricas por servidor.
Opcion 4: Muestra los casos sospechosos y criticos detectados.
Opcion 5: Exporta el informe a reporte_gamesec.txt.
Opcion 6: Sale del programa.

Nota de diseño

Toda la comunicacion entre funciones se hace mediante parametros y valores de retorno(return). De esta forma evitamos usar variables globales y garantizamos que cada modulo haga solo el trabajo que le corresponde.
