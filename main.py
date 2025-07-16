# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") 

        for asteroid in asteroid_group:
            for bullet in shot_group:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()

        for asteroid in asteroid_group:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        updatable_group.update(dt)
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()  
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    
    main()

