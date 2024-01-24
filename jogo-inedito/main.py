import pygame

pygame.init()

clock = pygame.time.Clock()
paddle_color = (255, 255, 255)
control_ball = 0 #0 - left player, 1 - right player
height_paddle = 90
paddle_part_height = height_paddle / 9
ball_speedx = -12
ball_speedy = -3
speed_limit = 30
hit = False
status = True
timer = 60
player_score = 0
ia_score = 0
initial_time = pygame.time.get_ticks()

game_font = pygame.font.Font('freesansbold.ttf',45)
screen_width = 1600  # original size 900
screen_height = 800  # original size 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('futpong')

# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/jogo-campo.jpg").convert()
field = pygame.transform.scale(imp, (screen_width, screen_height))

player_front_paddle_rect = pygame.Rect(screen_width / 2 - 340, 350, 10, height_paddle)  # original position (340, 250, 10, 90)
player_back_paddle_rect = pygame.Rect(100, 385, 10, height_paddle/2)  # original position (90, 275, 10, 45)
ia_front_paddle_rect = pygame.Rect(screen_width / 2 + 340, 350, 10, height_paddle)  # original position (60, 250, 10, 90)
ia_back_paddle_rect = pygame.Rect(screen_width - 103, 385, 10, height_paddle/2)  # original position (810, 275, 10, 45)

ball_rect = pygame.Rect(screen_width / 2 - 8, screen_height / 2 - 12, 25, 25)

goal_player_rect1 = pygame.Rect(0, 267, 100, 11)
goal_player_rect2 = pygame.Rect(0, 528, 100, 11)

goal_ia_rect1 = pygame.Rect(screen_width - 94, 267, 100, 11)
goal_ia_rect2 = pygame.Rect(screen_width - 94, 528, 100, 11)

player_goal_line_rect = pygame.Rect(70, 278, 11, 250)
ia_goal_line_rect = pygame.Rect(screen_width - 70, 278, 11, 250)

def kick_off(goalkeeper, ctball):
    global ball_speedx
    if ctball == 0:
        ball_rect.center = (goalkeeper.x + 30, goalkeeper.centery)
    elif ctball == 1:
        ball_rect.center = (goalkeeper.x - 30, goalkeeper.centery)
    ball_speedx = -ball_speedx

def game_restart(ctball):
    global screen_width, screen_height, ball_speedx, ball_speedy
    if ctball == 0:
        ball_speedx = -12
        ball_speedy = -3
    elif ctball == 1:
        ball_speedx = 12
        ball_speedy = 3
    ball_rect.center = (screen_width/2, screen_height/2)

def balls_moviments():
    collide_tolerance = 10
    global ball_speedy, ball_speedx, hit, player_score, ia_score, control_ball

    ball_rect.x = ball_rect.x + ball_speedx
    ball_rect.y = ball_rect.y + ball_speedy

    if ball_rect.right >= screen_width:
        ball_speedx *= -1
        ball_rect.x = screen_width - 120
        ball_rect.y = ia_back_paddle_rect.y

    if ball_rect.left <= 0:
        ball_speedx *= -1
        ball_rect.x = 120
        ball_rect.y = player_back_paddle_rect.y

    if ball_rect.top <= 0 or ball_rect.bottom >= screen_height:
        ball_speedy *= -1
    if player_front_paddle_rect.x <= ball_rect.x <= player_front_paddle_rect.x + player_front_paddle_rect.width:
        if player_front_paddle_rect.y <= ball_rect.y <= player_front_paddle_rect.y + player_front_paddle_rect.height:
            ball_rect.x = player_front_paddle_rect.x + player_front_paddle_rect.width
            ball_speedx *= -1

    if player_back_paddle_rect.x <= ball_rect.x <= player_back_paddle_rect.x + player_back_paddle_rect.width:
        if player_back_paddle_rect.y <= ball_rect.y <= player_back_paddle_rect.y + player_back_paddle_rect.height:
            ball_rect.x = player_back_paddle_rect.x + player_back_paddle_rect.width
            ball_speedx *= -1

    if ia_front_paddle_rect.x <= ball_rect.x <= ia_front_paddle_rect.x + ia_front_paddle_rect.width:
        if ia_front_paddle_rect.y <= ball_rect.y <= ia_front_paddle_rect.y + ia_front_paddle_rect.height:
            ball_rect.x = ia_front_paddle_rect.x
            ball_speedx *= -1

    if ia_back_paddle_rect.x <= ball_rect.x <= ia_back_paddle_rect.x + ia_back_paddle_rect.width:
        if ia_back_paddle_rect.y <= ball_rect.y <= ia_back_paddle_rect.y + ia_back_paddle_rect.height:
            ball_rect.x = ia_back_paddle_rect.x
            ball_speedx *= -1

    if ball_rect.colliderect(goal_player_rect1) or ball_rect.colliderect(goal_player_rect2):
        ball_speedy *= -1
    if ball_rect.colliderect(goal_ia_rect1) or ball_rect.colliderect(goal_ia_rect2):
        ball_speedy *= -1

    if ball_rect.colliderect(player_goal_line_rect):
        ia_score += 1
        control_ball = 0
        game_restart(control_ball)

    if ball_rect.colliderect(ia_goal_line_rect):
        player_score += 1
        control_ball = 1
        game_restart(control_ball)

while status:
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

    player_text = game_font.render('{}'.format(player_score), False, (200, 200, 200))
    screen.blit(player_text, ((screen_width/2) - 150, 100))
    ia_text = game_font.render('{}'.format(ia_score), False, (200, 200, 200))
    screen.blit(ia_text, ((screen_width/2) + 150, 100))
    timer_text = game_font.render('{}'.format(timer), False, (255, 0, 150))
    screen.blit(timer_text, (screen_width/2 - 20, 100))

    current_time = pygame.time.get_ticks()

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

    if player_score == 2 or ia_score == 2:
        status = False
    real_time = current_time - initial_time
    if real_time % 60 == 0:
        timer -= 1

    if timer <= 0 and (ia_score == player_score):
        timer = 60
        ball_rect.center = (screen_width / 2, screen_height / 2)
        player_front_paddle_rect.center = (screen_width / 2 - 340, 350)
        player_back_paddle_rect.center = (100, 385)
        ia_front_paddle_rect.center = (screen_width / 2 + 340, 350)
        ia_back_paddle_rect.center = (screen_width - 103, 385)
        ball_speedy = -1
    elif timer == 0:
        status = False

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
