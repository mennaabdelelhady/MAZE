# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")


# Set up the maze
maze = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X                  X",
    "X  XXXXXXXXXXXXXX  X",
    "X  X           X   X",
    "X  X  XXXXXXX  X  XX",
    "X  X  X        X  XX",
    "X  XXXX  XXXXXXX  XX",
    "X     X           XX",
    "XXXXX X   XXXXXXXXXX",
    "X     X      X     X",
    "X  XXXXXXXXX   XXX X",
    "X           X      X",
    "X  XXXXXXX  X    XXX",
    "X  X     X  X  X   X",
    "X  X  XXXX  X  X   X",
    "X  X  X     X  X   X",
    "X  XXXX  XXXX  X   X",
    "X     X        X   X",
    "XXXXXXXXXXXXXXXXXX  ",
]

# Set up the player
player_size = 40
player_x = 40
player_y = 40

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    elif keys[pygame.K_RIGHT]:
        player_x += 5
    elif keys[pygame.K_UP]:
        player_y -=5
    elif keys[pygame.K_DOWN]:
        player_y += 5

    # Check for collision with walls
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for row_index, row in enumerate(maze):
        for col_index, col in enumerate(row):
            if col == "X":
                wall_rect = pygame.Rect(col_index * player_size, row_index * player_size, player_size, player_size)
                if player_rect.colliderect(wall_rect):
                    if keys[pygame.K_LEFT]:
                        player_x += 5
                    elif keys[pygame.K_RIGHT]:
                        player_x -= 5
                    elif keys[pygame.K_UP]:
                        player_y += 5
                    elif keys[pygame.K_DOWN]:
                        player_y -= 5

    # Draw the maze
    screen.fill((255, 255, 255))
    for row_index, row in enumerate(maze):
        for col_index, col in enumerate(row):
            if col == "X":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(col_index * player_size, row_index * player_size, player_size, player_size))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_x, player_y, player_size, player_size))

    # Update the screen
    pygame.display.update()

# Clean up
pygame.quit()
