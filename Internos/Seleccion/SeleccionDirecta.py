"""
Funciona encontrando repetidamente el elemento mínimo en la porción
no ordenada del arreglo y colocándolo al principio.
El proceso continúa hasta que todo el arreglo esté ordenado.
"""

def direct_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # Encuentra el índice del elemento mínimo en la porción no ordenada del arreglo
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Intercambia el elemento actual con el mínimo encontrado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
direct_selection_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
