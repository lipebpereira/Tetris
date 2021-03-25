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
        self.color = shape_color[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_position={}):
	# Criando uma lista com 10 espaços para todas as 20 linhas, para representar as colunas
    # Definimos como (0,0,0) que significa a cor preta
    grid = [[PRETO for x in range(10)] for x in range(20)]
    
    # Vendo se há algum forma já presente no grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j, i) in locked_position:
                locked = locked_position[(j,i)]
                grid[i][j] = locked
    return grid

def convert_shape_format(shape):
	pass

def valid_space(shape, grid):
	pass

def check_lost(positions):
	pass

# Define um formato random para a peça
def get_shape():
	return random.choice(shapes)


def draw_text_middle(text, size, color, surface):
	pass

# Desenha a grid do jogo
def draw_grid(surface, row, col):
    surface.fill(CINZA)
    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 60)
    label = font.render('Tetris do Felipe', 1, BRANCO)

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2),30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y+ i*block_size, block_size, block_size),0)

    pygame.draw.rect(surface, VERMELHO, (top_left_x, top_left_y, play_width, play_height),4)

    pygame.display.update()

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
	pass

def main():
	pass

def main_menu():
	pass

main_menu()  # começa o jogo