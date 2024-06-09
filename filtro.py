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

    if len(sys.argv) == 2:
        filtrar_productos(int(sys.argv[1]))
    elif len(sys.argv) >= 3:
        filtrar_productos(int(sys.argv[1]), sys.argv[2])
    else:
        print("Debes pasar los argumentos por línea de comando. Ej: python filtro.py 60000 menor")