import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    fps = pygame.time.Clock()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)    
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0  


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player.containers = (updatable, drawable)
        screen.fill((0, 0, 0))
        dt = fps.tick(60) / 1000
        
        for sprite in updatable:
            sprite.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        


if __name__ == "__main__":
    main()

