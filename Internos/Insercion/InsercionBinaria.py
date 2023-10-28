"""
El algoritmo de inserción binaria es un método de ordenamiento que, a medida 
que se recorre un arreglo de elementos, inserta cada elemento 
en la posición correcta dentro de la parte del arreglo que ya está ordenada,
utilizando una búsqueda binaria para encontrar la ubicación de inserción.
"""

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        # Guardar el valor actual que se va a insertar
        valor_actual = arr[i]
        izquierda = 0
        derecha = i - 1

        # Usar búsqueda binaria para encontrar la posición de inserción
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if arr[medio] > valor_actual:
                derecha = medio - 1
            else:
                izquierda = medio + 1

        # Desplazar elementos para hacer espacio para el valor actual
        for j in range(i - 1, izquierda - 1, -1):
            arr[j + 1] = arr[j]

        # Insertar el valor actual en la posición correcta
        arr[izquierda] = valor_actual

# Ejemplo de uso
arr = [12, 11, 13, 5, 6]
binary_insertion_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
