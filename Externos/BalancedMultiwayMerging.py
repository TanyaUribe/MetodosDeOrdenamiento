"""
Este algoritmo es un método de ordenamiento que se utiliza 
para combinar varios arreglos ya ordenados en uno solo, manteniendo el orden. 
Utiliza una cola de prioridad (heap) para rastrear el elemento más pequeño de cada arreglo
y los combina en el resultado ordenadamente. 
Este algoritmo es útil cuando necesitas combinar múltiples fuentes de datos ya ordenadas en una sola secuencia ordenada.
"""

import heapq

def balanced_multiway_merge(arrays):
    # Usamos una cola de prioridad (heap) para mantener el menor elemento de cada arreglo
    min_heap = []
    result = []

    # Inicializamos el heap con el primer elemento de cada arreglo
    for i, arr in enumerate(arrays):
        if len(arr) > 0:
            min_heap.append((arr[0], i, 0))  # (elemento, índice del arreglo, índice del elemento)

    # Convertimos el heap en un heap mínimo
    heapq.heapify(min_heap)

    while min_heap:
        element, arr_index, element_index = heapq.heappop(min_heap)
        result.append(element)

        # Movemos al siguiente elemento del mismo arreglo (si existe)
        element_index += 1
        if element_index < len(arrays[arr_index]):
            heapq.heappush(min_heap, (arrays[arr_index][element_index], arr_index, element_index))

    return result

# Ejemplo de uso
arrays = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [0, 9, 10],
]

sorted_array = balanced_multiway_merge(arrays)

print("Arreglo ordenado:")
print(sorted_array)
