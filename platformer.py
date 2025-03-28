import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Initialize Pygame mixer for sounds
pygame.mixer.init()

# Load sounds
jump_sound = pygame.mixer.Sound("jump.ogg")  # Path to jump sound file
pygame.mixer.Sound.set_volume(jump_sound, 0.8)  # Set volume (0.0 to 1.0)
goal_sound = pygame.mixer.Sound("goal.ogg")  # Path to goal sound file
pygame.mixer.Sound.set_volume(goal_sound, 4.0)  # Set volume (0.0 to 1.0)

# Load background music
pygame.mixer.music.load("game-music-player-console-8bit-background-intro-theme-297305.mp3")  # Path to background music file
pygame.mixer.music.set_volume(0.6)  # Set volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Play music in a loop

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Default window size
BASE_WIDTH, BASE_HEIGHT = 800, 600      # Base resolution for rendering
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Allow resizing
base_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player properties
player = pygame.Rect(100, 500, 50, 50)
player_speed = 5
player_velocity_y = 0
gravity = 0.5
jump_strength = -10
on_ground = False
can_double_jump = True
jump_pressed = False

# Levels configuration
levels = [
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(500, 550, 300, 50),  # Ground (right side)
            pygame.Rect(350, 450, 100, 20)   # Floating platform in the middle
        ],
        "goal": pygame.Rect(750, 500, 50, 50)  # Positioned on the right ground
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(500, 550, 300, 50),  # Ground (right side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Additional platform on the left
            pygame.Rect(600, 400, 100, 20)   # Additional platform on the right
        ],
        "goal": pygame.Rect(650, 350, 50, 50)  # Positioned on the right platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(400, 450, 150, 20),  # First platform on the right
            pygame.Rect(200, 350, 150, 20),  # Second platform on the left
            pygame.Rect(500, 250, 150, 20),  # Third platform on the right
            pygame.Rect(100, 150, 150, 20)   # Fourth platform on the left
        ],
        "goal": pygame.Rect(150, 100, 50, 50)  # Positioned on the fourth left platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 800, 50),    # Ground
            pygame.Rect(300, 450, 200, 20),  # Wide platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(100, 350, 150, 20)   # Platform on the left
        ],
        "goal": pygame.Rect(650, 300, 50, 50)  # Positioned on the right platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(500, 550, 300, 50),  # Ground (right side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Platform on the left
            pygame.Rect(600, 400, 100, 20),  # Platform on the right
            pygame.Rect(350, 300, 100, 20)   # Higher platform in the middle
        ],
        "goal": pygame.Rect(350, 250, 50, 50)  # Positioned on the top platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Platform on the left
            pygame.Rect(600, 400, 100, 20),  # Platform on the right
            pygame.Rect(100, 300, 100, 20),  # Higher platform on the left
            pygame.Rect(700, 300, 100, 20)   # Higher platform on the right
        ],
        "goal": pygame.Rect(700, 250, 50, 50)  # Positioned on the right top platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 800, 50),    # Ground
            pygame.Rect(300, 450, 200, 20),  # Wide platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(100, 350, 150, 20),  # Platform on the left
            pygame.Rect(400, 250, 100, 20)   # Platform at the top middle
        ],
        "goal": pygame.Rect(400, 200, 50, 50)  # Positioned on the top middle platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(500, 550, 300, 50),  # Ground (right side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Platform on the left
            pygame.Rect(600, 400, 100, 20),  # Platform on the right
            pygame.Rect(350, 300, 100, 20),  # Higher platform in the middle
            pygame.Rect(350, 200, 100, 20)   # Top platform in the middle
        ],
        "goal": pygame.Rect(350, 150, 50, 50)  # Positioned on the top platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Platform on the left
            pygame.Rect(600, 400, 100, 20),  # Platform on the right
            pygame.Rect(350, 300, 100, 20),  # Higher platform in the middle
            pygame.Rect(100, 250, 100, 20),  # Top-left platform
            pygame.Rect(600, 250, 100, 20)   # Top-right platform
        ],
        "goal": pygame.Rect(600, 200, 50, 50)  # Positioned on the top-right platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 800, 50),    # Ground
            pygame.Rect(300, 450, 200, 20),  # Wide platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(100, 350, 150, 20),  # Platform on the left
            pygame.Rect(400, 250, 100, 20)   # Platform at the top middle
        ],
        "goal": pygame.Rect(400, 200, 50, 50)  # Positioned on the top middle platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(400, 450, 150, 20),  # Platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(200, 250, 150, 20)   # Platform on the left
        ],
        "goal": pygame.Rect(200, 200, 50, 50)  # Positioned on the left platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 800, 50),    # Ground
            pygame.Rect(300, 450, 200, 20),  # Wide platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(100, 350, 150, 20),  # Platform on the left
            pygame.Rect(400, 250, 100, 20)   # Platform at the top middle
        ],
        "goal": pygame.Rect(400, 200, 50, 50)  # Positioned on the top middle platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(500, 550, 300, 50),  # Ground (right side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Platform on the left
            pygame.Rect(600, 400, 100, 20),  # Platform on the right
            pygame.Rect(350, 300, 100, 20),  # Higher platform in the middle
            pygame.Rect(350, 200, 100, 20)   # Top platform in the middle
        ],
        "goal": pygame.Rect(350, 150, 50, 50)  # Positioned on the top platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(500, 550, 300, 50),  # Ground (right side)
            pygame.Rect(350, 450, 100, 20),  # Floating platform in the middle
            pygame.Rect(200, 400, 100, 20),  # Platform on the left
            pygame.Rect(600, 400, 100, 20),  # Platform on the right
            pygame.Rect(350, 300, 100, 20),  # Higher platform in the middle
            pygame.Rect(100, 250, 100, 20),  # Top-left platform
            pygame.Rect(600, 250, 100, 20)   # Top-right platform
        ],
        "goal": pygame.Rect(600, 200, 50, 50)  # Positioned on the top-right platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 800, 50),    # Ground
            pygame.Rect(300, 450, 200, 20),  # Wide platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(100, 350, 150, 20),  # Platform on the left
            pygame.Rect(400, 250, 100, 20)   # Platform at the top middle
        ],
        "goal": pygame.Rect(400, 200, 50, 50)  # Positioned on the top middle platform
    },
    {
        "platforms": [
            pygame.Rect(0, 550, 300, 50),    # Ground (left side)
            pygame.Rect(400, 450, 150, 20),  # Platform in the middle
            pygame.Rect(600, 350, 150, 20),  # Platform on the right
            pygame.Rect(200, 250, 150, 20)   # Platform on the left
        ],
        "goal": pygame.Rect(200, 200, 50, 50)  # Positioned on the left platform
    }
]

current_level = 0

# Controller setup
joystick = None
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

def render_text(surface, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    rendered_text = font.render(text, True, color)
    surface.blit(rendered_text, (x, y))

def options_menu():
    while True:
        base_surface.fill(WHITE)
        render_text(base_surface, "Options Menu", 48, BLACK, BASE_WIDTH // 2 - 100, 100)
        render_text(base_surface, "Press B to Go Back", 36, BLACK, BASE_WIDTH // 2 - 100, 200)

        screen.blit(pygame.transform.scale(base_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if joystick:
                if joystick.get_button(1):  # Button 1 = "B"
                    return

def main_menu():
    while True:
        base_surface.fill(WHITE)
        render_text(base_surface, "Press A to Start", 48, BLACK, BASE_WIDTH // 2 - 100, 200)
        render_text(base_surface, "Press Y to Quit Game", 36, BLACK, BASE_WIDTH // 2 - 100, 300)

        screen.blit(pygame.transform.scale(base_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if joystick:
                if joystick.get_button(0):  # Button 0 = "A"
                    return
                elif joystick.get_button(3):  # Button 3 = "Y"
                    pygame.quit()
                    exit()

def end_menu():
    while True:
        base_surface.fill(WHITE)
        render_text(base_surface, "Congratulations! Press Y to Exit", 48, BLACK, BASE_WIDTH // 2 - 200, BASE_HEIGHT // 2)

        screen.blit(pygame.transform.scale(base_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if joystick and joystick.get_button(3):  # Button 3 = "Y"
                pygame.quit()
                exit()

# Main game loop
main_menu()

while current_level < len(levels):
    level_data = levels[current_level]
    platforms = level_data["platforms"]
    goal = level_data["goal"]

    # Reset player position
    player.x, player.y = 100, 500
    player_velocity_y = 0

    running = True
    while running:
        base_surface.fill(WHITE)

        # Display level counter
        render_text(base_surface, f"Level: {current_level + 1}", 36, BLACK, 10, 10)

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        # Player movement
        move_x = 0
        if joystick:
            move_x = joystick.get_axis(0) * player_speed
            if joystick.get_button(0):  # Button 0 for jump
                if not jump_pressed:
                    if on_ground:
                        player_velocity_y = jump_strength
                        can_double_jump = True
                        jump_sound.play()  # Play jump sound
                    elif can_double_jump:
                        player_velocity_y = jump_strength
                        can_double_jump = False
                        jump_sound.play()  # Play jump sound
                jump_pressed = True
            else:
                jump_pressed = False

        player.x += move_x

        # Prevent player from going outside screen boundaries
        if player.left < 0:
            player.left = 0
        if player.right > BASE_WIDTH:
            player.right = BASE_WIDTH

        # Gravity
        player_velocity_y += gravity
        player.y += player_velocity_y

        # Restart level if player falls below the screen
        if player.top > BASE_HEIGHT:
            render_text(base_surface, "You Fell! Restarting Level...", 36, BLACK, BASE_WIDTH // 2 - 150, BASE_HEIGHT // 2)
            screen.blit(pygame.transform.scale(base_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)
            player.x, player.y = 100, 500
            player_velocity_y = 0
            continue

        # Collision with platforms
        on_ground = False
        for platform in platforms:
            if player.colliderect(platform) and player_velocity_y > 0:
                player.bottom = platform.top
                player_velocity_y = 0
                on_ground = True
                can_double_jump = True

        # Check if player reaches the goal
        if player.colliderect(goal):
            goal_sound.play()  # Play goal sound
            render_text(base_surface, "Level Complete!", 36, BLACK, BASE_WIDTH // 2 - 100, BASE_HEIGHT // 2)
            screen.blit(pygame.transform.scale(base_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)
            current_level += 1
            running = False

        # Draw platforms
        for platform in platforms:
            pygame.draw.rect(base_surface, BLACK, platform)

        # Draw goal
        pygame.draw.rect(base_surface, GREEN, goal)

        # Draw player
        pygame.draw.rect(base_surface, BLUE, player)

        # Scale and display
        screen.blit(pygame.transform.scale(base_surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()
        clock.tick(60)

# Show end menu after completing all levels
end_menu()
pygame.quit()
