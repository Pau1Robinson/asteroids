#!/usr/bin/env python3
'''
###########################
#                         #
#     PyGame Asteroids    #
#                         #
###########################
'''
import pygame
import asteroids_var
import asteroids_classes

#### Set everything up ####

# initialise pygame
pygame.init()

#Define the screen, display caption and clock
screen = pygame.display.set_mode((asteroids_var.WIDTH, asteroids_var.HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

#Initialise classes
ship = asteroids_classes.space_ship(512, 384, 270)
bullets = asteroids_classes.bullets()
asteroids = asteroids_classes.asteroids()

#Initialise fonts
my_font = pygame.font.SysFont(asteroids_var.font_name, asteroids_var.font_px)
game_over_font = pygame.font.SysFont(asteroids_var.font_name, 100)

#Declare the varables for tracking the score and state of the ship
score = 0
ship_dead = False

#Declare the bools to track key presses
d_press = False
a_press = False
w_press = False
s_press = False
q_press = False
e_press = False
p_press = False
space_press = False

#### Game loop ####
running = True
while running:

    #FPS limit
    clock.tick(asteroids_var.FPS)
    #### Game loop part 1: Event handling #####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:

            #Set the key presses to True when the key is pressed
            if event.key == pygame.K_d:
                d_press = True
            elif event.key == pygame.K_a:
                a_press = True
            elif event.key == pygame.K_w:
                w_press = True
            elif event.key == pygame.K_s:
                s_press = True
            elif event.key == pygame.K_q:
                q_press = True
            elif event.key == pygame.K_e:
                e_press = True
            elif event.key == pygame.K_SPACE:
                space_press = True
            elif event.key == pygame.K_p:
                p_press = True
        elif event.type == pygame.KEYUP:

            #Set the key presses to False when the key is released
            if event.key == pygame.K_d:
                d_press = False
            if event.key == pygame.K_a:
                a_press = False
            if event.key == pygame.K_w:
                w_press = False
            elif event.key == pygame.K_s:
                s_press = False
            elif event.key == pygame.K_q:
                q_press = False
            elif event.key == pygame.K_e:
                e_press = False

    #### Game loop part 2: Updates #####

    #Checks if the keys are press and call the ship methods if they are
    if e_press is True:
        ship.rotate_right()
    if q_press is True:
        ship.rotate_left()
    if w_press is True:
        ship.move_forward()
    if s_press is True:
        ship.move_backward()
    if d_press is True:
        ship.move_right()
    if a_press is True:
        ship.move_left()
    if p_press is True:
        pygame.image.save(screen, "screenshot.jpg")
    if space_press is True:
        bullets.bullet_fired(ship.shoot())
        space_press = False

    #### Game loop part 3: Draw #####
    screen.fill(asteroids_var.WHITE)

    #Check if the ship is alive
    if ship_dead is False:
        #Draw the ship, bullets and add new asteroids
        ship.draw_ship()
        ship_dead = ship.check_collision(asteroids.list_asteroids)
        bullets.draw_bullets()
        asteroids.add_asteroids()
        score += (asteroids.asteroid_collision(bullets.list_bullets))

    #Draw the asteroids and update the score
    asteroids.draw_asteroids()

    #Check if the ship is dead and show the game over message if it is
    if ship_dead is True:
        game_over_message = game_over_font.render(f'You Died', True, (255, 0, 0))
        screen.blit(game_over_message, (350, 200))

    #Render the fps counter and the score in the top left corner
    fps = my_font.render(str(f'{int(clock.get_fps())} score: {str(score)}'), True, (0,0,0))
    screen.blit(fps, (10, 10))

    # after drawing, make the drawing visible
    pygame.display.flip()

#### Clean up and close program ####
# close the window
pygame.quit()
