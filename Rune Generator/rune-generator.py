from typing import Any
import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 3
GRID_SPACING = 100
SPOT_SIZE = 10
LINE_THICKNESS = 20

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Drawing")

class Dot:

    def __init__(self, x, y, radius=SPOT_SIZE, color=BLACK) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

class Line:

    def __init__(self, start, end, width):

        self.start = start
        self.end = end
        self.width = width

    def draw(self):

        pygame.draw.line(screen, BLACK, self.start, self.end, self.width)
        pygame.draw.circle(screen, BLACK, self.start, self.width/2)
        pygame.draw.circle(screen, BLACK, self.end, self.width/2)

class Arc:

    def __init__(self, center, radius, start, end, width) -> None:
        self.center = center
        self.start = start
        self.end = end
        self.radius = radius
        self.width = width

    def draw(self):

        pygame.draw.arc(screen, BLACK, pygame.Rect(self.center.x-GRID_SPACING*self.radius-self.width/2, self.center.y -
                        GRID_SPACING*self.radius-self.width/2, 2*GRID_SPACING*self.radius+self.width, 2*GRID_SPACING*self.radius+self.width), self.start*math.pi/4, self.end*math.pi/4, self.width)

grid = []

dots = []
lines = []
arcs = []

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        grid.append(Dot(GRID_SPACING * (col+1),
                        GRID_SPACING * (row+1), SPOT_SIZE, GRAY))

# Draw the grid
def draw_grid():
    screen.fill(WHITE)

    for griddot in grid:
        griddot.draw()
    for dot in dots:
        dot.draw()
    for line in lines:
        line.draw()
    for arc in arcs:
        arc.draw()
        arc.draw()
    
    

# Draw thick lines and circles on the grid
def create_line(start, end):
    lines.append(Line((start.x, start.y), (end.x, end.y), LINE_THICKNESS))

create_line(grid[7], grid[8])
create_line(grid[8], grid[5])

arcs.append(Arc(grid[4], 1, 2, 6, LINE_THICKNESS))
dots.append(Dot(grid[2].x, grid[2].y))


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the grid
    draw_grid()

    # Draw thick lines and circles on specific spots
    # draw_on_grid(1, 1)
    # draw_on_grid(2, 0)
    # draw_on_grid(0, 2)

    # Update the screen
    pygame.display.flip()

# Quit the program
pygame.quit()