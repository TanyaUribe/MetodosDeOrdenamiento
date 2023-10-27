"""
 Funciona de manera similar al algoritmo de inserción regular,
 pero en lugar de usar un índice para mover elementos mayores hacia la derecha,
 utiliza el valor del elemento que se está insertando.
"""

def direct_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual que se va a insertar en su lugar correcto
        j = i - 1

        # Mover los elementos mayores que key hacia la derecha
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insertar key en su lugar correcto
        arr[j + 1] = key

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
direct_insertion_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
