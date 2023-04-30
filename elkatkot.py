import pygame

# Initialize Pygame
pygame.init()

#set up the music
pygame.mixer.music.load('C:/Users/user/Desktop/pydemo/background_music.mp3.mp3')

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

#music On
pygame.mixer.music.play(-1)

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
player_speed = 10  # increase player speed
movement_delay = 5  # delay in frames between movements
movement_delay_counter = 0


# Set up the exit
exit_rect = pygame.Rect(740, 760, player_size, player_size)

# Set up the clock
clock = pygame.time.Clock()

# Set up the timer
start_ticks = pygame.time.get_ticks()  # get number of milliseconds since Pygame was initialized

# Set up the time limit
time_limit = 27000  # 27 seconds in milliseconds

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the elapsed time
    elapsed_time = pygame.time.get_ticks() - start_ticks

    # Move the player
    keys = pygame.key.get_pressed()
    if movement_delay_counter == 0 and elapsed_time < time_limit:  # check if enough time has passed since last movement and time limit has not been reached
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            movement_delay_counter = movement_delay
        elif keys[pygame.K_RIGHT]:
            player_x += player_speed
            movement_delay_counter = movement_delay
        elif keys[pygame.K_UP]:
            player_y -= player_speed
            movement_delay_counter = movement_delay
        elif keys[pygame.K_DOWN]:
            player_y += player_speed
            movement_delay_counter = movement_delay

    # Decrement the movement delay counter
    if movement_delay_counter > 0:
        movement_delay_counter -= 1

    # Check for collision with walls
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for row_index, row in enumerate(maze):
        for col_index, col in enumerate(row):
            if col == "X":
                wall_rect = pygame.Rect(col_index * player_size, row_index * player_size, player_size, player_size)
                if player_rect.colliderect(wall_rect):
                    if keys[pygame.K_LEFT]:
                        player_x += player_speed
                    elif keys[pygame.K_RIGHT]:
                        player_x -= player_speed
                    elif keys[pygame.K_UP]:
                        player_y += player_speed
                    elif keys[pygame.K_DOWN]:
                        player_y -= player_speed

    # Check for collision with exit
    if player_rect.colliderect(exit_rect):
        running = False
        print("You win at Time: {:02d}:{:02d}!".format(minutes, seconds))

    # Draw the maze
    screen.fill((255, 255, 255))
    for row_index, row in enumerate(maze):
        for col_index, col in enumerate(row):
            if col == "X":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(col_index * player_size, row_index * player_size, player_size, player_size))

    # Draw the exit
    pygame.draw.rect(screen, (0, 255, 0), exit_rect)

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_x, player_y, player_size, player_size))

    # Draw the timer
    seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)
    minutes = int(seconds / 60)
    seconds %= 60
    font = pygame.font.SysFont(None, 25)
    timer_text = font.render("Time: {:02d}:{:02d}".format(minutes, seconds), True, (255, 0, 0))
    screen.blit(timer_text, (10, 10))

    # Check if time limit has been reached
    if elapsed_time >= time_limit:
        running = False
        print("You ran out of time!LOSERRR")

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
pygame.mixer.music.stop()
