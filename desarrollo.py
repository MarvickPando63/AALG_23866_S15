class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)

        if raiz_x != raiz_y:
            self.padre[raiz_y] = raiz_x
            return True
        return False


def kruskal(vertices, aristas):
    # Ordenar aristas por peso
    aristas.sort(key=lambda x: x[2])

    uf = UnionFind(vertices)

    arbol_minimo = []
    costo_total = 0

    for origen, destino, peso in aristas:
        if uf.unir(origen, destino):
            arbol_minimo.append((origen, destino, peso))
            costo_total += peso

    return arbol_minimo, costo_total


# Ejemplo de uso
vertices = 4

aristas = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, costo = kruskal(vertices, aristas)

print("Aristas del árbol de expansión mínima:")
for u, v, p in mst:
    print(f"{u} -- {v} : {p}")

print("Costo total:", costo)