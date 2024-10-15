import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
colors = {
    "Mercury": (169, 169, 169),  # Dark Gray
    "Venus": (255, 204, 0),      # Yellow
    "Earth": (0, 102, 204),      # Blue
    "Mars": (255, 99, 71),       # Tomato
    "Jupiter": (255, 165, 0),    # Orange
    "Saturn": (210, 180, 140),   # Tan
    "Uranus": (135, 206, 235),   # Light Blue
    "Neptune": (0, 0, 128),      # Navy
}

# Planet data with increased size
planet_data = [
    {"name": "Mercury", "distance": 70, "size": 12},
    {"name": "Venus", "distance": 100, "size": 16},
    {"name": "Earth", "distance": 130, "size": 16},
    {"name": "Mars", "distance": 160, "size": 12},
    {"name": "Jupiter", "distance": 200, "size": 24},
    {"name": "Saturn", "distance": 240, "size": 20},
    {"name": "Uranus", "distance": 280, "size": 16},
    {"name": "Neptune", "distance": 320, "size": 16},
]

# Sun position and size
sun_pos = (width // 2, height // 2)
sun_size = 60  # Increased sun size

# Function to draw a starry sky background
def draw_starry_background():
    screen.fill(black)  # Fill background with black
    for _ in range(200):  # Draw 200 stars
        star_size = random.randint(1, 3)  # Random size for stars
        x = random.randint(0, width)
        y = random.randint(0, height)
        pygame.draw.circle(screen, white, (x, y), star_size)  # Small stars

# Function to draw the shining sun
def draw_sun():
    # Draw glowing effect
    for i in range(10, 0, -1):  # Create multiple circles for glow
        pygame.draw.circle(screen, (255, 255, 0, i * 25), sun_pos, sun_size + i)  # Sun color and size
    pygame.draw.circle(screen, (255, 255, 0), sun_pos, sun_size)  # Draw the sun

# Function to draw planets in a circular orbit
def draw_planets(angle):
    for planet in planet_data:
        # Calculate planet position
        x = sun_pos[0] + planet["distance"] * math.cos(angle / (planet["distance"] / 100))  
        y = sun_pos[1] + planet["distance"] * math.sin(angle / (planet["distance"] / 100))

        # Draw the planet
        pygame.draw.circle(screen, colors[planet["name"]], (int(x), int(y)), planet["size"])

        # Draw planet name
        font = pygame.font.Font(None, 24)
        text = font.render(planet["name"], True, white)
        text_rect = text.get_rect(center=(int(x), int(y) + planet["size"] + 10))
        screen.blit(text, text_rect)

        # Draw orbit line
        pygame.draw.circle(screen, white, sun_pos, planet["distance"], 1)  # Draw the orbit line

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the starry background
    draw_starry_background()
    
    # Draw the sun
    draw_sun()
    
    # Draw the planets
    draw_planets(angle)

    # Update angle for planet movement
    angle += 0.05  # Adjust speed of planet movement

    # Update the display
    pygame.display.flip()
    pygame.time.delay(30)  # Delay for smooth animation

# Quit Pygame
pygame.quit()
#second code