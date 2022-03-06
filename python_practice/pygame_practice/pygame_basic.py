import pygame
pygame.init()

# screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#screen title setting
pygame.display.set_caption("python game")

#FPS (frame per second)
clock = pygame.time.Clock()

#background
background = pygame.image.load("C:\\Users\\delig\\Desktop\\coding\\python\\background.png")

#importing sprite
character = pygame.image.load("C:\\Users\\delig\\Desktop\\coding\\python\\character.png")
character_size = character.get_rect().size #size of image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2 #half of the width of screen
character_y_pos = screen_height - character_height #very bottom of the height of screen

# location to move
to_x = 0
to_y = 0

# moving spped
character_speed = 0.6

# enemy character
enemy = pygame.image.load("C:\\Users\\delig\\Desktop\\coding\\python\\enemy.png")
enemy_size = enemy.get_rect().size #size of image
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2 #half of the width of screen
enemy_y_pos = screen_height /2 - enemy_height /2 #very bottom of the height of screen


# font
game_font = pygame.font.Font(None, 40) #creating font object (font, size)

# total time
total_time = 10

# time calculation
start_ticks = pygame.time.get_ticks() # start_ticks = present time


# event loop
running = True #Is the game running?
while running:
    dt = clock.tick(60)
    
    for event in pygame.event.get(): #what event had occured?
        if event.type == pygame.QUIT: #Is the screen closed?
            running = False

        if event.type == pygame.KEYDOWN: #is the key pressed?
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: # is the user stop pressing key?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #limiting the movement of character by the border of screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #collision check
    if character_rect.colliderect(enemy_rect):
        print("collided")
        running = False

    

    screen.blit(background, (0, 0)) #background and its location (very top left)
    #screen.fill((rgb)) ==> filling the screen by certain color
    screen.blit(character, (character_x_pos, character_y_pos)) #character and its location
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #calculating time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #time = present time - start time (after - before = total amount of time spent)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # if the time is below 0, quit the game
    if total_time - elapsed_time <= 0:
        print("time out")
        running = False

    pygame.display.update() # redrawing the game screen

#wait before quit
pygame.time.delay(2000) #wait 2second before quit

# quit the game
pygame.quit()

