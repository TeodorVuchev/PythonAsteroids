from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    #On Death Asteroid Logic
    def split(self) -> None:
        self.kill()
        #Check if it's a small asteroid and dont spawn anything if it is
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        #Calculate Forward Vector for Spawns + Spawn New Asteroids + Make 1.2 faster than parent
        log_event("asteroid_split")
        split_angle:float = random.uniform(20, 50)
        asteroid_forward_1 = self.velocity.rotate(split_angle)
        asteroid_forward_2 = self.velocity.rotate(-split_angle)
        spawned_asteroids_size = self.radius - ASTEROID_MIN_RADIUS
        asteroid_spawn_1:Asteroid = Asteroid(self.position.x, self.position.y, spawned_asteroids_size)
        asteroid_spawn_2:Asteroid = Asteroid(self.position.x, self.position.y, spawned_asteroids_size)
        asteroid_spawn_1.velocity = asteroid_forward_1 * 1.2
        asteroid_spawn_2.velocity = asteroid_forward_2 * 1.2


