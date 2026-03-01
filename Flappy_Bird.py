import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)

# Bird
bird_x = 100
bird_y = HEIGHT // 2
bird_radius = 15
velocity = 0
gravity = 0.5
flap_power = -8

# Dash
dash_speed = 12
dash_cooldown = 0
dash_max = 60  # frames

# Pipes
pipe_width = 70
pipe_gap = 180
pipe_speed = 4
pipes = []

# Coins
coins = []

score = 0
coin_score = 0
gravity_flip = 1  # 1 = normal, -1 = inverted

def create_pipe():
    gap_y = random.randint(150, HEIGHT - 150)
    pipe = {
        "x": WIDTH,
        "gap_y": gap_y,
        "passed": False
    }
    pipes.append(pipe)

def create_coin(x, gap_y):
    coin = {
        "x": x + pipe_width // 2,
        "y": gap_y,
        "collected": False
    }
    coins.append(coin)

create_pipe()

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Flap
    if keys[pygame.K_SPACE]:
        velocity = flap_power * gravity_flip

    # Dash
    if keys[pygame.K_LSHIFT] and dash_cooldown == 0:
        bird_x += dash_speed
        dash_cooldown = dash_max

    if dash_cooldown > 0:
        dash_cooldown -= 1

    # Gravity
    velocity += gravity * gravity_flip
    bird_y += velocity

    # Create new pipes
    if pipes[-1]["x"] < WIDTH - 250:
        create_pipe()
        create_coin(WIDTH, pipes[-1]["gap_y"])

    # Move pipes
    for pipe in pipes:
        pipe["x"] -= pipe_speed

        # Score when passing pipe
        if not pipe["passed"] and pipe["x"] + pipe_width < bird_x:
            pipe["passed"] = True
            score += 1

            # Gravity flip every 15 score
            if score % 15 == 0:
                gravity_flip *= -1

        # Draw pipes
        top_rect = pygame.Rect(pipe["x"], 0, pipe_width, pipe["gap_y"] - pipe_gap // 2)
        bottom_rect = pygame.Rect(pipe["x"], pipe["gap_y"] + pipe_gap // 2, pipe_width, HEIGHT)

        pygame.draw.rect(screen, GREEN, top_rect)
        pygame.draw.rect(screen, GREEN, bottom_rect)

        # Collision
        bird_rect = pygame.Rect(bird_x - bird_radius, bird_y - bird_radius, bird_radius * 2, bird_radius * 2)
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            running = False

    # Move coins
    for coin in coins:
        coin["x"] -= pipe_speed

        if not coin["collected"]:
            dist = ((bird_x - coin["x"]) ** 2 + (bird_y - coin["y"]) ** 2) ** 0.5
            if dist < bird_radius + 10:
                coin["collected"] = True
                coin_score += 1

        if not coin["collected"]:
            pygame.draw.circle(screen, GOLD, (int(coin["x"]), int(coin["y"])), 10)

    # Bird color (dash cooldown indicator)
    if dash_cooldown > 0:
        pygame.draw.circle(screen, RED, (bird_x, int(bird_y)), bird_radius)
    else:
        pygame.draw.circle(screen, YELLOW, (bird_x, int(bird_y)), bird_radius)

    # Ground / ceiling collision
    if bird_y < 0 or bird_y > HEIGHT:
        running = False

    # UI text
    score_text = font.render(f"Score: {score}", True, WHITE)
    coin_text = font.render(f"Coins: {coin_score}", True, WHITE)
    gravity_text = font.render(
        "Gravity: DOWN" if gravity_flip == 1 else "Gravity: UP", True, WHITE
    )

    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (10, 40))
    screen.blit(gravity_text, (10, 70))

    pygame.display.update()

pygame.quit()
