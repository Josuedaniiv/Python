import pygame
import random
import pygame.mixer

# Inicializar Pygame
pygame.init()

# Inicializar Pygame mixer y cargar la música
pygame.mixer.init()
pygame.mixer.music.load("nombre_del_archivo_de_musica.wav") # musica de fondo

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Galaga")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Reproducir música en bucle
pygame.mixer.music.play(-1)

# Cargar imágenes de sprites
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
bullet_image = pygame.image.load("bullet.png")

# Clase Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height - self.rect.height
        self.speed_x = 0
    
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

# Clase Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 5)
    
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > screen_height + self.rect.height:
            self.kill()

# Clase Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = -10
    
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y < 0:
            self.kill()

# Grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Crear jugador
player = Player()
all_sprites.add(player)

# Crear enemigos
for i in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Bucle de juego
running = True
while running:
    # Actualizar sprites
    all_sprites.update()

    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.speed_x < 0:
                player.speed_x = 0
            elif event.key == pygame.K_RIGHT and player.speed_x > 0:
                player.speed_x = 0

    # Colisiones de balas con enemigos
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit inhits:
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

    # Colisiones de jugador con enemigos
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # Dibujar sprites en la pantalla
    screen.fill(black)
    all_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

# Detener la música y cerrar Pygame mixer
pygame.mixer.music.stop()
pygame.mixer.quit()

# Salir del juego
pygame.quit()