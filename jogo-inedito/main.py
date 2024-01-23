import pygame
import random

pygame.init()

clock = pygame.time.Clock()
r = random.randint(-5, 5)
paddle_color = (250, 250, 250)
screen_width = 1600  # original size 900
screen_height = 800  # original size 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('futpong')

# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/jogo-campo.jpg").convert()
field = pygame.transform.scale(imp, (screen_width, screen_height))

player_front_paddle_rect = pygame.Rect(screen_width / 2 - 340, 350, 10, 90)  # original position (340, 250, 10, 90)
player_back_paddle_rect = pygame.Rect(100, 385, 10, 45)  # original position (90, 275, 10, 45)
ia_front_paddle_rect = pygame.Rect(screen_width / 2 + 340, 350, 10, 90)  # original position (60, 250, 10, 90)
ia_back_paddle_rect = pygame.Rect(screen_width - 103, 385, 10, 45)  # original position (810, 275, 10, 45)

ball_rect = pygame.Rect(screen_width / 2 - 8, screen_height / 2 - 12, 25, 25)

goal_player_rect1 = pygame.Rect(0, 267, 100, 11)
goal_player_rect2 = pygame.Rect(0, 528, 100, 11)
goal_ia_rect1 = pygame.Rect(screen_width - 94, 267, 100, 11)
goal_ia_rect2 = pygame.Rect(screen_width - 94, 528, 100, 11)
player_goal_line_rect = pygame.Rect(70, 278, 11, 250)
ia_goal_line_rect = pygame.Rect(screen_width - 70, 278, 11, 250)

ball_speedx = 7
ball_speedy = r
paddle_speed = 0
max_speed = 12
hit = False
status = True
timer = 0
player_goals = 0
ia_goals = 0

def kick_off(goalkeeper):
    global ball_speedx
    ball_rect.center = (goalkeeper.x, goalkeeper.centery)
    ball_speedx = -ball_speedx

def balls_moviments():
    global ball_speedy, ball_speedx, hit

    ball_rect.x = ball_rect.x + ball_speedx
    ball_rect.y = ball_rect.y + ball_speedy

    if (ball_rect.right >= screen_width) and hit == False:
        kick_off(ia_back_paddle_rect)
        hit = True
    elif (ball_rect.left <= 0) and hit == False:
        kick_off(player_back_paddle_rect)
        hit = True

    if (ball_rect.top <= 0 or ball_rect.bottom >= screen_height) and hit == False:
        ball_speedy = -ball_speedy
        hit = True

    if (ball_rect.x >= 20 and ball_rect.x <= 1400) or (ball_rect.y >= 20 and ball_rect.y <= 1700):
        hit = False

    if hit == False and (ball_rect.colliderect(player_front_paddle_rect)):
        ball_speedx = -ball_speedx
        ball_speedy = -ball_speedy
        hit = True
    if hit == False and (ball_rect.colliderect(ia_front_paddle_rect)):
        ball_speedx = -ball_speedx
        ball_speedy = -ball_speedy
        hit = True
    if hit == False and (ball_rect.colliderect(ia_back_paddle_rect)):
        ball_speedx = -ball_speedx
        ball_speedy = -ball_speedy
        hit = True
    if hit == False and (ball_rect.colliderect(player_back_paddle_rect)):
        ball_speedx = -ball_speedx
        ball_speedy = -ball_speedy
        hit = True


while status :
    # drawing on screen
    screen.fill((0, 0, 0))
    screen.blit(field, (0, 0))
    player_front_paddle = pygame.draw.rect(screen, paddle_color, player_front_paddle_rect)
    player_back_paddle = pygame.draw.rect(screen, paddle_color, player_back_paddle_rect)

    ia_front_paddle = pygame.draw.rect(screen, paddle_color, ia_front_paddle_rect)
    ia_back_paddle = pygame.draw.rect(screen, paddle_color, ia_back_paddle_rect)

    goal_player1 = pygame.draw.rect(screen, (0, 255, 0), goal_player_rect1)
    goal_player2 = pygame.draw.rect(screen, (0, 255, 0), goal_player_rect2)
    goal_ia1 = pygame.draw.rect(screen, (0, 255, 255,), goal_ia_rect1)
    goal_ia2 = pygame.draw.rect(screen, (0, 255, 255,), goal_ia_rect2)
    player_goal_line = pygame.draw.rect(screen,(255, 0, 255), player_goal_line_rect)
    ia_goal_line = pygame.draw.rect(screen,(255, 0, 255), ia_goal_line_rect)

    ball = pygame.draw.rect(screen, (155, 0, 0), ball_rect)

    # paddle`s moviments

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_front_paddle_rect.move_ip(0, -10)
        if player_front_paddle_rect.top <= 0:
            player_front_paddle_rect.top = 0
    elif key[pygame.K_s]:
        player_front_paddle_rect.move_ip(0, 10)
        if player_front_paddle_rect.bottom >= screen_height:
            player_front_paddle_rect.bottom = screen_height
    if key[pygame.K_q]:
        player_back_paddle_rect.move_ip(0, -7)
        if player_back_paddle_rect.top <= 267:
            player_back_paddle_rect.top = 267
    elif key[pygame.K_a]:
        player_back_paddle_rect.move_ip(0, 7)
        if player_back_paddle_rect.bottom >= 539:
            player_back_paddle_rect.bottom = 539
    if key[pygame.K_u]:
        ia_front_paddle_rect.move_ip(0, -10)
        if ia_front_paddle_rect.top <= 0:
            ia_front_paddle_rect.top = 0
    elif key[pygame.K_j]:
        ia_front_paddle_rect.move_ip(0, 10)
        if ia_front_paddle_rect.bottom >= screen_height:
            ia_front_paddle_rect.bottom = screen_height
    if key[pygame.K_i]:
        ia_back_paddle_rect.move_ip(0, -7)
        if ia_back_paddle_rect.top <= 267:
            ia_back_paddle_rect.top = 267
    elif key[pygame.K_k]:
        ia_back_paddle_rect.move_ip(0, 7)
        if ia_back_paddle_rect.bottom >= 539:
            ia_back_paddle_rect.bottom = 539

    balls_moviments()
    # player_front_paddle_rect.y = player_front_paddle.y + paddle_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_p:
                status = False
            if pygame.K_SPACE:
                status = True

    pygame.display.update()
    clock.tick(60)
pygame.quit()
