"""
Divide el arreglo en intervalos más pequeños y luego aplica el ordenamiento por inserción en 
cada uno de estos intervalos. A medida que el algoritmo avanza, 
reduce gradualmente el tamaño de los intervalos hasta que el arreglo esté completamente ordenado.
"""

def shell_sort(arr):
    n = len(arr)
    intervalo = n // 2

    while intervalo > 0:
        for i in range(intervalo, n):
            temp = arr[i]
            j = i

            while j >= intervalo and arr[j - intervalo] > temp:
                arr[j] = arr[j - intervalo]
                j -= intervalo

            arr[j] = temp

        intervalo //= 2

# Ejemplo de uso
arr = [12, 34, 54, 2, 3]
shell_sort(arr)

print("Arreglo ordenado:")
for i in range(len(arr)):
    print(arr[i])
