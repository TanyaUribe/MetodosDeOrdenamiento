"""
es un algoritmo de ordenamiento no comparativo que ordena los elementos tratando cada dígito 
del número como una clave de ordenación. En el código de ejemplo, se utiliza el algoritmo de Counting
Sort como subrutina para ordenar los elementos basados en sus dígitos en cada posición (unidades, decenas, centenas, etc.). 
El proceso se repite para cada posición de dígito hasta que el arreglo esté completamente ordenado. 
"""

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contar la ocurrencia de cada dígito en la posición 'exp'
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calcular las posiciones finales de los dígitos en la salida
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_element = max(arr)
    exp = 1

    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)

print("Arreglo ordenado:")
for elemento in arr:
    print(elemento)
