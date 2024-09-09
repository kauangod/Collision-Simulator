import pygame 
import numpy as np

FPS = 360
SCREEN_WIDTH = 1366 
SCREEN_HEIGHT = 768

class Circle:
    def __init__(self, rad, pos, vel, mass, screen):
        self.clr = "black"
        self.rad = rad 
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.screen = screen
    def overlaps (self, another_circle, distance):    
        overlap = self.rad + another_circle.rad - distance
        direction = (self.pos - another_circle.pos) / distance
        self.pos += direction * overlap / 2
        another_circle.pos -= direction * overlap / 2
    def check_collision (self, another_circle):
        distance = np.sqrt((self.pos[0] - another_circle.pos[0])**2 + (self.pos[1] - another_circle.pos[1])**2)
        if (distance <= (2 * self.rad)):
            self.overlaps(another_circle, distance)
            sum_mass = self.mass + another_circle.mass
            v_diff = np.array([self.vel[0] - another_circle.vel[0], self.vel[1] - another_circle.vel[1]])
            n_divisor = np.linalg.norm(self.pos - another_circle.pos)
            n = np.array([(self.pos[0] - another_circle.pos[0])/n_divisor, (self.pos[1] - another_circle.pos[1])/n_divisor])
            n2 = np.array([(another_circle.pos[0] - self.pos[0])/n_divisor, (another_circle.pos[1] - self.pos[1])/n_divisor])
            self.vel -= 2 * another_circle.mass * np.dot(v_diff, n) * n / sum_mass
            another_circle.vel -= 2 * self.mass * np.dot(-v_diff, n2) * n2 / sum_mass
        self.update_position()
        another_circle.update_position()
    def update_position(self):
        self.limit_screen()
        dt = 1/FPS # Time between frames
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
        self.draw()
    def limit_screen(self):
        LIMIT_X = SCREEN_WIDTH - self.rad 
        LIMIT_Y = SCREEN_HEIGHT - self.rad  
        if self.pos[0] <= self.rad + 1 or self.pos[0] >= LIMIT_X - 1:
            self.vel[0] = -self.vel[0]
        elif self.pos[1] <= self.rad + 1 or self.pos[1] >= LIMIT_Y - 1:
            self.vel[1] = -self.vel[1]  
    def draw(self):
        pygame.draw.circle(self.screen, self.clr, pygame.Vector2(self.pos[0], self.pos[1]) ,self.rad)