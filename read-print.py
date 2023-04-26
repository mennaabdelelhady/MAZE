import pygame
from collections import deque

# Define the maze as a 2D array of integers
maze = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Define the maze cell size and colors
CELL_SIZE = 50
WALL_COLOR = pygame.Color('black')
OPEN_COLOR = pygame.Color('white')
START_COLOR = pygame.Color('green')
END_COLOR = pygame.Color('red')
PATH_COLOR = pygame.Color('blue')

# Define the starting and ending positions
start = (0, 0)
end = (4, 4)

# Define the four possible movements
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Initialize pygame
pygame.init()

# Create the maze surface
maze_surface = pygame.Surface((CELL_SIZE * len(maze), CELL_SIZE * len(maze[0])))

# Draw the maze on the maze surface
for i in range(len(maze)):
    for j in range(len(maze[0])):
        rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if maze[i][j] == 0:
            pygame.draw.rect(maze_surface, OPEN_COLOR, rect)
        else:
            pygame.draw.rect(maze_surface, WALL_COLOR, rect)

# Draw the start and end positions on the maze surface
pygame.draw.rect(maze_surface, START_COLOR, pygame.Rect(start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
pygame.draw.rect(maze_surface, END_COLOR, pygame.Rect(end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Create the screen
screen = pygame.display.set_mode((CELL_SIZE * len(maze), CELL_SIZE * len(maze[0])))

# Initialize the clock
clock = pygame.time.Clock()

# Define a queue for BFS
queue = deque()
queue.append(start)

# Define a dictionary to store the previous position for each position
prev = {}
prev[start] = None

# Implement BFS
while queue:
    current = queue.popleft()
    if current == end:
        break
    for move in moves:
        neighbor = (current[0] + move[0], current[1] + move[1])
        if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == 0 and neighbor not in prev:
            prev[neighbor] = current
            queue.append(neighbor)

# Trace the path from the end position to the start position
path = []
if end in prev:
    current = end
    while current != start:
        path.append(current)
        current = prev[current]
    path.append(start)
    path.reverse()

# Draw the path on the maze surface
for i in range(len(path)):
    pygame.draw.rect(maze_surface, PATH_COLOR, pygame.Rect(path[i][0] * CELL_SIZE, path[i][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze surface on the screen
    screen.blit(maze_surface, (0, 0))

    # Update the display
    pygame.display.update()

    # Set the desired frame rate
    frame_rate = 10

    # Tick the clock
    clock.tick(frame_rate)

# Quit pygame
pygame.quit()
