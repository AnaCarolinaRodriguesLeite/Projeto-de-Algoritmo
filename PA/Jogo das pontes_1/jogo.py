import pygame
import time
import random

# Constantes
WINDOW_SIZE = (800, 600)
CELL_SIZE = 40
LABIRINTO_SIZE = (15, 15)
TEMPO_MAXIMO = 60
PALAVRAS = ['RUBY', 'JAVA', 'PYTHON', 'JAVASCRIPT']

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Inicialização do Pygame
pygame.init()

# Fonte para as palavras encontradas
fonte = pygame.font.Font(None, 30)

def criar_labirinto(n_linhas, n_colunas):
    """
    Cria um labirinto de letras aleatório.
    """
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    labirinto = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha.append(random.choice(letras))
        labirinto.append(linha)
    return labirinto

def desenhar_labirinto(screen, labirinto, selecionados):
    """
    Desenha o labirinto na tela.
    """
    for i, linha in enumerate(labirinto):
        for j, letra in enumerate(linha):
            x, y = j * CELL_SIZE, i * CELL_SIZE
            cor = WHITE
            if (i, j) in selecionados:
                cor = GREEN
            pygame.draw.rect(screen, cor, (x, y, CELL_SIZE, CELL_SIZE), 1)
            texto = fonte.render(letra, True, WHITE)
            screen.blit(texto, (x + 10, y + 10))

def exibir_palavras(screen, palavras_encontradas):
    """
    Exibe as palavras encontradas na tela.
    """
    texto = fonte.render('Palavras encontradas:', True, WHITE)
    screen.blit(texto, (10, WINDOW_SIZE[1] - 40))
    y = WINDOW_SIZE[1] - 40
    for palavra in palavras_encontradas:
        y -= 30
        texto = fonte.render(palavra, True, WHITE)
        screen.blit(texto, (10, y))


def bfs(labirinto, palavra, i, j):
    """
    Realiza a busca em largura no labirinto para encontrar a palavra.
    """
    visitados = set()
    fila = [(i, j, 0)]
    while fila:
        i, j, k = fila.pop(0)
        if k == len(palavra):
            return True
        if i < 0 or i >= len(labirinto) or j < 0 or j >= len(labirinto[0]):
            continue
        if (i, j) in visitados:
            continue
        if labirinto[i][j] != palavra[k]:
            continue
        visitados.add((i, j))
        fila.append((i + 1, j, k + 1))
        fila.append((i - 1, j, k + 1))
        fila.append((i, j + 1, k + 1))
        fila.append((i, j - 1, k + 1))
    return False

def dfs(labirinto, i, j, palavra, visitados):
    if not palavra:
        return True

    for di, dj in DIRECOES:
        ni, nj = i + di, j + dj
        if (ni, nj) not in visitados and dentro_do_labirinto(labirinto, ni, nj) and labirinto[ni][nj] == palavra[0]:
            visitados.add((ni, nj))
            if dfs(labirinto, ni, nj, palavra[1:], visitados):
                return True
            visitados.remove((ni, nj))

    return False


def mensagem_vitoria(screen):
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render("Você venceu!", True, WHITE)
    texto_rect = texto.get_rect(center=screen.get_rect().center)
    screen.blit(texto, texto_rect)

def mensagem_tempo(screen):
    fonte = pygame.font.SysFont(None, 50)
    texto = fonte.render("Tempo acabou!", True, WHITE)
    texto_rect = texto.get_rect(center=screen.get_rect().center)
    screen.blit(texto, texto_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Jogo de Palavras')

    labirinto = criar_labirinto(*LABIRINTO_SIZE)
    palavras_encontradas = []
    selecionados = set()
    palavras_a_encontrar = ['ruby', 'java', 'python', 'javascript']

    # Iniciando o contador de tempo
    tempo_inicial = time.time()

    while True:
        # Verificando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificando se a célula selecionada faz parte de alguma palavra
                x, y = event.pos
                i, j = y // CELL_SIZE, x // CELL_SIZE
                visitados = set([(i, j)])
                selecionados.add((i, j))
                palavra_encontrada = None

                # Verificando cada palavra a ser encontrada
                for palavra in palavras_a_encontrar:
                    if bfs(labirinto, palavra, i, j):
                        palavras_encontradas.append(palavra)
                        palavra_encontrada = palavra
                        break
                    elif dfs(labirinto, i, j, palavra, visitados):
                        palavras_encontradas.append(palavra)
                        palavra_encontrada = palavra
                        break

                # Removendo as letras da palavra encontrada do labirinto
                if palavra_encontrada:
                    for k, (x, y) in enumerate(palavra_encontrada):
                        selecionados.add((x, y))
                        labirinto[x][y] = None

                # Verificando se todas as palavras foram encontradas
                if set(palavras_a_encontrar) == set(palavras_encontradas):
                    screen.fill(BLACK)
                    mensagem_vitoria(screen)
                    pygame.display.flip()
                    time.sleep(5)
                    pygame.quit()
                    return

        # Desenhando o labirinto e as palavras encontradas na tela
        screen.fill(BLACK)
        desenhar_labirinto(screen, labirinto, selecionados)
        exibir_palavras(screen, palavras_encontradas)

        # Verificando se o tempo do jogo acabou
        tempo_atual = time.time()
        if tempo_atual - tempo_inicial >= TEMPO_MAXIMO:
            screen.fill(BLACK)
            mensagem_tempo(screen)
            pygame.display.flip()
            time.sleep(5)
            pygame.quit()
            return

        pygame.display.flip()

if __name__ == '__main__':
    main()