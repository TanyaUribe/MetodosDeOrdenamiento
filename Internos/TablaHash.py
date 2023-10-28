"""
Este ejemplo muestra cómo crear una tabla hash simple, insertar elementos
en ella y recuperar valores asociados con claves específicas.
Una tabla hash no ordena elementos, sino que los organiza de manera eficiente para recuperación rápida.
"""


# Clase para una tabla hash simple
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

# Ejemplo de uso
hash_table = HashTable(10)
hash_table.insert(5, "Manzana")
hash_table.insert(15, "Banana")
hash_table.insert(25, "Cereza")

print(hash_table.get(15))  # Output: "Banana"
