"""
El algoritmo de HeapSort utiliza un heap binario (en este caso, un max-heap) para ordenar
un arreglo. Primero, construye un max-heap a partir del arreglo dado y luego extrae los 
elementos uno por uno, lo que garantiza que los elementos se coloquen en orden ascendente 
en el arreglo final. El resultado es un arreglo ordenado de menor a mayor.

Un heap es una estructura de datos de árbol especializada que satisface una propiedad 
fundamental. En particular, se utiliza comúnmente en algoritmos de ordenamiento y en problemas de prioridad. 
"""

def heapify(arr, n, i):
    # Inicializamos el índice más grande como la raíz
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Comparamos con el hijo izquierdo
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Comparamos con el hijo derecho
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el índice más grande no es la raíz, intercambiamos y llamamos a heapify recursivamente
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el elemento máximo con el último elemento
        heapify(arr, i, 0)

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)

print("Arreglo ordenado:")
for elemento in arr:
    print(elemento)

