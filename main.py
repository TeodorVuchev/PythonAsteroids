import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from logger import log_event
import sys

def main():
    pygame.init()
    #Setting up all Groups to be utilized By Entities
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # The Window Size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Assigning Groups for Each Game Entity
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, shots, drawable)

    #Spawning initial Entities
    player:Player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroid_field:AsteroidField = AsteroidField()
    
    clock = pygame.time.Clock()
    dt: float = 0.
    while True:
        log_state()
        # returns the event input for this cycle to be processed further
        for event in pygame.event.get():
            # allows the X button on the pop up window to terminate the program
            if event.type == pygame.QUIT:
                return

        #Check for all Player Entity Updates and Executes
        updatable.update(dt)

        #Check if Player is colliding with any Asteroids and act if he is
        for sprite in asteroids:
            if player.collides_with(sprite):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        #Checks for all Player Entity draws and Executes
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        #saves delta time, time that has past since last frame
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
