import random
import pygame

#初始化參數設計
win_width = 1000
win_height = 800
font_px = 15

#創建窗口及文本設計
pygame.init()
pygame.display.set_caption("程式的一場雨")
winsur = pygame.display.set_mode((win_width,win_height))
font = pygame.font.SysFont('',23)
bg_surface = pygame.Surface((win_width,win_height),flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_surface)
bg_surface.fill(pygame.Color(0,0,0,28))
winsur.fill((0,0,0))

#文本內容
letter='1234567890!@#$%^&*qwertyuiopasdfghjklzxcvbnm'
rainbow_list = [(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 127, 255),(0, 0, 255),(139, 0, 255),
(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 127, 255),(0, 0, 255),(139, 0, 255),
(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 127, 255),(0, 0, 255),(139, 0, 255),
(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 127, 255),(0, 0, 255),(139, 0, 255),
(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 127, 255),(0, 0, 255),(139, 0, 255),
(255, 0, 0),(255, 165, 0),(255, 255, 0),(0, 255, 0),(0, 127, 255),(0, 0, 255),(139, 0, 255),
(255, 0, 0),(255, 165, 0)]
# blue_silver=[(0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),
# (0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),
# (0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),
# (0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),
# (0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),(0,191,255),(192,192,192),
# (0,191,255),(192,192,192),(0,191,255),(192,192,192)]

texts = [font.render(letter[i],True,(0,255,0)) for i in range(44)]
# texts = [font.render(letter[i],True,j) for i,j in zip(range(44),rainbow_list)]
# texts = [font.render(letter[i],True,j) for i,j in zip(range(44),blue_silver)]
# texts = [font.render(letter[i],True,(0,191,255)) for i in range(44)]
# texts2 = [font.render(letter[i],True,(192,192,192)) for i in range(44)]


#顯示設計
column = int(win_width/font_px)
drops = [0 for i in range(column)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            change = pygame.key.get_pressed()
            if change[32]:
                exit()
    #延時30
    pygame.time.delay(30)

    winsur.blit(bg_surface,(0,0))
    for i in range(len(drops)):
        text = random.choice(texts)
        winsur.blit(text,((i* font_px),drops[i] * font_px))
        drops[i] += 1
        if drops[i] * 10 > win_height or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()