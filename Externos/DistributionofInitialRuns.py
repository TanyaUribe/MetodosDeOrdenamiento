"""
se utiliza en el contexto de la ordenación externa, específicamente 
para la ordenación de conjuntos de datos que no caben completamente en la memoria principal. 
La idea principal de este enfoque es dividir los datos en ejecuciones iniciales más 
pequeñas (runs), ordenar estas ejecuciones en la memoria principal y luego combinarlas 
para obtener el resultado ordenado. Su implementación es compleja.
"""

import heapq

def distribution_of_initial_runs(arr, buffer_size):
    runs = []  # Lista para almacenar las ejecuciones iniciales
    current_run = []  # Lista para almacenar una ejecución temporal
    buffer = []  # Búfer para ordenar elementos

    for element in arr:
        current_run.append(element)

        # Si la ejecución temporal alcanza el tamaño del búfer, ordenar y agregar a las ejecuciones
        if len(current_run) == buffer_size:
            current_run.sort()
            runs.append(current_run)
            current_run = []

    # Ordenar y agregar la ejecución temporal final
    if current_run:
        current_run.sort()
        runs.append(current_run)

    # Combinar las ejecuciones iniciales usando una cola de prioridad (heap)
    result = []
    min_heap = []

    for run in runs:
        for element in run:
            heapq.heappush(min_heap, element)

    while min_heap:
        result.append(heapq.heappop(min_heap))

    return result

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10, 7, 21, 50]
buffer_size = 4  # Tamaño del búfer para cada ejecución inicial
sorted_array = distribution_of_initial_runs(arr, buffer_size)

print("Arreglo ordenado:")
print(sorted_array)
