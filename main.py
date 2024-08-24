import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player.containers = (updatable, drawable)
        screen.fill((0, 0, 0))
        dt = fps.tick(60) / 1000
        
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        


if __name__ == "__main__":
    main()

