'''
Contains the classes for the player's space ship,\n
tracking and drawing the asteroids and the bullets fired by the player
'''
import random
import math
import sys
import pygame
import asteroids_var

screen = pygame.display.set_mode((asteroids_var.WIDTH, asteroids_var.HEIGHT))

class space_ship:
    '''
    Class to define the player controlled ship\n

    Variables\n
    angle: Int to track the angle the ship is facing in degrees\n
    x_pos,y_pos: x,y to track the middle of the ship also the point the ship rotates around\n
    x_top,y_top: x,y to track the top of the polygon used to draw the ship\n
    X_bottom,y_bottom: x,y for the bottom of the ship used to calculate the corners of the ship\n
    X_right_corner,y_right_corner: x,y for the right corner of the ship\n
    X_left_corner,y_left_corner: x,y for the right corner of the ship\n

    Methods\n
    draw_ship: handles the drawing of the ship and collision checking with the asteroids\n
    rotate_right: rotates the ship right by changing space_ship.angle\n
    rotate_left: rotates the ship left by changing space_ship.angle\n
    move_forward: moves the ships x,y forward by 5px\n
    move_backward: moves the ships x,y backward by 5px\n
    move_right: moves the ships x,y right by 5px\n
    move_left: moves the ships x,y left by 5px\n
    '''
    def __init__(self, x_pos, y_pos, angle):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.angle = angle
        self.x_top = self.x_pos + math.cos(math.radians(self.angle)) * 20
        self.y_top = self.y_pos + math.sin(math.radians(self.angle)) * 20
        self.x_bottom = self.x_pos + math.cos(math.radians(180 + self.angle)) * 10
        self.y_bottom = self.y_pos + math.sin(math.radians(180 + self.angle)) * 10
        self.x_right_corner = self.x_bottom + math.cos(math.radians(90 + self.angle)) * 10
        self.y_right_corner = self.y_bottom + math.sin(math.radians(90 + self.angle)) * 10
        self.x_left_corner = self.x_bottom - math.cos(math.radians(90 + self.angle)) * 10
        self.y_left_corner = self.y_bottom - math.sin(math.radians(90 + self.angle)) * 10

    def draw_ship(self):
        '''
        Draws the players ship from x_pos and y_pos
        x_top, y-top: cords for the top of the polygon
        X_bottom, y_bottom: cords for the bottom of the polygon
        X_right_corner, y_right_corner: cords for the bottom of the polygon
        X_left_corner, y_left_corner: cords for the bottom of the polygon
        '''
        #Calculates the top of the polygon as a point 20px from x_pos, y_pos in a line
        self.x_top = self.x_pos + math.cos(math.radians(self.angle)) * 20
        self.y_top = self.y_pos + math.sin(math.radians(self.angle)) * 20

        #Calculates the bottom of the polygon as a point 10px from x_pos, y_pos in a 180 angle away from x_top, y_top
        self.x_bottom = self.x_pos + math.cos(math.radians(180 + self.angle)) * 10
        self.y_bottom = self.y_pos + math.sin(math.radians(180 + self.angle)) * 10

        #Calculates the right corner of the polygon as a point 10px from x_bottom, y_bottom at a 90 angle
        self.x_right_corner = self.x_bottom + math.cos(math.radians(90 + self.angle)) * 10
        self.y_right_corner = self.y_bottom + math.sin(math.radians(90 + self.angle)) * 10

        #Calculates the right corner of the polygon as a point 10px from x_bottom, y_bottom at a 270 angle
        self.x_left_corner = self.x_bottom - math.cos(math.radians(90 + self.angle)) * 10
        self.y_left_corner = self.y_bottom - math.sin(math.radians(90 + self.angle)) * 10

        #Cobines the cords of the polygon into a list and draws the polygon
        poly_cords = [(self.x_top, self.y_top), (self.x_right_corner, self.y_right_corner), (self.x_left_corner, self.y_left_corner)]
        pygame.draw.polygon(screen, (0, 0, 0), poly_cords, 2)

        #Checks for collision with the asteroids and returns a bool to determine if the ship has crashed

    def check_collision(self, list_asteroids):
        '''
        Iterates through the list_asteroids and checks each corner of the ship\n
        if it has collided with an asteroid
        '''
        asteroid_collision = False
        for asteroid in list_asteroids:

            #Checks for collision with the top of the ship
            if ((round(self.x_top) - round(asteroid[0])) ** 2 + (round(self.y_top) - round(asteroid[1])) ** 2) < (asteroid[4] ** 2):
                print(f'ship.top collision X:{self.x_top} Y:{self.y_top} detected')
                asteroid_collision = True
                asteroid[5] = (255, 0, 0)

            #Checks for collision with the right corner of the ship
            if ((round(self.x_right_corner) - round(asteroid[0])) ** 2 + (round(self.y_right_corner) - round(asteroid[1])) ** 2) < (asteroid[4] ** 2):
                print(f'ship.right_corner collision X:{self.x_right_corner} Y:{self.y_right_corner} detected')
                asteroid_collision = True
                asteroid[5] = (255, 0, 0)

            #Check for collision with the left corner of the ship
            if ((round(self.x_left_corner) - round(asteroid[0])) ** 2 + (round(self.y_left_corner) - round(asteroid[1])) ** 2) < (asteroid[4] ** 2):
                print(f'ship.left_corner collision X:{self.x_left_corner} Y:{self.y_left_corner} detected')
                asteroid_collision = True
                asteroid[5] = (255, 0, 0)
        return(asteroid_collision)

    def rotate_right(self):
        '''
        Rotates the ship 5 degrees to the right
        '''
        self.angle += 5

    def rotate_left(self):
        '''
        Rotates the ship 5 degrees to the left
        '''
        self.angle -= 5

    def move_forward(self):
        '''
        Move the x_pos, y_pos forward by 5px
        '''
        self.x_pos = self.x_pos + math.cos(math.radians(self.angle)) * 5
        self.y_pos = self.y_pos + math.sin(math.radians(self.angle)) * 5

    def move_backward(self):
        '''
        Move the x_pos, y_pos backward by 5px
        '''
        self.x_pos = self.x_pos + math.cos(math.radians(180 + self.angle)) * 5
        self.y_pos = self.y_pos + math.sin(math.radians(180 + self.angle)) * 5

    def move_right(self):
        '''
        Move the x_pos, y_pos right by 5px
        '''
        self.x_pos = self.x_pos + math.cos(math.radians(90 + self.angle)) * 5
        self.y_pos = self.y_pos + math.sin(math.radians(90 + self.angle)) * 5

    def move_left(self):
        '''
        Move the x_pos, y_pos left by 5px
        '''
        self.x_pos = self.x_pos - math.cos(math.radians(90 + self.angle)) * 5
        self.y_pos = self.y_pos - math.sin(math.radians(90 + self.angle)) * 5

    def shoot(self):
        '''
        Calls bullet_fired method with the x,y from the top of the ship\n
        and the angle the bullet was fired at.
        '''
        return self.x_top, self.y_top, self.angle

class bullets:
    '''
    Handles the cords and drawing of the bullets that have been fired\n

    Variables\n
    list_bullets: A list of the bullets currently on the screen\n

    Methods\n
    bullet_fired: Add a new bullet to the list of bullet getting the values for x,y and angles\n
    draw_bullets: Draws the bullets from list_bullets and removes the ones that leave the screen\n
    '''
    def __init__(self):
        self.list_bullets = []

    def bullet_fired(self, bullet):
        '''
        Adds a new bullet to list_bullets with its cords and the angle it was fired at
        '''
        self.list_bullets.append([bullet[0], bullet[1], bullet[2]])

    def draw_bullets(self):
        '''
        draw_bullets: Draws the bullets from list_bullets and removes the ones that leave the screen
        '''
        for bullet in self.list_bullets:
            #draws the bullet
            pygame.draw.circle(screen, (0, 0, 0), (round(bullet[0]), round(bullet[1])), 3)

            #Moves the cords of each bullet 10px
            bullet[0] = bullet[0] + math.cos(math.radians(bullet[2])) * 20
            bullet[1] = bullet[1] + math.sin(math.radians(bullet[2])) * 20

            #Removes bullets that leave the screen
            if (bullet[0] < 0 or bullet[0] > 1024 or bullet[1] < 0 or bullet[1] > 768):
                self.list_bullets.remove(bullet)

class asteroids:
    '''
    Handles the cords and drawing of the asteroids
    '''
    def __init__(self):
        self.list_asteroids = []
        self.time_add_asteroid = 1

    def create_asteroids(self):
        '''
        Adds 10 asteroids to list_asteroids 100px away from the ship start point and 50 from the border of the window.\n
        Gives them random cords, direction, speed and size.
        '''
        for i in range(1, 6):
            self.list_asteroids.append(
                [random.randrange(50, 412), random.randrange(50, 284),
                random.randrange(0, 360), random.randrange(1, 5), 20])
            self.list_asteroids.append(
                [random.randrange(612, 974), random.randrange(484, 718),
                random.randrange(0, 360), random.randrange(1, 5), 20])

    def draw_asteroids(self):
        score = 0
        for asteroid in self.list_asteroids:
            #Draws the asteroids using asteroid[0] as x, asteroid[1] as y and asteroid[4] as radius
            pygame.draw.circle(screen, asteroid[5], (round(asteroid[0]), round(asteroid[1])), asteroid[4])

            #Moves the cords of the asteroids a number of px the speed of movement in asteroid[3]
            asteroid[0] = asteroid[0] + math.cos(math.radians(asteroid[2])) * asteroid[3]
            asteroid[1] = asteroid[1] + math.sin(math.radians(asteroid[2])) * asteroid[3]

            #Removes asteroids that leave the screen
            if (asteroid[0] < 0 or asteroid[0] > 1024 or asteroid[1] < 0 or asteroid[1] > 768):
                self.list_asteroids.remove(asteroid)

    def asteroid_collision(self, list_bullets):
        '''
        Checks for collisions between the bullets and asteroids\n
        If a collision happens removes the asteroid from list_asteroids\n
        and updates the score.
        '''
        score = 0
        for asteroid in self.list_asteroids:
            bullet_collision = False
            for bullet in list_bullets:
                if ((round(bullet[0]) - round(asteroid[0])) ** 2 + (round(bullet[1]) - round(asteroid[1])) ** 2) < (asteroid[4] ** 2):
                    bullet_collision = True
            if bullet_collision is True:
                self.list_asteroids.remove(asteroid)
                score += 1
        return score

    def add_asteroids(self):
        '''
        Picks a random amount of frames until an asteroid is added to list_asteroids.\n
        When the time is meet, adds an asteroid to list_asteroids,\n
        that starts at a random side of the screen and travels invards.
        '''
        self.time_add_asteroid -= 1
        if self.time_add_asteroid == 0:
            side_picked = random.randrange(1,5)
            if side_picked == 1:
                self.list_asteroids.append(
                    [10, random.randrange(50, 718),
                    random.randrange(270, 450), random.randrange(1, 5), 20, (0, 0, 0)])
            if side_picked == 2:
                self.list_asteroids.append(
                    [random.randrange(50, 974), 10,
                    random.randrange(0, 180), random.randrange(1, 5), 20, (0, 0, 0)])
            if side_picked == 3:
                self.list_asteroids.append(
                    [1014, random.randrange(50, 718),
                    random.randrange(90, 270), random.randrange(1, 5), 20, (0, 0, 0)])
            if side_picked == 4:
                self.list_asteroids.append(
                    [random.randrange(50, 974), 758,
                    random.randrange(180, 360), random.randrange(1, 5), 20, (0, 0, 0)])
            self.time_add_asteroid = random.randrange(5, 20)