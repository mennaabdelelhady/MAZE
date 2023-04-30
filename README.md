# MAZE 
#BFS
This code creates a maze using Pygame and implements the Breadth-First Search (BFS) algorithm to find the shortest path from the starting position to the ending position in the maze. Here's a brief overview of how the code works:

The maze is defined as a 2D array of integers, where 0 represents an open cell and 1 represents a blocked cell (a wall).

Pygame is initialized and a surface is created to draw the maze.

The BFS algorithm is implemented using a queue and a dictionary to store the previous position for each position. The BFS algorithm starts at the starting position and iteratively explores its neighbors until it reaches the ending position or all reachable positions have been explored.

The shortest path is traced from the ending position back to the starting position using the dictionary of previous positions.

The path is drawn on the maze surface using a blue color.

The maze surface is drawn on the screen in the main loop, and Pygame is updated to display the changes.

The desired frame rate is set and the clock is ticked to control the game's speed.

Pygame is quit when the game is exited.
