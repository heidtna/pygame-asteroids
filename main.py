# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        # This will quit the program when the 'X' is 
        # clicked on the game window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        #keep near top
        screen.fill("black")
        dt = clock.tick(60) / 1000

        # update player position
        # player.draw(screen)
        # player.update(dt)
        for object in drawable:
            object.draw(screen)

        updatable.update(dt)


        # Always keep this last
        pygame.display.flip()

if __name__ == "__main__":
    main()