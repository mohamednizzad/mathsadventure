import pygame
import sys
from game import Game

def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()
    
    # Set up the display
    WINDOW_SIZE = (800, 600)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Math Adventure - Developed by M.N.F. Zahra - Grade 05 - KM/KM/G.M.M. School")
    
    # Create game instance
    game = Game(screen)
    
    # Main game loop
    while True:
        game.handle_events()
        game.update()
        game.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()