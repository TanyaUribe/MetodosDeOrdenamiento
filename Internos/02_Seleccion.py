"""
El algoritmo de ordenamiento por selección funciona seleccionando
repetidamente el elemento mínimo del arreglo no ordenado y colocándolo
al principio.
El proceso continúa hasta que todo el arreglo esté ordenado.
"""

def selection_sort(arr):
    n = len(arr)

    # Recorremos el arreglo
    for i in range(n):
        # Encontramos el índice del mínimo elemento en el resto del arreglo
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambiamos el elemento actual con el mínimo encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
