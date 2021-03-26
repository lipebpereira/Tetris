import pygame
import random

pygame.font.init()

# Váriaveis globais
s_width = 800
s_height = 700
play_width = 300
play_height = 600 
block_size = 30
CINZA = (127, 127, 127)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# Formato das peças, cada letra significando o formato que a peça tem
S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
 # Cor das peças
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

 # Peça
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_positions={}):
	# Criando uma lista com 10 espaços para todas as 20 linhas, para representar as colunas
    # Definimos como (0,0,0) que significa a cor preta
    grid = [[PRETO for x in range(10)] for x in range(20)]
    
    # Vendo se há algum forma já presente no grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j, i) in locked_positions:
                locked = locked_positions[(j,i)]
                grid[i][j] = locked
    return grid

# Definindo o formato para ser possível trabalhar com ele
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    
    return positions

# Espaços válidos
def valid_space(shape, grid):
    accepted_pos = [[(j,i) for j in range(10) if grid[i][j] == PRETO] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
    
    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    
    return False


# Define um formato random para a peça
def get_shape():
	return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
	pass

# Desenha a grid do jogo
def draw_grid(surface, grid):
    start_x = top_left_x
    start_y = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, CINZA, (start_x, start_y+ i*30), (start_x + play_width, start_y + i * 30))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, CINZA, (start_x + j * 30, start_y), (start_x + j * 30, start_y + play_height))

# Limpar a linha quando ela está completa
def clear_rows(grid, locked):
    increment = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (PRETO) not in row: #se não há preto, ela está cheia
            increment += 1
            index = i
            for j in range(len(row)):
                try:
                    del locked[(j,i)]
                except:
                    continue
    if increment > 0:
        for key in sorted(list(locked), key = lambda x: x[1])[::-1]:
            x, y = key
            if y < index:
                newKey = (x, y+increment)
                locked[newKey] = locked.pop(key)
    return increment

def draw_next_shape(shape, surface):
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    label = font.render('Next Shape', 1, PRETO)

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
    
    surface.blit(label, (sx + 10, sy - 30))

# Cria a Janela
def draw_window(surface, grid, score =0):
    surface.fill(CINZA)
    font = pygame.font.Font(pygame.font.get_default_font(), 60)
    label = font.render('Tetris do Felipe', 1, BRANCO)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2),30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)

    draw_grid(surface,grid)

    pygame.draw.rect(surface, VERMELHO, (top_left_x, top_left_y, play_width, play_height), 4)

    

# Função main
def main(window):
	
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece,grid)):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece,grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece,grid)):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
        
        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
        
        if change_piece:
            for pos in shape_pos:
                p = (pos[0],pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score *= clear_rows(grid,locked_positions) * 10

        draw_window(window,grid)

        draw_next_shape(next_piece, window)
        # Colocar a contagem dos pontos aqui, perto do formato da próxima peça
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    pygame.display.quit()

def main_menu(window):
    main(window)

window = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption('Tetris do Felipe')
main_menu(window)  # começa o jogo