import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000,300
GROUND_Y = 250
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
DARK_GREEN = (60, 110, 60)
LIGHT_GREEN = (90, 140, 90)
RED = (200, 50, 50)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Never-Ending Dino Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 24, bold=True)
big_font = pygame.font.SysFont("Courier New", 48, bold=True)

# High score file
HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score))

# Dino class
class Dino:
    def __init__(self):
        self.x = 70
        self.y = GROUND_Y - 48
        self.w = 40
        self.h = 48
        self.vy = 0
        self.gravity = 0.6
        self.jump_power = -12
        self.grounded = True
        self.ducking = False
        self.frame = 0

    def jump(self):
        if self.grounded:
            self.vy = self.jump_power
            self.grounded = False

    def duck(self, active):
        self.ducking = active and self.grounded

    def update(self):
        self.vy += self.gravity
        self.y += self.vy
        floor_y = GROUND_Y - (self.h * 0.65 if self.ducking else self.h)
        if self.y >= floor_y:
            self.y = floor_y
            self.vy = 0
            self.grounded = True
        else:
            self.grounded = False
        self.frame += 1

    def get_hitbox(self):
        shrink = 6
        if self.ducking:
            return pygame.Rect(
                self.x + shrink,
                self.y + 16,
                self.w - shrink * 2,
                self.h - 16 - shrink
            )
        else:
            return pygame.Rect(
                self.x + shrink,
                self.y + shrink,
                self.w - shrink * 2,
                self.h - shrink * 2
            )

    def draw(self, surf):
        # Body
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if self.ducking:
            rect.h = int(self.h * 0.65)
            rect.y = GROUND_Y - rect.h
        pygame.draw.rect(surf, DARK_GREEN, rect, border_radius=6)
        pygame.draw.rect(surf, LIGHT_GREEN, rect.inflate(-12, -12), border_radius=4)
        # Eye
        eye_x = rect.x + (30 if self.ducking else 28)
        eye_y = rect.y + 10
        pygame.draw.circle(surf, WHITE, (eye_x, eye_y), 5)
        pygame.draw.circle(surf, BLACK, (eye_x + 2, eye_y), 2.5)
        # Mouth
        pygame.draw.rect(surf, (42, 90, 42), (rect.x + 30, rect.y + 16, 8, 3))
        # Legs (only when grounded)
        if self.grounded:
            leg_off = int(pygame.math.Vector2(0, 0).rotate(self.frame * 5).y * 0.3)
            pygame.draw.rect(surf, (42, 90, 42), (rect.x + 6, rect.bottom - 4, 6, 6 + leg_off))
            pygame.draw.rect(surf, (42, 90, 42), (rect.right - 12, rect.bottom - 4, 6, 6 - leg_off))
        # Tiny arms
        pygame.draw.rect(surf, (42, 90, 42), (rect.x + 4, rect.y + 12, 4, 6))
        pygame.draw.rect(surf, (42, 90, 42), (rect.right - 8, rect.y + 12, 4, 6))

# Obstacle classes
class Cactus:
    def __init__(self, x):
        size = random.choice([
            (16, 28), (22, 38), (28, 48)
        ])
        self.w, self.h = size
        self.x = x
        self.y = GROUND_Y - self.h
        self.passed = False

    def update(self, speed):
        self.x -= speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, surf):
        g = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(surf, (30, 130, 30), g, border_radius=4)
        pygame.draw.rect(surf, (20, 100, 20), g.inflate(-6, -6), border_radius=3)
        # spines
        for i in range(3):
            sx = self.x + 4 + i * 7
            sy = self.y + 6 + i * 12
            pygame.draw.rect(surf, (20, 100, 20), (sx, sy - 2, 2, 6))
            pygame.draw.rect(surf, (20, 100, 20), (sx + 10, sy - 2, 2, 6))

class Pterodactyl:
    def __init__(self, x):
        self.x = x
        self.w = 40
        self.h = 28
        self.y = random.choice([GROUND_Y - 58 - 12, GROUND_Y - 58 - 40])
        self.passed = False
        self.wing_angle = 0

    def update(self, speed):
        self.x -= speed
        self.wing_angle += 0.15

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, surf):
        wing = abs(pygame.math.Vector2(0, 0).rotate(self.wing_angle * 50).y) * 0.03
        # Body
        pygame.draw.ellipse(surf, (60, 60, 60), (self.x, self.y, 36, 20))
        # Head
        pygame.draw.circle(surf, (60, 60, 60), (self.x + 34, self.y + 6), 7)
        # Beak
        pygame.draw.polygon(surf, (200, 130, 30), [
            (self.x + 40, self.y + 6),
            (self.x + 48, self.y + 8),
            (self.x + 40, self.y + 10)
        ])
        # Wings
        pygame.draw.ellipse(surf, (60, 60, 60), (self.x + 6, self.y - 2 + wing * 20, 20, 8))
        pygame.draw.ellipse(surf, (60, 60, 60), (self.x + 6, self.y + 16 - wing * 20, 20, 8))
        # Eye
        pygame.draw.circle(surf, WHITE, (self.x + 36, self.y + 4), 3)
        pygame.draw.circle(surf, BLACK, (self.x + 38, self.y + 4), 1.5)

# Game functions
def spawn_obstacle(obstacles):
    if random.random() < 0.3:
        obstacles.append(Pterodactyl(800))
    else:
        obstacles.append(Cactus(800))

def check_collision(dino, obstacles):
    d_rect = dino.get_hitbox()
    for obs in obstacles:
        if d_rect.colliderect(obs.get_rect()):
            return True
    return False

def draw_ground(surf, offset):
    pygame.draw.rect(surf, GRAY, (0, GROUND_Y, WIDTH, 4))
    for i in range(int(-offset), WIDTH + 40, 24):
        pygame.draw.rect(surf, (180, 180, 180), (i, GROUND_Y + 8, 12, 3))
        
def main():
    # Game state
    dino = Dino()
    obstacles = []
    score = 0
    highscore = load_highscore()
    speed = 6
    base_speed = 6
    max_speed = 16
    spawn_rate = 60
    min_spawn_rate = 25
    frame_counter = 0
    ground_offset = 0
    game_over = False
    running = True

    while running:
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    if game_over:
                        # Restart
                        game_over = False
                        dino = Dino()
                        obstacles.clear()
                        score = 0
                        speed = base_speed
                        spawn_rate = 60
                        frame_counter = 0
                        ground_offset = 0
                        continue
                    else:
                        dino.jump()
                if event.key == pygame.K_DOWN:
                    if not game_over:
                        dino.duck(True)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    dino.duck(False)

        if not game_over:
            # Update
            dino.update()

            # Speed scaling
            speed = base_speed + (score // 200) * 0.8
            speed = min(speed, max_speed)
            spawn_rate = max(min_spawn_rate, 60 - score // 80)

            # Spawn
            frame_counter += 1
            if frame_counter >= spawn_rate:
                frame_counter = 0
                # Prevent obstacle spam
                too_close = any(o.x > 600 for o in obstacles)
                if not too_close and random.random() < 0.65:
                    spawn_obstacle(obstacles)

            # Update obstacles
            for obs in obstacles[:]:
                obs.update(speed)
                if not obs.passed and obs.x + obs.w < dino.x:
                    obs.passed = True
                    score += 10
                if obs.x + obs.w < -20:
                    obstacles.remove(obs)

            # Ground scroll
            ground_offset = (ground_offset + speed) % 24

            # Collision
            if check_collision(dino, obstacles):
                game_over = True
                if score > highscore:
                    highscore = score
                    save_highscore(highscore)

            # Passive score
            if frame_counter % 4 == 0:
                score += 1

        # ----- Drawing -----
        screen.fill(WHITE)
        # Sky gradient
        for y in range(HEIGHT):
            color = (232 + (255 - 232) * (y / HEIGHT), 240 + (255 - 240) * (y / HEIGHT), 254 + (255 - 254) * (y / HEIGHT))
            pygame.draw.line(screen, (int(color[0]), int(color[1]), int(color[2])), (0, y), (WIDTH, y))

        draw_ground(screen, ground_offset)

        # Obstacles
        for obs in obstacles:
            obs.draw(screen)

        # Dino
        dino.draw(screen)

        # HUD
        score_text = font.render(f"🏆 {score}", True, BLACK)
        screen.blit(score_text, (WIDTH - 100, 10))
        high_text = font.render(f"⭐ {highscore}", True, (184, 134, 11))
        screen.blit(high_text, (WIDTH - 120, 40))

        # Speed
        speed_text = font.render(f"speed {speed:.1f}", True, GRAY)
        screen.blit(speed_text, (10, 10))

        # Game Over overlay
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            screen.blit(overlay, (0, 0))
            go_text = big_font.render("💀 GAME OVER", True, WHITE)
            screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, 130))
            restart_text = font.render("Press SPACE or UP to restart", True, (220, 220, 220))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 200))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()