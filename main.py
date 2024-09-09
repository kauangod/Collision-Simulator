import pygame
import numpy as np
from circle import Circle

def main():
    SCREEN_WIDTH = 1366
    SCREEN_HEIGHT = 768 # Defines
    LIMIT = 1335
    FPS = 360
        
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption ("Collision Simulation")
    clock = pygame.time.Clock()
    running = True
    list_circles = []
    
    while True:
        user_input = input("How many circles do you want in your simulation? Choose a number less than or equal to 30\n")
        try:
            nmb_circles = int(user_input)
            if nmb_circles >= 31:
                print("Please choose a number less than or equal to 30.")
            elif nmb_circles >= 0:
                break
        except (ValueError, TypeError):
            print("Invalid input. Please enter a valid integer.")
    
    rad = 10
    position = np.array ([2 * rad + 1, 2 * rad + 1], dtype=np.float32)
    
    mass = 0.15
    i = 0
    k = 0
    j = 0
    if nmb_circles <= 3:
        velocity = np.array([24 * rad, 24 * rad], dtype=np.float32)
    elif nmb_circles >= 15:
        velocity = np.array([rad/8, rad/8], dtype=np.float32)
    else:
        velocity = np.array([rad/2, rad/2], dtype=np.float32)
    for circle in range (nmb_circles):
        list_circles.append(Circle(rad, position.copy(), velocity.copy(), mass, screen))
        position[0] += 40
        if position[0] >= LIMIT:
            position[0] = 2 * rad + 1
            position[1] += 40
        if k % 2 == 0:
            i += (0.05 + mass)/512.0
            j += 0.05
        else:
            i -= (0.05 + mass)/1024.0
            j -= 0.25
        k += 1
        mass += i
        velocity += j
        

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        screen.fill("white")
        
        if nmb_circles != 1:
            for i, circle in enumerate(list_circles):
                for j, another_circle in enumerate(list_circles):
                    if i!= j:
                        circle.check_collision(another_circle)
        else:
            list_circles[0].update_position()
        pygame.display.flip()
        clock.tick(FPS)  
    exit()
if __name__ == "__main__":
    main()