import pygame

pygame.init()

largura = 500
altura = 500

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Tela de teste")

square = pygame.Rect(100, 100, 50, 50)

status = True
while status:
    #tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (0, 0, 255), square)
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        square.move_ip(0, -1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    pygame.display.update()
pygame.quit()