import maze as maze
import pygame

graph = {
    'B': ['A', 'N', 'A', 'N', 'A'],
    'A': ['B', 'N', 'A', 'N', 'A', 'M', 'A', 'C', 'A'],
    'N': ['B', 'A', 'N', 'A', 'M', 'O', 'R', 'A', 'N', 'G', 'O'],
    'M': ['A', 'O', 'R', 'A', 'N', 'G', 'O'],
    'O': ['N', 'M', 'R', 'A', 'N', 'G', 'O'],
    'R': ['N', 'M', 'O', 'A', 'N', 'G', 'O'],
    'G': ['N', 'R', 'A', 'N', 'G', 'O'],
    'P': ['E', 'R', 'A'],
    'E': ['P', 'R', 'A']
}

words = {'Banana': 6, 'mamao': 5, 'maca': 4, 'pera': 4, 'morango': 7}

def bfs(graph, start, word, length):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if len(path) == length - 1 and next == word[length - 1]:
                return True
            else:
                queue.append((next, path + [next]))
    return False

# Função para desenhar o labirinto na tela
def draw_maze():
    # Define as dimensões dos retângulos
    rect_width = 800 // 10
    rect_height = 600 // 10

    # Percorre a matriz maze e desenha os retângulos correspondentes
    for row in range(10):
        for col in range(10):
            x = col * rect_width
            y = row * rect_height
            if maze[row][col] == 'X':
                pygame.draw.rect(screen, black, (x, y, rect_width, rect_height))
            else:
                pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))


# Função para desenhar as palavras encontradas na tela
def draw_words():
    pass

# Função principal do jogo
def main():
    # Inicializa o Pygame
    pygame.init()

    # Define as dimensões da janela do jogo
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Define o título da janela do jogo
    pygame.display.set_caption("Caça-Palavras")

    # Define as cores que serão usadas no jogo
# Define as cores que serão usadas no jogo
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    # Define a fonte que será usada para desenhar as palavras encontradas
    font = pygame.font.Font(None, 30)

    # Define o tempo máximo que o jogador tem para encontrar todas as palavras (em segundos)
    max_time = 60

    # Inicializa o relógio do jogo
    clock = pygame.time.Clock()

    # Cria uma lista para armazenar as palavras encontradas
    found_words = []

    # Define o nó inicial do grafo
    start_node = 'B'

    # Define o comprimento máximo das palavras
    max_length = max(words.values())

    # Loop principal do jogo
    running = True
    while running:
        # Processa eventos do Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenha o labirinto na tela
        screen.fill(white)
        draw_maze()

        # Verifica se o tempo acabou
        time_remaining = max_time - pygame.time.get_ticks() // 1000
        if time_remaining <= 0:
            running = False

        # Desenha as palavras encontradas na tela
        draw_words()

        # Verifica se o jogador acertou alguma palavra
        for word, length in words.items():
            if length <= max_length and word not in found_words:
                if bfs(graph, start_node, word, length):
                    found_words.append(word)
                    # Marca as letras da palavra no labirinto com a cor vermelha
                    for letter in word:
                        pass  # Implementar aqui a marcação das letras no labirinto com a cor vermelha

        # Verifica se o jogador encontrou todas as palavras
        if len(found_words) == len(words):
            running = False

        # Atualiza a janela do jogo
        pygame.display.update()

        # Define a taxa de atualização do jogo (FPS)
        clock.tick(60)

    # Exibe a mensagem de vitória ou derrota
    if len(found_words) == len(words):
        text = font.render("Parabéns, você ganhou!", True, black)
    else:
        text = font.render("Você perdeu!", True, black)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    pygame.display.update()

    # Aguarda 3 segundos antes de sair do jogo
    pygame.time.wait(3000)

    # Encerra o Pygame
    pygame.quit()
