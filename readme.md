<a href="https://colab.research.google.com/gist/EniDev911/771dc8a19d02c85de020c80d891f1742/estructuras-de-datos-y-funciones-ii.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Actividad 1

La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar un filtrado por precio. Para ello se solicita generar una función que permita dar la solución al problema. Dada una muestra de los productos que actualmente se encuentran disponibles en la tienda, se solicita implementar una función que permita entregar lo siguiente:

- Un diccionario con los productos que cumplen una cierta condición dado un umbral.
- La función debe permitir mostrar los valores mayor que o menor que un umbral (siempre estricto).
- Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos que se indique lo contrario.


```python
import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(umbral, operacion="mayor"):
    if operacion == "mayor":
        filtro = { k:v for k,v in precios.items() if v > umbral }
        print("Los productos mayores al umbral son:", ", ".join(filtro.keys()))
    elif operacion == "menor":
        filtro = { k:v for k,v in precios.items() if v < umbral }
        print("Los productos menores al umbral son:", ", ".join(filtro.keys()))
    else:
        print("Lo sentimos, no es una operación válida")

if __name__ == "__main__":

  filtrar_productos(
      int(input('Introduce un umbral para el filtro: ')),
      input('Introduce la operación. Ej: menor o mayor: ').strip() or 'mayor'
  )

```

    Introduce un umbral para el filtro: 30000
    Introduce la operación. Ej: menor o mayor: menor
    Los productos menores al umbral son: Teclado, Mouse


## Actividad 2

Otra solución que se encuentra pendiente es la encargada por una empresa de flotas que debe medir mediante telemetría las velocidades de cada una de sus correas transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que, para poder entregar energía a las correas más lentas, es necesario ralentizar las más rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se requiere levantar una alerta de la posición de las correas transportadoras que están sobre el promedio.

Para ello se pide determinar una **funcionalidad que calcucle el promedio** de una lista de velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta con mucha capacidad por lo que se pide no depender de librerías externas.
Listar las posiciones de todas las correas transportadoras que están sobre el promedio.


```python
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,14, 14, 16, 10, 6,
    23, 13, 25, 4, 19,14, 20, 18, 9, 18, 4, 18, 1, 3,
    4, 2,14, 23, 19, 23, 9, 18, 20, 22, 14, 1,10, 5,
    23, 3, 5, 9, 5, 3, 12, 20, 5,11, 10, 18, 10, 14,
    5, 23, 20, 23, 21
]

def calcular_promedio(velocidades):
    return sum(velocidades) / len(velocidades)


if __name__ == "__main__":
    promedio = calcular_promedio(velocidad)
    posiciones = [p for p, e in enumerate(velocidad) if e > promedio]
    print(posiciones)

```

    [0, 2, 3, 6, 8, 9, 10, 13, 15, 17, 18, 19, 20, 22, 24, 29, 30, 31, 32, 34, 35, 36, 37, 41, 48, 52, 54, 56, 57, 58, 59]


## Actividad 3

Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda escolar que tiene esta ONG se está enseñando a programar algunas operaciones avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos operaciones conocidas como el **factorial** y la **productoria**.

Para resolver este programa se solicita lo siguiente:

- Una función que calcule el factorial.
- Una función que calcule la productoria.
- Una función que permita controlar los calculos. Esta función se debe invocar de la siguiente manera:

```python
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)
```


```python
def factorial(numero):
    if numero <= 1:
        return 1

    return numero * factorial(numero - 1)


def productoria(numeros=[]):
    resultado = 1

    for num in numeros:
        resultado *= num

    return resultado

def calcular(**kargs):

    for k, v in kargs.items():
        if k.startswith("fact"):
            print(f"El factorial de {v} es {factorial(v)}")
        elif 'prod_' in k:
            print(f"La productoria de {v} es {productoria(v)}")
        else:
            print("Acción no disponible")

if __name__ == "__main__":

    calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
```

    El factorial de 5 es 120
    La productoria de [4, 6, 7, 4, 3] es 2016
    El factorial de 6 es 720

