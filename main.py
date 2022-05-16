import sys
import json
from entities import ShortestPath
from functions import parser

if __name__ == "__main__":
    try:
        FILE_NAME = str(sys.argv[1])
    except IndexError:
        print("Lo siento, debes agregar un parámetro que indique el \
             nombre del archivo que usaras para poblar la red.")
    try:
        START_STATION = str(sys.argv[2])
    except IndexError:
        print("Lo siento, debes agregar un parámetro que indique la estación de inicio.")
    try:
        END_STATION = str(sys.argv[3])
    except IndexError:
        print("Lo siento, debes agregar un parámetro que indique la estación de término.")
    try:
        EXPRESS_COLOR = str(sys.argv[4])
        if EXPRESS_COLOR not in ['mix', 'red', 'green']:
            print("Lo siento, los colores pueden ser solo red, green o mix \
                 (si lo dejas vacio asumiremos tren mixto)")
            sys.exit()
    except IndexError:
        EXPRESS_COLOR = 'mix'
        print("No especificaste el color, asi que sumiremos que será el tren mixto")
    try:
        with open(f'{FILE_NAME}', "r", encoding='utf-8') as file:
            data = json.load(file)
            graph = parser(data, EXPRESS_COLOR)
            ShortestPath(graph[START_STATION], graph[END_STATION]).bfs()
    except FileNotFoundError:
        print("Lo siento, no se ha encontrado el archivo para poblar la red")
    except KeyError:
        print("Una o ambas de las estaciones ingresadas no se encuentran en el archivo ingresado")
