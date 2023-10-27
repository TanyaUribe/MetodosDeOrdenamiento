"""
Funciona recorriendo el arreglo de izquierda a derecha, tomando un elemento
a la vez e insertandolo en su lugar correcto dentro de la porcion ya
ordenada.
El resultado es un arreglo ordemado de menor a mayor.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual que se va a insertar en su lugar correcto
        j = i - 1  # Índice del elemento anterior al elemento actual

        # Mover los elementos mayores que key hacia la derecha
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insertar key en su lugar correcto
        arr[j + 1] = key

# Ejemplo de uso
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
