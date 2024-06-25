# import sys
# from collections import defaultdict
# from queue import Queue
# from typing import List
#
# import pygame
# import numpy as np
#
# from caca_palavras import grafo
#
#
# class Grafo:
#     def __init__(self, palavras, vertices):
#         self.vertices = defaultdict(set)
#         self.palavras = palavras
#         self.criar_grafo(palavras, vertices)
#
#     def criar_grafo(self, palavras):
#         for palavra in palavras:
#             for letra in palavra:
#                 if letra not in self.vertices:
#                     self.vertices[letra] = {}
#                 self.vertices[letra].setdefault(palavra, {})
#                 if palavra.index(letra) > 0:
#                     letra_anterior = palavra[letra - 1]
#                     self.vertices[letra].setdefault(letra_anterior, {})
#                     if letra == len(palavra) - 1:
#                         self.vertices[letra][letra_anterior][None] = palavra
#                 elif letra == 0:
#                     self.vertices[letra].setdefault(None, {})
#                     if len(palavra) == 1:
#                         self.vertices[letra][None][None] = palavra
#
#
# def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#     result = []
#     rows = len(board)
#     cols = len(board[0])
#
#     # making board a global variable
#     self.board = board
#
#     for word in words:
#         for i in range(rows):
#             for j in range(cols):
#                 if self.board[i][j] == word[0]:
#
#                     # making a function findwords to
#                     # find words along with their
#                     # location which inputs the board
#                     # and list of words
#                     if self.dfs(i, j, word[1:], [[False] * cols for _ in range(rows)]):
#                         result.append(f"{word}->{{{i},{j}}}")
#
#     return result
#
#     # depth first search for the string, with the
#     # coordinates and a visited array to take care that we
#     # do not overlap the places visited already
#
#
# def dfs(self, x: int, y: int, s: str, vis: List[List[bool]]) -> bool:
#     # if string length becomes 0 means string is found
#     if not s:
#         return True
#
#     vis[x][y] = True
#
#     # making a solution boolean to see if we can
#     # perform depth search to find answer
#     sol = False
#
#     # making possible moves
#     for move in self.mover:
#         currX = move[0] + x
#         currY = move[1] + y
#
#         # checking for out of bound areas
#         if 0 <= currX < len(self.board) and 0 <= currY < len(self.board[0]):
#
#             # checking for similarity in the first
#             # letter and the visited array
#             if self.board[currX][currY] == s[0] and not vis[currX][currY]:
#                 if self.dfs(currX, currY, s[1:], vis):
#                     # removing the first letter
#                     # from the string
#                     sol = True
#
#     return sol
#
# def main():
#     # Lê a lista de palavras
#     with open('lista_palavras.txt') as f:
#         palavras = f.read().splitlines()
#
#     # Lê a matriz de letras
#     matriz_letras = np.loadtxt('matriz_letras.txt', dtype=str)
#
#     # Encontra as palavras na matriz de letras
#     palavras_encontradas = encontrar_palavras(palavras, matriz_letras, grafo)
#
#     # Inicializa o Pygame
#     pygame.init()
#
#     # Configura a janela do Pygame
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Caça-palavras")
#
#     # Define a fonte utilizada para desenhar as palavras encontradas
#     font = pygame.font.SysFont("Arial", 20)
#
#     # Desenha as palavras encontradas na tela
#     y = 50
#     for palavra in palavras_encontradas:
#         # Cria um texto a partir da palavra encontrada
#         text = font.render(palavra, True, (0, 255, 0))
#
#         # Define a posição do texto na tela
#         x = 50
#         y += 30
#
#         # Desenha o texto na tela
#         screen.blit(text, (x, y))
#
#     # Atualiza a tela
#     pygame.display.update()
#
#     # Espera até o usuário fechar a janela do Pygame
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
# if __name__ == '__main__':
#     main()
#
# import sys
# from typing import List
#
# import numpy as np
# import pygame
#
#
# class Solution:
#     def __init__(self):
#         # making the possible moves in movers array
#         self.mover = [
#             [1, 0], [0, 1], [-1, 0], [0, -1],
#             [1, 1], [-1, -1], [1, -1], [-1, 1]
#         ]
#
#     # making a function findwords to find words along with
#     # their location which inputs the board and list of
#     # words
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         result = []
#         rows = len(board)
#         cols = len(board[0])
#
#         # making board a global variable
#         self.board = board
#
#         for word in words:
#             for i in range(rows):
#                 for j in range(cols):
#                     if self.board[i][j] == word[0]:
#
#                         # making a function findwords to
#                         # find words along with their
#                         # location which inputs the board
#                         # and list of words
#                         if self.dfs(i, j, word[1:], [[False] * cols for _ in range(rows)]):
#                             result.append(f"{word}->{{{i},{j}}}")
#
#         return result
#
#     # depth first search for the string, with the
#     # coordinates and a visited array to take care that we
#     # do not overlap the places visited already
#     def dfs(self, x: int, y: int, s: str, vis: List[List[bool]]) -> bool:
#
#         # if string length becomes 0 means string is found
#         if not s:
#             return True
#
#         vis[x][y] = True
#
#         # making a solution boolean to see if we can
#         # perform depth search to find answer
#         sol = False
#
#         # making possible moves
#         for move in self.mover:
#             currX = move[0] + x
#             currY = move[1] + y
#
#             # checking for out of bound areas
#             if 0 <= currX < len(self.board) and 0 <= currY < len(self.board[0]):
#
#                 # checking for similarity in the first
#                 # letter and the visited array
#                 if self.board[currX][currY] == s[0] and not vis[currX][currY]:
#                     if self.dfs(currX, currY, s[1:], vis):
#                         # removing the first letter
#                         # from the string
#                         sol = True
#
#         return sol
#
#
# # testing the code
# solver = Solution()
# board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'],
#          ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
# words = ['oath', 'pea', 'eat', 'rain']
# ans = solver.findWords(board, words)
# for part in ans:
#     print(part)
#
# def main():
#     # Lê a lista de palavras
#     with open('lista_palavras.txt') as f:
#         palavras = f.read().splitlines()
#
#     # Lê a matriz de letras
#     matriz_letras = np.loadtxt('matriz_letras.txt', dtype=str)
#
#     # Encontra as palavras na matriz de letras
#     palavras_encontradas = Solution()
#     ans = solver.findWords(board, words)
#
#     # Inicializa o Pygame
#     pygame.init()
#
#     # Configura a janela do Pygame
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Caça-palavras")
#
#     # Define a fonte utilizada para desenhar as palavras encontradas
#     font = pygame.font.SysFont("Arial", 20)
#
#     # Desenha as palavras encontradas na tela
#     y = 50
#     for palavra in palavras_encontradas:
#         # Cria um texto a partir da palavra encontrada
#         text = font.render(palavra, True, (0, 255, 0))
#
#         # Define a posição do texto na tela
#         x = 50
#         y += 30
#
#         # Desenha o texto na tela
#         screen.blit(text, (x, y))
#
#     # Atualiza a tela
#     pygame.display.update()
#
#     # Espera até o usuário fechar a janela do Pygame
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#
# if __name__ == '__main__':
#     main()



import sys
from typing import List

import numpy as np
import pygame

from tkinter import *
import random
from typing import List


class Solution:
    def __init__(self):
        # making the possible moves in movers array
        self.mover = [
            [1, 0], [0, 1], [-1, 0], [0, -1],
            [1, 1], [-1, -1], [1, -1], [-1, 1]
        ]

    # making a function findwords to find words along with
    # their location which inputs the board and list of
    # words
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        rows = len(board)
        cols = len(board[0])

        # making board a global variable
        self.board = board

        for word in words:
            for i in range(rows):
                for j in range(cols):
                    if self.board[i][j] == word[0]:

                        # making a function findwords to
                        # find words along with their
                        # location which inputs the board
                        # and list of words
                        if self.dfs(i, j, word[1:], [[False] * cols for _ in range(rows)]):
                            result.append(f"{word}")

        return result

    # depth first search for the string, with the
    # coordinates and a visited array to take care that we
    # do not overlap the places visited already
    def dfs(self, x: int, y: int, s: str, vis: List[List[bool]]) -> bool:

        # if string length becomes 0 means string is found
        if not s:
            return True

        vis[x][y] = True

        # making a solution boolean to see if we can
        # perform depth search to find answer
        sol = False

        # making possible moves
        for move in self.mover:
            currX = move[0] + x
            currY = move[1] + y

            # checking for out of bound areas
            if 0 <= currX < len(self.board) and 0 <= currY < len(self.board[0]):

                # checking for similarity in the first
                # letter and the visited array
                if self.board[currX][currY] == s[0] and not vis[currX][currY]:
                    if self.dfs(currX, currY, s[1:], vis):
                        # removing the first letter
                        # from the string
                        sol = True

        return sol

def cria_palavras(palavras):
        """
        Cria um dicionário com as palavras do jogo e suas posições.

        Args:
            palavras (list): uma lista de strings contendo as palavras a serem incluídas no jogo.

        Returns:
            dict: um dicionário contendo cada palavra e sua posição no jogo.
        """
        palavras_posicoes = {}
        for palavra in palavras:
            posicao = input(f"Informe a posição da palavra '{palavra}': ")
            palavras_posicoes[palavra] = posicao
        return palavras_posicoes

def cria_jogo(palavras: List[str], tamanho_grade: int) -> List[List[str]]:
        # Criar uma matriz quadrada de tamanho 'tamanho_grade' por 'tamanho_grade' com letras aleatórias
        grade = [[random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(tamanho_grade)] for _ in
                 range(tamanho_grade)]

        # Colocar as palavras na matriz
        for palavra in palavras:
            direcoes = ['horizontal', 'vertical', 'diagonal']
            direcao = random.choice(direcoes)
            linha = random.randint(0, tamanho_grade - 1)
            coluna = random.randint(0, tamanho_grade - 1)

            # Verificar se é possível colocar a palavra na direção escolhida
            palavra_valida = False
            if direcao == 'horizontal':
                if coluna + len(palavra) <= tamanho_grade:
                    palavra_valida = True
            elif direcao == 'vertical':
                if linha + len(palavra) <= tamanho_grade:
                    palavra_valida = True
            elif direcao == 'diagonal':
                if linha + len(palavra) <= tamanho_grade and coluna + len(palavra) <= tamanho_grade:
                    palavra_valida = True

            # Colocar a palavra na matriz
            if palavra_valida:
                for i in range(len(palavra)):
                    if direcao == 'horizontal':
                        grade[linha][coluna + i] = palavra[i]
                    elif direcao == 'vertical':
                        grade[linha + i][coluna] = palavra[i]
                    elif direcao == 'diagonal':
                        grade[linha + i][coluna + i] = palavra[i]

        return grade

def gera_jogo():
    words = palavra_entry.get().upper().split(",")
    size = int(tamanho_entry.get())
    game = cria_jogo(words, size)
    resposta_text.delete("1.0", END)
    resposta_text.insert(END, game)
    resposta_text.config(state="disabled")


# def main():
#     # Lê a lista de palavras
#     with open('lista_palavras.txt') as f:
#         palavras = f.read().splitlines()
#
#     # Lê a matriz de letras
#     matriz_letras = np.loadtxt('matriz_letras.txt', dtype=str)
#
#     # Encontra as palavras na matriz de letras
#     solver = Solution()
#     palavras_encontradas = solver.findWords(matriz_letras.tolist(), palavras)
#
#     # Inicializa o Pygame
#     pygame.init()
#
#     # Configura a janela do Pygame
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Caça-palavras")
#
#     # Define a fonte utilizada para desenhar as palavras encontradas
#     font = pygame.font.SysFont("Arial", 20)
#
#     # Desenha as palavras encontradas na tela
#     y = 50
#     for palavra in palavras_encontradas:
#         # Cria um texto a partir da palavra encontrada
#         text = font.render(palavra, True, (0, 255, 0))
#
#         # Define a posição do texto na tela
#         x = 50
#         y += 30
#
#         # Desenha o texto na tela
#         screen.blit(text, (x, y))
#
#     # Atualiza a tela
#     pygame.display.update()
#
#     # Espera até o usuário fechar a janela do Pygame
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

# def main():
#     # Lê a lista de palavras
#     with open('lista_palavras.txt') as f:
#         palavras = f.read().splitlines()
#
#     # Lê a matriz de letras
#     matriz_letras = np.loadtxt('matriz_letras.txt', dtype=str)
#
#     # Encontra as palavras na matriz de letras
#     solver = Solution()
#     palavras_encontradas = solver.findWords(matriz_letras, palavras)
#
#     # Inicializa o Pygame
#     pygame.init()
#
#     # Configura a janela do Pygame
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Caça-palavras")
#
#     # Define a fonte utilizada para desenhar as palavras encontradas
#     font = pygame.font.SysFont("Arial", 20)
#
#     # Define a cor de fundo da tela do jogo
#     bg_color = (255, 255, 255)
#
#     # Loop principal do jogo
#     while True:
#         # Cria uma nova superfície com o tamanho da janela do Pygame
#         surface = pygame.Surface((800, 600))
#
#         # Define a cor de fundo da superfície
#         surface.fill(bg_color)
#
#         # Desenha as palavras encontradas na tela
#         y = 50
#         for palavra in palavras_encontradas:
#             # Cria um texto a partir da palavra encontrada
#             text = font.render(palavra, True, (0, 255, 0))
#
#             # Define a posição do texto na tela
#             x = 50
#             y += 30
#
#             # Desenha o texto na superfície
#             surface.blit(text, (x, y))
#
#         # Blit a superfície para a janela principal do Pygame
#         screen.blit(surface, (0, 0))
#
#         # Atualiza a tela do Pygame
#         pygame.display.update()
#
#         # Verifica eventos do Pygame
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#
# if __name__ == '__main__':
    #main()

if __name__ == '__main__':
    window = Tk()
    window.title("Caça-Palavras")
    window.config(padx=10, pady=10)

    # Labels
    palavra_label = Label(text="Palavras (separadas por vírgula):")
    palavra_label.grid(row=0, column=0)

    tamanho_label = Label(text="Tamanho da grade:")
    tamanho_label.grid(row=1, column=0)

    resposta_label = Label(text="Jogo:")
    resposta_label.grid(row=2, column=0)

    # Entries
    palavra_entry = Entry(width=35)
    palavra_entry.grid(row=0, column=1, columnspan=2)
    palavra_entry.focus()

    tamanho_entry = Entry(width=35)
    tamanho_entry.grid(row=1, column=1, columnspan=2)

    # Text box
    resposta_text = Text(height=20, width=50)
    resposta_text.grid(row=3, column=0, columnspan=3)
    resposta_text.config(state="disabled")

    # Button
    add_button = Button(text="Gerar Jogo", width=36, command=gera_jogo)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()