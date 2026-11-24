from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x:int, y:int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.
    # in the Player class

    def update(self, dt: float) -> None:
        #saves current keyboard input to a dict
        keys = pygame.key.get_pressed()

        #Updating shoot timer for shoot cooldown handling
        self.shoot_timer -= dt

        # Checks for left or right input
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
                

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

    #Using a Normalized Vector move ahead towards the player current facing direction + speed
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        target_vector = rotated_vector * (PLAYER_SPEED * dt)
        self.position += target_vector

    #Handle shoot input for the Player
    def shoot(self) -> None:
        #Check for shoot cooldown
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        projectile:Shot = Shot(self.position.x, self.position.y)
        projectile.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED