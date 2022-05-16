# Desafío Buda - Red de Metro

## Introducción

Programa que encuentra la ruta más corta entre dos estaciones de Metro dependiendo del color de la ruta seleccionada (verde, roja o mixta) utilizando una modelación con grafos y una implementación del algoritmo de búsqueda BFS ([**Breadth First Search (BFS)**](https://en.wikipedia.org/wiki/Breadth-first_search))

## Supuestos

1) Una estación de combinación tiene que ser mixta

## Input Red de Metro

La red de metro está modelada utilizando el formato JSON, donde cada estación está almecenada usando su nombre como key, con el valor de su color y una lista de estaciones.

```json
//tests/EasyInput.json
//tests/MediumInput.json
//tests/HardInput.json

{
    "A": {
        "color": "mix",
        "vecinos": ["B"]
    },
    "B": {
        "color": "mix",
        "vecinos": ["A", "C"]
    },
    "C": {
        "color": "mix",
        "vecinos": ["B", "D", "G"]
    }
}
```

En la carpeta de ```img``` se encuentran las representaciones visuales de las redes propuestas.

## Ejecución

El programa se ejecuta corriendo el archivo main.py en conjunto con el archivo que contiene la información de la red, los parámetros dee la estación de inicio, la estación final y el color de la ruta seleccionada.

Los archivos utilizados como input están en la carpeta ```tests``` y estos son: ```EasyInput.json MediumInput.json y HardInput.json```

Los colores de las rutas seleccionables son: "red", "green" o "mix". En caso de que no se especifique se asumirá la ruta mixta.

```python3 main.pt <input_file> <starting_station> <end_station> <colour (Optional)>```

### Ejemplo

Cuando se quiera saber el camino más corto entre dos estaciones A y C pertenecientes a la red EasyInput a través de un color rojo.

```python
python3 main.py tests/EasyInput.json A C red

------

A -> B -> C

```
## Test

Para correr los tests usamos `test_functions.py`


```python3
python3 test_functions.py
```

