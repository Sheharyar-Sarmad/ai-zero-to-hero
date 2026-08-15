import pyglet
from pyglet.window import key
from pyglet import shapes
from pyglet.text import Label
import random
import math
from typing import List, Tuple, Optional

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
GOLD = (255, 215, 0)
DARK_RED = (139, 0, 0)
DARK_GREEN = (0, 100, 0)
LIGHT_BLUE = (173, 216, 230)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)


class Validation:
    def __init__(self):
        pass

    def are_enemies_damages_none(self, enemies: list, damages: list) -> bool:
        return enemies is None and damages is None

    def are_enemies_damages_lists(self, enemies: list, damages: list) -> bool:
        return not (isinstance(enemies, list) or isinstance(damages, list))

    def are_enemies_damages_0(self, enemies: list, damages: list) -> bool:
        return len(enemies) == 0 or len(damages) == 0

    def are_enemies_damages_types_valid(self, enemies: list, damages: list) -> bool:
        return all(isinstance(item, str) for item in enemies) and all(
            isinstance(item, int) for item in damages)

    def are_enemies_damages_length_equal(self, enemies: list, damages: list) -> bool:
        return len(enemies) == len(damages)

    def is_legal_damage(self, damages: list) -> bool:
        for damage in damages:
            if damage <= 0 or damage > 30:
                return False
        return True


class Logic(Validation):
    def __init__(self):
        super().__init__()
        self.coins = 0

    def boost_energy(self, energy_cost: int = 10) -> bool:
        if self.coins >= energy_cost:
            self.coins -= energy_cost
            return True
        return False

    def is_alive(self, damages: list, health: int) -> bool:
        for damage in damages:
            health -= damage
            if health <= 0:
                return False
        return True

    def apply_damage(self, damages: list[int], health: int) -> bool:
        for damage in damages:
            health -= damage
            if health <= 0:
                return False
        return True


class Player(Logic):
    def __init__(self, name: str, health: int, energy: int, coins: int = 0):
        super().__init__()
        self.name = name
        self.max_health = health
        self.health = health
        self.max_energy = energy
        self.energy = energy
        self.coins = coins
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed = 5
        self.radius = 20
        self.attack_cooldown = 0
        self.invincible = False
        self.invincible_timer = 0

    def attack(self, enemies: List[str], damages: List[int], use_energy: bool = True) -> Tuple[List[str], List[int]]:
        try:
            self.enemies = list(enemies) if enemies else []
            self.damages = list(damages) if damages else []
            self.use_energy = bool(use_energy)

            if self.are_enemies_damages_none(self.enemies, self.damages):
                print("\nThe enemies & damage cant be None!")
                return (list(self.enemies), list(self.damages))

            elif self.are_enemies_damages_lists(self.enemies, self.damages):
                print("\nThe enemies & damage are not the instance of list\n")
                return (list(self.enemies), list(self.damages))

            elif self.are_enemies_damages_0(self.enemies, self.damages):
                print("\nThe enemies & damage are empty!\n")
                return (list(self.enemies), list(self.damages))

            elif not self.are_enemies_damages_types_valid(self.enemies, self.damages):
                print("\nThe enemies & damage, name attributes are not valid instance\n")
                return (list(self.enemies), list(self.damages))

            elif not self.are_enemies_damages_length_equal(self.enemies, self.damages):
                print("\nThe enemies & damage length is not equal!\n")
                return (list(self.enemies), list(self.damages))

            elif not self.is_legal_damage(self.damages):
                print("\nThe damage is not legal, damage can be only between 1 to 30!\n")
                return (list(self.enemies), list(self.damages))

            elif not self.apply_damage(self.damages, self.health):
                print("\nYou died, Better luck next time!\n")
                return (list(self.enemies), list(self.damages))

            self.apply_damage(self.damages, self.health)

            if use_energy and self.energy > 0:
                self.energy = max(0, self.energy - 5)

            return (list(self.enemies), list(self.damages))

        except Exception as err:
            print(f"Error in attack: {err}")
            return ([], [])

    def move(self, dx: int, dy: int):
        self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x + dx * self.speed))
        self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y + dy * self.speed))

    def take_damage(self, damage: int):
        if not self.invincible:
            self.health -= damage
            self.invincible = True
            self.invincible_timer = 30

    def update(self):
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
            if self.invincible_timer == 0:
                self.invincible = False

        if self.energy < self.max_energy:
            self.energy = min(self.max_energy, self.energy + 0.1)

        if self.health < self.max_health:
            self.health = min(self.max_health, self.health + 0.05)


class Enemy:
    def __init__(self, x: int, y: int, name: str, health: int, damage: int):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.radius = 18
        self.speed = random.uniform(1.5, 3)
        self.color = random.choice([RED, ORANGE, PURPLE, DARK_RED])
        self.attack_cooldown = 0
        self.angle = random.uniform(0, 2 * math.pi)
        self.move_timer = 0

    def update(self, player_x: int, player_y: int):
        dx = player_x - self.x
        dy = player_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            self.move_timer += 1
            if self.move_timer > 60:
                self.angle += random.uniform(-0.5, 0.5)
                self.move_timer = 0

            speed_x = dx / distance * self.speed + math.cos(self.angle) * 0.5
            speed_y = dy / distance * self.speed + math.sin(self.angle) * 0.5

            self.x += speed_x
            self.y += speed_y

            self.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.x))
            self.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.y))

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

    def can_attack(self) -> bool:
        return self.attack_cooldown == 0

    def reset_attack_cooldown(self):
        self.attack_cooldown = 30


class BattleRoyaleGame:
    def __init__(self):
        self.window = pyglet.window.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Battle Royale - Pyglet Edition")
        self.window.set_location(100, 100)
        
        self.player = Player("Hero", 100, 100, 50)

        self.enemies = []
        self.projectiles = []
        self.particles = []
        self.powerups = []
        self.game_over = False
        self.win = False
        self.paused = False
        self.score = 0
        self.kills = 0
        self.wave = 1
        self.enemies_spawned = 0
        self.max_enemies = 5

        self.input_text = ""
        self.show_input = False
        self.input_active = False

        self.keys = key.KeyStateHandler()
        self.window.push_handlers(self.keys)

        self.spawn_enemies(3)
        self.spawn_powerups(2)

        self.bg_stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
                          random.randint(1, 3)) for _ in range(100)]

        self.frame_count = 0
        self.batch = pyglet.graphics.Batch()
        
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def spawn_enemies(self, count: int):
        enemy_names = ["Goblin", "Orc", "Troll", "Demon", "Wraith", "Skeleton", "Zombie", "Ghoul"]
        for _ in range(count):
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            while math.sqrt((x - self.player.x) ** 2 + (y - self.player.y) ** 2) < 200:
                x = random.randint(50, SCREEN_WIDTH - 50)
                y = random.randint(50, SCREEN_HEIGHT - 50)

            health = random.randint(20, 50 + self.wave * 10)
            damage = random.randint(5, 10 + self.wave * 2)
            name = random.choice(enemy_names)
            self.enemies.append(Enemy(x, y, name, health, damage))
            self.enemies_spawned += 1

    def spawn_powerups(self, count: int):
        powerup_types = ["health", "energy", "coin"]
        for _ in range(count):
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            powerup_type = random.choice(powerup_types)
            self.powerups.append({
                'x': x, 'y': y,
                'type': powerup_type,
                'radius': 15,
                'pulse': 0
            })

    def create_particles(self, x: int, y: int, color: tuple, count: int = 20):
        for _ in range(count):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            self.particles.append({
                'x': x, 'y': y,
                'vx': math.cos(angle) * speed,
                'vy': math.sin(angle) * speed,
                'life': random.randint(20, 60),
                'color': color,
                'size': random.randint(2, 6)
            })

    def update_particles(self):
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            if particle['life'] <= 0:
                self.particles.remove(particle)

    def update(self, dt):
        if self.paused or self.game_over or self.win:
            return

        self.frame_count += 1
        self.player.update()

        for enemy in self.enemies[:]:
            enemy.update(self.player.x, self.player.y)

            dist = math.sqrt((enemy.x - self.player.x) ** 2 + (enemy.y - self.player.y) ** 2)
            if dist < self.player.radius + enemy.radius and enemy.can_attack():
                self.player.take_damage(enemy.damage)
                enemy.reset_attack_cooldown()
                self.create_particles(self.player.x, self.player.y, RED, 10)
                print(f"Took {enemy.damage} damage from {enemy.name}!")

                if self.player.health <= 0:
                    self.game_over = True
                    print("Game Over!")
                    return

        self.update_particles()

        for powerup in self.powerups[:]:
            dist = math.sqrt((powerup['x'] - self.player.x) ** 2 + (powerup['y'] - self.player.y) ** 2)
            if dist < self.player.radius + powerup['radius']:
                if powerup['type'] == 'health':
                    self.player.health = min(self.player.max_health, self.player.health + 30)
                    self.create_particles(powerup['x'], powerup['y'], RED, 20)
                elif powerup['type'] == 'energy':
                    self.player.energy = min(self.player.max_energy, self.player.energy + 30)
                    self.create_particles(powerup['x'], powerup['y'], CYAN, 20)
                elif powerup['type'] == 'coin':
                    self.player.coins += random.randint(5, 20)
                    self.create_particles(powerup['x'], powerup['y'], GOLD, 30)
                self.powerups.remove(powerup)
                self.score += 5

        if self.frame_count % 300 == 0 and len(self.powerups) < 5:
            self.spawn_powerups(1)

        if len(self.enemies) == 0:
            self.wave += 1
            self.spawn_enemies(2 + self.wave)
            self.score += 20
            print(f"Wave {self.wave} started!")
            self.create_particles(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, GOLD, 40)

        if self.wave > 10:
            self.win = True

    def draw_health_bar(self, x: int, y: int, width: int, height: int, current: int, maximum: int, color: tuple):
        ratio = max(0, current / maximum)
        
        bg_rect = shapes.Rectangle(x, y, width, height, color=DARK_RED, batch=self.batch)
        
        if ratio > 0:
            hp_rect = shapes.Rectangle(x, y, width * ratio, height, color=color, batch=self.batch)
        
        border = shapes.Rectangle(x, y, width, height, color=WHITE, batch=self.batch)
        border.opacity = 100

    def draw_background(self):
        for i in range(0, SCREEN_HEIGHT, 5):
            color_value = int(20 + (i / SCREEN_HEIGHT) * 40)
            rect = shapes.Rectangle(0, i, SCREEN_WIDTH, 5, color=(0, 0, color_value), batch=self.batch)

        for star in self.bg_stars:
            circle = shapes.Circle(star[0], star[1], star[2], color=WHITE, batch=self.batch)
            circle.opacity = 150

        for x in range(0, SCREEN_WIDTH, 50):
            line = shapes.Line(x, 0, x, SCREEN_HEIGHT, color=(20, 20, 40), batch=self.batch)
            line.opacity = 50
        for y in range(0, SCREEN_HEIGHT, 50):
            line = shapes.Line(0, y, SCREEN_WIDTH, y, color=(20, 20, 40), batch=self.batch)
            line.opacity = 50

    def draw_ui(self):
        panel = shapes.Rectangle(10, SCREEN_HEIGHT - 200, 250, 190, color=BLACK, batch=self.batch)
        panel.opacity = 128
        
        border = shapes.Rectangle(10, SCREEN_HEIGHT - 200, 250, 190, color=WHITE, batch=self.batch)
        border.opacity = 100

        health_label = Label("HP", font_size=16, x=20, y=SCREEN_HEIGHT - 175, color=(255, 255, 255, 255))
        health_label.draw()
        self.draw_health_bar(60, SCREEN_HEIGHT - 175, 180, 20, self.player.health, self.player.max_health, RED)

        energy_label = Label("Energy", font_size=14, x=20, y=SCREEN_HEIGHT - 145, color=(255, 255, 255, 255))
        energy_label.draw()
        self.draw_health_bar(90, SCREEN_HEIGHT - 145, 150, 15, self.player.energy, self.player.max_energy, CYAN)

        coin_label = Label(f"💰 {int(self.player.coins)}", font_size=16, x=20, y=SCREEN_HEIGHT - 115,
                           color=(255, 215, 0, 255))
        coin_label.draw()

        score_label = Label(f"Score: {self.score}", font_size=14, x=20, y=SCREEN_HEIGHT - 85,
                            color=(255, 255, 255, 255))
        score_label.draw()
        
        kills_label = Label(f"Kills: {self.kills}", font_size=14, x=20, y=SCREEN_HEIGHT - 60,
                            color=(255, 255, 255, 255))
        kills_label.draw()

        wave_label = Label(f"Wave: {self.wave}", font_size=14, x=20, y=SCREEN_HEIGHT - 35,
                           color=(255, 255, 0, 255))
        wave_label.draw()
        
        enemy_label = Label(f"Enemies: {len(self.enemies)}", font_size=14, x=20, y=SCREEN_HEIGHT - 10,
                            color=(255, 0, 0, 255))
        enemy_label.draw()

        if self.show_input:
            input_rect = shapes.Rectangle(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 400, 50,
                                          color=BLACK, batch=self.batch)
            input_rect.opacity = 200
            border2 = shapes.Rectangle(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 25, 400, 50,
                                       color=WHITE, batch=self.batch)
            border2.opacity = 150
            
            input_label = Label(self.input_text, font_size=24, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                                anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            input_label.draw()
            
            prompt = Label("Enter enemies (comma separated):", font_size=16,
                           x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2 - 45,
                           anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            prompt.draw()

        if self.game_over:
            self.draw_overlay("GAME OVER", RED, f"Final Score: {self.score}  Kills: {self.kills}")
        elif self.win:
            self.draw_overlay("VICTORY!", GOLD, f"Final Score: {self.score}  Kills: {self.kills}")

    def draw_overlay(self, title: str, color: tuple, score_text: str):
        overlay = shapes.Rectangle(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, color=BLACK, batch=self.batch)
        overlay.opacity = 128
        
        title_label = Label(title, font_size=72, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2 + 20,
                            anchor_x='center', anchor_y='center', color=color)
        title_label.draw()
        
        score_label = Label(score_text, font_size=24, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2 - 40,
                            anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
        score_label.draw()
        
        restart_label = Label("Press R to restart", font_size=16, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2 - 80,
                              anchor_x='center', anchor_y='center', color=(255, 255, 255, 200))
        restart_label.draw()

    def draw_powerups(self):
        for powerup in self.powerups:
            powerup['pulse'] += 0.05
            pulse_effect = abs(math.sin(powerup['pulse']))
            radius = powerup['radius'] + pulse_effect * 3

            color = RED if powerup['type'] == 'health' else CYAN if powerup['type'] == 'energy' else GOLD
            circle = shapes.Circle(powerup['x'], powerup['y'], radius, color=color, batch=self.batch)
            
            border = shapes.Circle(powerup['x'], powerup['y'], radius, color=WHITE, batch=self.batch)
            border.opacity = 100

            icon_text = "❤" if powerup['type'] == 'health' else "⚡" if powerup['type'] == 'energy' else "💰"
            icon = Label(icon_text, font_size=16, x=powerup['x'], y=powerup['y'],
                         anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            icon.draw()

    def draw_player(self):
        color = BLUE if not self.player.invincible else (255, 0, 0)
        circle = shapes.Circle(self.player.x, self.player.y, self.player.radius, color=color, batch=self.batch)
        
        border = shapes.Circle(self.player.x, self.player.y, self.player.radius, color=WHITE, batch=self.batch)
        border.opacity = 150

        eye_offset = 6
        for dx in [-eye_offset, eye_offset]:
            eye = shapes.Circle(self.player.x + dx, self.player.y - 5, 4, color=WHITE, batch=self.batch)
            pupil = shapes.Circle(self.player.x + dx, self.player.y - 5, 2, color=BLACK, batch=self.batch)

        bar_width = 40
        self.draw_health_bar(self.player.x - bar_width // 2, self.player.y + self.player.radius + 5,
                             bar_width, 5, self.player.health, self.player.max_health, RED)

    def draw_enemies(self):
        for enemy in self.enemies:
            circle = shapes.Circle(enemy.x, enemy.y, enemy.radius, color=enemy.color, batch=self.batch)
            border = shapes.Circle(enemy.x, enemy.y, enemy.radius, color=WHITE, batch=self.batch)
            border.opacity = 150

            eye_offset = 4
            for dx in [-eye_offset, eye_offset]:
                eye = shapes.Circle(enemy.x + dx, enemy.y - 5, 3, color=WHITE, batch=self.batch)
                pupil = shapes.Circle(enemy.x + dx, enemy.y - 5, 1, color=RED, batch=self.batch)

            bar_width = 35
            self.draw_health_bar(enemy.x - bar_width // 2, enemy.y - enemy.radius - 12,
                                 bar_width, 4, enemy.health, enemy.max_health, RED)

    def draw_particles(self):
        for particle in self.particles:
            alpha = int(255 * (particle['life'] / 60))
            color = list(particle['color'])
            size = max(1, int(particle['size'] * (particle['life'] / 60)))
            
            circle = shapes.Circle(particle['x'], particle['y'], size,
                                   color=tuple(color), batch=self.batch)
            circle.opacity = alpha

    # RENAME THIS METHOD - was causing the conflict
    def render_game(self):
        # Create a new batch each frame
        self.batch = pyglet.graphics.Batch()
        
        self.draw_background()
        self.draw_powerups()
        self.draw_enemies()
        self.draw_player()
        self.draw_particles()
        self.draw_ui()
        
        if not self.game_over and not self.win:
            controls = Label("SPACE: Attack | E: Boost | T: Custom Attack | ESC: Pause",
                             font_size=14, x=SCREEN_WIDTH // 2, y=20,
                             anchor_x='center', anchor_y='center', color=(255, 255, 255, 200))
            controls.draw()

        if self.paused:
            pause_text = Label("PAUSED", font_size=72, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                               anchor_x='center', anchor_y='center', color=(255, 255, 255, 255))
            pause_text.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.paused = not self.paused
            return

        if self.game_over or self.win:
            if symbol == key.R:
                self.reset_game()
            return

        if symbol == key.SPACE:
            self.attack_nearest_enemy()

        elif symbol == key.E:
            if self.player.boost_energy(10):
                self.player.health = min(self.player.max_health, self.player.health + 20)
                self.score += 5
                self.create_particles(self.player.x, self.player.y, GREEN, 30)
                print("Energy boost used! Health restored.")
            else:
                print("Not enough coins! Need 10 coins.")

        elif symbol == key.T:
            self.show_input = not self.show_input
            self.input_text = ""
            self.input_active = True

        elif symbol == key.ENTER and self.input_active and self.show_input:
            enemies = [e.strip() for e in self.input_text.split(',') if e.strip()]
            if enemies:
                damages = [random.randint(5, 20) for _ in enemies]
                self.player.attack(enemies, damages, True)
                self.score += 5
                self.create_particles(self.player.x, self.player.y, YELLOW, 20)
                print(f"Attacked {len(enemies)} enemies!")
            self.input_text = ""
            self.show_input = False
            self.input_active = False

    def on_text(self, text):
        if self.show_input and self.input_active:
            self.input_text += text

    def attack_nearest_enemy(self):
        if not self.enemies:
            return

        nearest = None
        min_dist = float('inf')
        for enemy in self.enemies:
            dist = math.sqrt((enemy.x - self.player.x) ** 2 + (enemy.y - self.player.y) ** 2)
            if dist < min_dist:
                min_dist = dist
                nearest = enemy

        if nearest and min_dist < 150:
            damage = random.randint(5, 15)
            nearest.health -= damage
            self.create_particles(nearest.x, nearest.y, RED, 15)

            if nearest.health <= 0:
                self.enemies.remove(nearest)
                self.kills += 1
                self.score += 10
                self.player.coins += random.randint(5, 15)
                self.create_particles(nearest.x, nearest.y, GOLD, 30)
                print(f"Killed {nearest.name}! +10 points")

                if len(self.enemies) < self.max_enemies + self.wave:
                    self.spawn_enemies(1)
            else:
                print(f"Hit {nearest.name} for {damage} damage!")

    def reset_game(self):
        self.player = Player("Hero", 100, 100, 50)
        self.enemies = []
        self.particles = []
        self.powerups = []
        self.game_over = False
        self.win = False
        self.score = 0
        self.kills = 0
        self.wave = 1
        self.enemies_spawned = 0

        self.spawn_enemies(3)
        self.spawn_powerups(2)

    def run(self):
        # Event handler for drawing - now calls render_game
        @self.window.event
        def on_draw():
            self.render_game()
        
        @self.window.event
        def on_key_press(symbol, modifiers):
            self.on_key_press(symbol, modifiers)
        
        @self.window.event
        def on_text(text):
            self.on_text(text)

        def update_movement(dt):
            if not self.paused and not self.game_over and not self.win:
                dx, dy = 0, 0
                if self.keys[key.LEFT] or self.keys[key.A]:
                    dx = -1
                if self.keys[key.RIGHT] or self.keys[key.D]:
                    dx = 1
                if self.keys[key.UP] or self.keys[key.W]:
                    dy = 1
                if self.keys[key.DOWN] or self.keys[key.S]:
                    dy = -1

                if dx != 0 and dy != 0:
                    dx *= 0.7071
                    dy *= 0.7071

                self.player.move(dx, dy)
        
        pyglet.clock.schedule(update_movement)
        pyglet.app.run()


def main():
    game = BattleRoyaleGame()
    game.run()


if __name__ == "__main__":
    main()