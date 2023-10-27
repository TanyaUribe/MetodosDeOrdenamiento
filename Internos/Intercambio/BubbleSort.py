"""
funciona comparando pares de elementos adyacentes y, si están
en el orden incorrecto, los intercambia. Este proceso se repite
hasta que ningún intercambio adicional sea necesario,
lo que garantiza que el arreglo esté completamente ordenado.
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
