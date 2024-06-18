import pygame
import sys
import random

# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
FPS = 60

# Create window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")


# Initialize variables
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player1 = pygame.Rect(50, HEIGHT // 2 - 60, 20, 120)
player2 = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 60, 20, 120)
ball_speed_x = 7 * random.choice((1, -1))  # Randomize initial direction
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 10

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Player 1 controls
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed

    # Player 2 controls
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collisions with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Respawn ball if out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Draw everything
    win.fill(WHITE)
    pygame.draw.rect(win, (0, 0, 255), player1)
    pygame.draw.rect(win, (255, 0, 0), player2)
    pygame.draw.ellipse(win, (0, 255, 0), ball)
    pygame.draw.aaline(win, (255, 255, 0), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)
