from queue import Queue
import numpy as np

class Grafo:
    def __init__(self, palavras, vertices):
        self.vertices = vertices
        self.palavras = palavras
        self.lista_adjacencia = {v: [] for v in vertices}

    def __criar_grafo(self, palavras):
        for palavra in palavras:
            for i in range(len(palavra)):
                letra = palavra[i]
                if letra not in self.vertices:
                    self.vertices[letra] = {}
                if i > 0:
                    letra_anterior = palavra[i-1]
                    if letra_anterior not in self.vertices[letra]:
                        self.vertices[letra][letra_anterior] = {}
                    if i == len(palavra)-1:
                        self.vertices[letra][letra_anterior][None] = palavra
                elif i == 0:
                    if None not in self.vertices[letra]:
                        self.vertices[letra][None] = {}
                    if len(palavra) == 1:
                        self.vertices[letra][None][None] = palavra

    def buscar_palavra(self, matriz, palavra, i, j):
        if len(palavra) == 0:
            return True
        if i < 0 or j < 0 or i >= len(matriz) or j >= len(matriz[i]):
            return False
        if matriz[i][j] != palavra[0]:
            return False
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (1, 2), (2, 1), (2, -1),
                       (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            if self.buscar_palavra(matriz, palavra[1:], i + di, j + dj):
                return True
        return False

    def buscar_palavras(self, matriz):
        palavras_encontradas = set()
        for palavra in self.palavras:
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if self.buscar_palavra(matriz, palavra, i, j):
                        palavras_encontradas.add(palavra)
        return list(palavras_encontradas)

    def adicionar_arestas(self, u, v):
        self.lista_adjacencia[u].append(v)
        self.lista_adjacencia[v].append(u)

    def bfs(self, origem):
        visitados = {v: False for v in self.vertices}
        fila = Queue()
        visitados[origem] = True
        fila.put(origem)

        while not fila.empty():
            vertice_atual = fila.get()
            print(vertice_atual)

            for vizinho in self.lista_adjacencia[vertice_atual]:
                if not visitados[vizinho]:
                    visitados[vizinho] = True
                    fila.put(vizinho)

    def __dfs(self, matriz, i, j, vertice_atual, visitados, palavras_encontradas):
        visitados.add((i, j))
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]:
            novo_i, novo_j = i + di, j + dj
            if 0 <= novo_i < len(matriz) and 0 <= novo_j < len(matriz[0]) and (novo_i, novo_j) not in visitados:
                nova_letra = matriz[novo_i][novo_j]
                if nova_letra in vertice_atual:
                    proximo_vertice = vertice_atual[nova_letra]
                    for final in proximo_vertice.get(None, {}):
                        palavras_encontradas.add(final)
                    self.__dfs(matriz, novo_i, novo_j, nova_letra, proximo_vertice, visitados, palavras_encontradas)
        visitados.remove((i, j))

def read_letter_matrix_from_file(matrix):
    with open(matrix, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = line.strip().split()
            matrix.append(row)
    return matrix



palavras = ['casa', 'carro', 'cadeira', 'computador']
# matriz = [
#     ['c', 'a', 'r', 'r', 'o'],
#     ['o', 's', 'a', 'c', 'e'],
#     ['m', 'o', 'm', 'p', 'a'],
#     ['p', 'r', 'a', 'r', 'r'],
#     ['u', 'c', 'a', 'd', 'e']
# ]

vertices = [(i, i) for i in range(10) for j in range(10)]
grafo = Grafo(palavras, vertices)
matrix = read_letter_matrix_from_file('matrix.txt')
print(matrix)
palavras_encontradas = grafo.buscar_palavras(matrix)
print(palavras_encontradas)