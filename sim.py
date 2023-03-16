import pygame
import numpy as np
import calculation

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDING = 50
PEN_RADIUS = 10
PEN_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)

def render_pendulum_chain(lengths, masses, initial_angles, time_step, total_time):
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Simulation loop
    for thetas, omegas, energy in calculation.simulate_pendulum_chain(lengths, masses, initial_angles, time_step, total_time):
        # Clear screen
        screen.fill(BACKGROUND_COLOR)

        # Draw pendulums
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        for i in range(len(thetas)):
            angle = thetas[i]
            length = lengths[i] * 50
            px = x + length * np.sin(angle)
            py = y + length * np.cos(angle)
            pygame.draw.line(screen, PEN_COLOR, (x, y), (px, py), PEN_RADIUS)
            pygame.draw.circle(screen, PEN_COLOR, (int(px), int(py)), PEN_RADIUS)

            # Update position
            x = px
            y = py

        # Update screen
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Limit frame rate
        clock.tick(60)

    # Quit pygame
    pygame.quit()

