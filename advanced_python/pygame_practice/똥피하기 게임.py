import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\delig\\Desktop\\coding\\python\\background.png")


character = pygame.image.load("C:\\Users\\delig\\Desktop\\coding\\python\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

enemy = pygame.image.load("C:\\Users\\delig\\Desktop\\coding\\python\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0, screen_width - enemy_width)
enemy_y_pos = 0 - enemy_height

running = True

game_font = pygame.font.Font(None, 60)
timer_font = pygame.font.Font(None, 40)

character_speed = 0.6
enemy_speed = 0.04

to_x = 0
enemy_to_y = 0

total_time = 60

start_time = pygame.time.get_ticks()

while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Is the screen closed?
           running = False

        if event.type == pygame.KEYDOWN: #is the key pressed?
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP: # is the user stop pressing key?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_to_y += enemy_speed
    enemy_y_pos += enemy_to_y * dt
    character_x_pos += to_x * dt
    
    if enemy_y_pos >= screen_height:
        enemy_y_pos = 0 - enemy_height
        enemy_x_pos = random.randrange(0, screen_width - enemy_width)
        enemy_to_y = 0

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
        
    screen.blit(background, (0, 0)) 
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer = timer_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        running = False
        win = game_font.render("GOOD JOB YOU WON!", True, (255, 255, 255))
        screen.blit(win, (20, 100))

    if character_rect.colliderect(enemy_rect):
        running = False
        fail = game_font.render("UH OH GAME OVER!", True, (255, 255, 255))
        screen.blit(fail, (40,100))
    
    pygame.display.update()


pygame.time.delay(2000)
pygame.quit()




