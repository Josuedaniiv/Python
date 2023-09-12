import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)

# Size of each Tetris block
BLOCK_SIZE = 30

# Tetris piece shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]]
]

# Tetris piece colors
COLORS = [CYAN, YELLOW, ORANGE, GREEN, PURPLE]

# Initialize game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

class Piece:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = WIDTH // 2 - len(shape[0]) * BLOCK_SIZE // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def move_left(self):
        self.x -= BLOCK_SIZE

    def move_right(self):
        self.x += BLOCK_SIZE

    def move_down(self):
        self.y += BLOCK_SIZE

    def draw(self):
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]:
                    pygame.draw.rect(window, self.color, (self.x + col * BLOCK_SIZE, self.y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(window, BLACK, (self.x + col * BLOCK_SIZE, self.y + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

class Grid:
    def __init__(self):
        self.grid = [[0] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]

    def is_collision(self, piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col]:
                    if (
                        piece.x + col < 0
                        or piece.x + col >= WIDTH // BLOCK_SIZE
                        or piece.y + row >= HEIGHT // BLOCK_SIZE
                        or self.grid[piece.y // BLOCK_SIZE + row][piece.x // BLOCK_SIZE + col]
                    ):
                        return True
        return False

    def add_piece(self, piece):
        for row in range(len(piece.shape)):
            for col in range(len(piece.shape[row])):
                if piece.shape[row][col]:
                    self.grid[piece.y // BLOCK_SIZE + row][piece.x // BLOCK_SIZE + col] = 1

    def clear_lines(self):
        full_rows = []
        for row in range(len(self.grid)):
            if all(self.grid[row]):
                full_rows.append(row)
        for row in full_rows:
            del self.grid[row]
            self.grid.insert(0, [0] * (WIDTH // BLOCK_SIZE))
        return len(full_rows)

    def draw(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col]:
                    pygame.draw.rect(window, WHITE, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(window, BLACK, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 2)

def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    window.blit(text, (10, 10))

def game_over():
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, RED)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(300)