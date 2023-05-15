import sys

class Node:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val

class SegmentTree:
    def __init__(self, a):
        self.a = a.copy()
        self.n = len(a)
        self.tree = [1000000000] * (self.n * 4) # El árbol tendrá n * 4 nodos
        self.build(1, 0, self.n - 1) # Construimos el árbol

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.a[start]
        else:
            mid = (start + end) // 2
            nodeL = node * 2
            nodeR = node * 2 + 1
            self.build(nodeL, start, mid)
            self.build(nodeR, mid + 1, end)
            self.tree[node] = min(self.tree[nodeL], self.tree[nodeR])

    def modify(self, i, val):
        self.modify_util(1, 0, self.n - 1, i, val)

    def modify_util(self, node, start, end, i, val):
        if start == end == i:
            self.tree[node] = val
            self.a[i] = val
        else:
            mid = (start + end) // 2
            nodeL = node * 2
            nodeR = node * 2 + 1
            if i <= mid:
                self.modify_util(nodeL, start, mid, i, val)
            else:
                self.modify_util(nodeR, mid + 1, end, i, val)
            self.tree[node] = min(self.tree[nodeL], self.tree[nodeR])

    def minim(self, i, j):
        return self.minim_util(1, 0, self.n - 1, i, j)

    def minim_util(self, node, start, end, i, j):
        if start > j or end < i:
            return sys.maxsize
        if i <= start and end <= j:
            return self.tree[node]
        mid = (start + end) // 2
        nodeL = node * 2
        nodeR = node * 2 + 1
        return min(self.minim_util(nodeL, start, mid, i, j), self.minim_util(nodeR, mid + 1, end, i, j))


caso = 1
while True:
    nElementos = int(input())
    if nElementos == 0:
        break

    if caso != 1:
        print()

    print(f"Caso {caso}:")
    valores = []
    for i in range(nElementos):
        valores.append(int(input())) # Leemos los valores iniciales
    sg = SegmentTree(valores)
    linea = input().split() # Para leer la línea
    while linea[0] != "END":
        if linea[0] == "S": # Modificar
            i = int(linea[1]) - 1
            val = int(linea[2])
            sg.modify(i, val)
        else: # Mostrar suma
            i = int(linea[1]) - 1
            j = int(linea[2]) - 1
            print(sg.minim(i, j))

        linea = input().split()
    caso += 1
