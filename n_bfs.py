import pygame
from collections import deque
import time

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")


# Define the maze as a 2D array of integers
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Calculate the size of each cell based on the screen size and the maze dimensions
CELL_WIDTH = SCREEN_WIDTH // len(maze[0])
CELL_HEIGHT = SCREEN_HEIGHT // len(maze)

# Define the starting and ending points
start = (1, 1)
end = (len(maze)-2, len(maze[0])-2)

# Define a function to draw the maze
def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            color = WHITE
            if maze[row][col] == 1:
                color = BLACK
            elif (row, col) == start:
                color = RED
            elif (row, col) == end:
                color = GREEN
            pygame.draw.rect(screen, color, (col*CELL_WIDTH, row*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

# Define a function to find the path through the maze using BFS
def find_path():
    queue = deque()
    visited = set()
    prev = {}
    queue.append(start)
    visited.add(start)
    while queue:
        curr = queue.popleft()
        if curr == end:
            break
        row, col = curr
        neighbors = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]
        for neighbor in neighbors:
            row, col = neighbor
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                prev[neighbor] = curr

    # Backtrack to find the path
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()

    # Return the path
    return path

# Define the main function
def main():
    # Set up the clock
    clock = pygame.time.Clock()
    FPS = 60

    # Find the path through the maze
    path = find_path()

    # Main game loop
    running = True
    i = 0
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the maze
        draw_maze()

        # Draw the path up to the current cell
        for j in range(len(path[:i])-1):
            curr = path[j]
            next = path[j+1]
            pygame.draw.line(screen, BLUE, ((curr[1]+0.5)*CELL_WIDTH, (curr[0]+0.5)*CELL_HEIGHT), ((next[1]+0.5)*CELL_WIDTH, (next[0]+0.5)*CELL_HEIGHT), 5)

        # Update the screen
        pygame.display.update()

        # Tick the clock
        clock.tick(FPS)

        # Wait for a short time
        time.sleep(0.1)

        # Increment the current cell counter
        i += 1
        if i >= len(path):
            running = False

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    main()
