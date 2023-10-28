"""
El algoritmo de "Natural Merging" es un método de ordenamiento que trabaja en dos fases: 
la fase de división y la fase de fusión. En la fase de división, se dividen los subarreglos 
ordenados (bloques) en el arreglo original, 
y en la fase de fusión, se fusionan estos bloques en un solo arreglo ordenado.
"""


def natural_merge_sort(arr):
    # Fase de división
    runs = []
    current_run = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            runs.append(current_run)
            current_run = [arr[i]]
        else:
            current_run.append(arr[i])
    runs.append(current_run)

    # Fase de fusión
    while len(runs) > 1:
        merged_runs = []
        i = 0
        while i < len(runs):
            if i < len(runs) - 1:
                merged_run = merge(runs[i], runs[i + 1])
                merged_runs.append(merged_run)
                i += 2
            else:
                merged_runs.append(runs[i])
                i += 1
        runs = merged_runs

    return runs[0]

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Ejemplo de uso
arr = [34, 5, 23, 32, 45, 62, 56, 12, 11]
arr_ordenado = natural_merge_sort(arr)

print("Arreglo ordenado:")
print(arr_ordenado)
