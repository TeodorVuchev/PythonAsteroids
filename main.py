import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()

    # The Window Size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player:Player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    
    clock = pygame.time.Clock()
    dt: float = 0.
    while True:
        log_state()
        # returns the event input for this cycle to be processed further
        for event in pygame.event.get():
            # allows the X button on the pop up window to terminate the program
            if event.type == pygame.QUIT:
                return

        #Check for Player Updates
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        #saves delta time, time that has past since last frame
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
