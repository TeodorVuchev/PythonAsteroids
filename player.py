from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x:int, y:int) -> None:
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
    # in the Player class

    def update(self, dt: float) -> None:
        #saves current keyboard input to a dict
        keys = pygame.key.get_pressed()

        # Checks for left or right input
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #Draws the Player Sprite on the Screen Canvas
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    #Updates Player Rotation Value based on DeltaTime and Turn Speed
    def rotate(self, dt: float) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED