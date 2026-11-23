import pygame
import constants
from logger import log_state

def main():
    pygame.init()
    
    # The Window Size
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt: float = 0.
    while True:
        log_state()
        # returns the event input for this cycle to be processed further
        for event in pygame.event.get():
            # allows the X button on the pop up window to terminate the program
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()

        #saves delta time, time that has past since last frame
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
