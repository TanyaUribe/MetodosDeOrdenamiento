"""
Los algoritmos de ordenamiento basados en árbolesa menudo se refieren a estructuras
de datos como los árboles binarios de búsqueda (BST) o los árboles AVL. Estos árboles
se utilizan para almacenar elementos y mantenerlos automáticamente ordenados.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root, result):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.value)
        inorder_traversal(root.right, result)

def tree_sort(arr):
    root = None
    for item in arr:
        root = insert(root, item)
    result = []
    inorder_traversal(root, result)
    return result

# Ejemplo de uso
arr = [12, 4, 5, 6, 13, 9, 2]
sorted_arr = tree_sort(arr)

print("Arreglo ordenado:")
for item in sorted_arr:
    print(item)
