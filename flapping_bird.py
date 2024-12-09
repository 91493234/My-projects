import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)

# Game variables
gravity = 0.3  # Reduced gravity for slower falling
bird_movement = 0
game_active = True
score = 0
font = pygame.font.Font(None, 36)

# Load images
bird = pygame.image.load("bird.png").convert_alpha()
bird = pygame.transform.scale(bird, (50, 35))  # Resize the bird
bird_rect = bird.get_rect(center=(100, 300))

pipe_surface = pygame.image.load("pipe.png").convert_alpha()
pipe_surface = pygame.transform.scale(pipe_surface, (70, 400))

# Pipes
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1600)  # Spawn pipes every 1.6 seconds (slower spawn rate)
pipe_height = [300, 400, 500]

# Background
background = pygame.image.load("background.png").convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Load sounds
flap_sound = pygame.mixer.Sound("flap.wav")
# game_over_sound = pygame.mixer.Sound("game_over.wav")
# pygame.mixer.music.load("background.mp3")
pygame.mixer.music.set_volume(0.3)  # Adjust volume
# pygame.mixer.music.play(-1)  # Loop background music

# Function to draw pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT:
            SCREEN.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            SCREEN.blit(flip_pipe, pipe)

# Function to move pipes
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3  # Slower pipe movement
    return [pipe for pipe in pipes if pipe.right > 0]

# Collision detection
def check_collision(pipes):
    global game_active
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            game_active = False
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        game_active = False

# Display score
def display_score():
    score_surface = font.render(f"Score: {int(score)}", True, BLACK)
    SCREEN.blit(score_surface, (10, 10))

# Main game loop
clock = pygame.time.Clock()

while True:
    SCREEN.fill(WHITE)
    SCREEN.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 8  # Reduced upward movement for slower gameplay
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 300)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_position = random.choice(pipe_height)
            top_pipe = pipe_surface.get_rect(midbottom=(500, pipe_position - 150))
            bottom_pipe = pipe_surface.get_rect(midtop=(500, pipe_position))
            pipe_list.extend([top_pipe, bottom_pipe])

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += bird_movement
        SCREEN.blit(bird, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision
        check_collision(pipe_list)

        # Score
        score += 0.01  # Increment score slowly
        display_score()
    else:
        game_over_surface = font.render("Game Over! Press Space to Restart", True, BLACK)
        SCREEN.blit(game_over_surface, (40, SCREEN_HEIGHT / 2 - 20))

    pygame.display.update()
    clock.tick(60)
