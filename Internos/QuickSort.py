"""
El algoritmo de QuickSort es un método de ordenamiento de tipo "divide y vencerás" que 
elige un elemento como pivote y divide el arreglo en dos subarreglos: uno con elementos 
menores que el pivote y otro con elementos mayores. 
Luego, se repite el proceso en los subarreglos hasta que todo el arreglo esté ordenado.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]
        mayores = [x for x in arr[1:] if x > pivot]
        return quick_sort(menores) + [pivot] + quick_sort(mayores)

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
arr_ordenado = quick_sort(arr)

print("Arreglo ordenado:")
for elemento in arr_ordenado:
    print(elemento)
