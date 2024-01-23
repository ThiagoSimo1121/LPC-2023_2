import pygame
import paddle
import ball

pygame.init()

clock = pygame.time.Clock()
paddle_color = (250, 250, 250)
screen_width = 1600 #original size 900
screen_height = 800 #original size 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('futpong')

# create a surface object, image is drawn on it.
imp = pygame.image.load("./assets/jogo-campo.jpg").convert()
field = pygame.transform.scale(imp, (screen_width, screen_height))

player1_quarterback = paddle.Paddle(screen_width/2 -340,  350, paddle_color, 10, 90)
player1_goalkeeper = paddle.Paddle(100,  385, paddle_color, 10, 45)
ia_front_paddle_rect = pygame.Rect(screen_width/2 + 340, 350, 10, 90) #original position (60, 250, 10, 90)
ia_back_paddle_rect = pygame.Rect(screen_width - 120, 385, 10, 45) #original position (810, 275, 10, 45)

'''
player_front_paddle_rect = pygame.Rect(screen_width/2 - 340, 350, 10, 90) #original position (340, 250, 10, 90)
player_back_paddle_rect = pygame.Rect(100, 385, 10, 45) #original position (90, 275, 10, 45)
ia_front_paddle_rect = pygame.Rect(screen_width/2 + 340, 350, 10, 90) #original position (60, 250, 10, 90)
ia_back_paddle_rect = pygame.Rect(screen_width - 120, 385, 10, 45) #original position (810, 275, 10, 45)
'''
player_front_paddle_rect = pygame.Rect(player1_quarterback.dest_x, player1_quarterback.dest_y, player1_quarterback.width, player1_quarterback.height) #original position (340, 250, 10, 90)
player_back_paddle_rect = pygame.Rect(player1_goalkeeper.dest_x, player1_goalkeeper.dest_y, player1_goalkeeper.width, player1_goalkeeper.height)
b = ball.Ball(1 ,screen_width/2 - 8, screen_height/2 - 12, (155, 0, 0), 25, 25, 10, 0)
ball_rect = pygame.Rect(b.dest_x, b.dest_y, b.width, b.height)
def ball_left():
    ball_rect.move_ip(-b.speedx, b.speedy)
    #return True

def ball_right():
    ball_rect.move_ip(b.speedx, b.speedy)
    #return True

status = True
while status:
    screen.fill((0, 0, 0))
    screen.blit(field, (0, 0))
    player_front_paddle = pygame.draw.rect(screen, paddle_color, player_front_paddle_rect)
    #player_back_paddle = pygame.draw.rect(screen, paddle_color, player_back_paddle_rect)

    ia_front_paddle = pygame.draw.rect(screen, paddle_color, ia_front_paddle_rect)
    ia_back_paddle = pygame.draw.rect(screen, paddle_color, ia_back_paddle_rect)

    ball = pygame.draw.rect(screen,(155, 0, 0), ball_rect)
    if b.status == 1:
        ball_left()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_front_paddle_rect.move_ip(0, -10)
    elif key[pygame.K_s]:
        player_front_paddle_rect.move_ip(0, 10)
    if key[pygame.K_q]:
        player_back_paddle_rect.move_ip(0, -7)
    elif key[pygame.K_a]:
        player_back_paddle_rect.move_ip(0, 7)
    if key[pygame.K_u]:
        ia_front_paddle_rect.move_ip(0, -10)
    elif key[pygame.K_j]:
        ia_front_paddle_rect.move_ip(0, 10)
    if key[pygame.K_i]:
        ia_back_paddle_rect.move_ip(0, -7)
    elif key[pygame.K_k]:
        ia_back_paddle_rect.move_ip(0, 7)

    if pygame.Rect.colliderect(ball, player_front_paddle_rect) and b.status == 1:
        b.status = 2
        b.speedy = 0
        b.speedy = player1_quarterback.dest_y/100
    if b.status == 2:
        ball_right()
    if pygame.Rect.colliderect(ball, ia_front_paddle_rect) and b.status == 2:
        b.status = 1
    #player1_quarterback.set_positiony()
    print(player_front_paddle_rect.update(player1_quarterback.dest_x, player1_quarterback.dest_y, player1_quarterback.width, player1_quarterback.height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
