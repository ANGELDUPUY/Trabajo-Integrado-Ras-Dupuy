import time
import random
import unicodedata

# Trabajo Integrador - Programación I
# Título: Comparador de Algoritmos de Búsqueda y Ordenamiento en Python
# Integrantes: Agustin Federico Ras, Manuel Angel Dupuy
# Fecha de entrega: 07/06/2025

# Algoritmos de ordenamiento

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current[key] < arr[j][key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][key]
    left = [x for x in arr if x[key] < pivot]
    middle = [x for x in arr if x[key] == pivot]
    right = [x for x in arr if x[key] > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] < right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Algoritmos de búsqueda

def busqueda_lineal(arr, key, target):
    for i in range(len(arr)):
        if normalize_value(arr[i][key]) == normalize_value(target):
            return i
    return -1

def busqueda_binaria(arr, key, target):
    target_norm = normalize_value(target)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        current = normalize_value(arr[mid][key])
        if current == target_norm:
            return mid
        elif current < target_norm:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Función para medir el tiempo de ejecución
def medir_tiempo(algoritmo, arr, key, target=None):
    inicio = time.time()
    if target is not None:
        resultado = algoritmo(arr, key, target)
    else:
        resultado = algoritmo(arr.copy(), key)
    fin = time.time()
    return resultado, fin - inicio

# Normalizador de texto
def normalize_value(value):
    if isinstance(value, str):
        value = unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode('utf-8').lower()
    return value

# Generador de nombres únicos

def generar_nombres_unicos(cantidad):
    nombres = ["Lucia", "Mateo", "Valentina", "Santiago", "Martina", "Benjamin", "Camila", "Thiago", "Julieta", "Lautaro", "Agustin", "Manuel"]
    apellidos = ["Gomez", "Fernandez", "Lopez", "Martinez", "Perez", "Sanchez", "Romero", "Diaz", "Alvarez", "Torres", "Ras", "Dupuy"]
    combinaciones = [f"{n} {a}" for n in nombres for a in apellidos]
    random.shuffle(combinaciones)
    return combinaciones[:cantidad]

# Interfaz por consola
def main():
    tamanio = int(input("\nCantidad de estudiantes a generar (max. 100): "))
    if tamanio > 100:
        print("Demasiados estudiantes. Maximo permitido: 100.")
        return

    nombres_unicos = generar_nombres_unicos(tamanio)
    promedios_unicos = random.sample(range(1, 101), tamanio)

    estudiantes = [
        {"nombre": nombre, "promedio": promedio}
        for nombre, promedio in zip(nombres_unicos, promedios_unicos)
    ]

    print(f"\nLista generada ({tamanio} estudiantes):")
    for e in estudiantes:
        print(f"{e['nombre']}: {e['promedio']}")

    print("\nOrdenar por:")
    print("1. Nombre")
    print("2. Promedio")
    clave = input("Elige una opcion (1-2): ")
    clave_orden = "nombre" if clave == "1" else "promedio"

    print("\nAlgoritmos de Ordenamiento:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    print("4. Merge Sort")
    opcion = input("Elige una opcion (1-4): ")

    algoritmos = {
        "1": bubble_sort,
        "2": insertion_sort,
        "3": quick_sort,
        "4": merge_sort
    }

    if opcion not in algoritmos:
        print("Opcion invalida")
        return

    print("\nOrdenando estudiantes...")
    estudiantes_ordenados, tiempo_ordenamiento = medir_tiempo(algoritmos[opcion], estudiantes, clave_orden)
    print(f"Tiempo de ordenamiento: {tiempo_ordenamiento:.6f} segundos")
    print("\nLista ordenada:")
    for e in estudiantes_ordenados:
        print(f"{e['nombre']}: {e['promedio']}")

    print("\nBuscar estudiante por:")
    print("1. Nombre")
    print("2. Promedio")
    opcion_busqueda = input("Elige una opcion (1-2): ")
    clave_busqueda = "nombre" if opcion_busqueda == "1" else "promedio"

    if clave_busqueda == "nombre":
        valor = input("Nombre completo a buscar: ")
    else:
        valor = int(input("Promedio a buscar (1-100): "))

    print("\nMetodo de busqueda:")
    print("1. Lineal")
    print("2. Binaria")
    metodo = input("Elige una opcion (1-2): ")

    if metodo == "1":
        index, tiempo_busqueda = medir_tiempo(busqueda_lineal, estudiantes_ordenados, clave_busqueda, valor)
    else:
        index, tiempo_busqueda = medir_tiempo(busqueda_binaria, estudiantes_ordenados, clave_busqueda, valor)

    print(f"Tiempo de busqueda: {tiempo_busqueda:.6f} segundos")

    if index != -1:
        e = estudiantes_ordenados[index]
        print(f"\nEstudiante encontrado: {e['nombre']}, promedio: {e['promedio']}")
    else:
        print("\nEstudiante no encontrado.")

if __name__ == "__main__":
    main()