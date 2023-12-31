import check
import pygame
from pygame.locals import *
import sys
import random


def true(tehai):
    pygame.init()
    (w, h) = 900, 600
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("True Page")

    mati = check.matihai(tehai)
    x = 450
    y = 300
    title = pygame.image.load("gif/maru.png").convert_alpha()
    rect_title = title.get_rect()
    rect_title.center = (x, y)

    while(True):
        screen.fill((0, 0, 0, 0))
        screen.blit(title, rect_title)
        
        pygame.time.wait(10)
        pygame.display.update()

        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                answer(tehai)


def false(tehai):
    pygame.init()
    (w, h) = 900, 600
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("False Page")

    mati = check.matihai(tehai)
    x = 450
    y = 300
    title = pygame.image.load("gif/batu.png").convert_alpha() 
    rect_title = title.get_rect() 
    rect_title.center = (x, y)

    while(True):
        screen.fill((0, 0, 0, 0))
        screen.blit(title, rect_title)
        
        pygame.time.wait(10) 
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                answer(tehai)


def answer(tehai):
    pygame.init()
    (w, h) = 900, 600
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Answer Page")

    mati = check.matihai(tehai)
    title = pygame.image.load("gif/kotae.png").convert_alpha()
    rect_title = title.get_rect()
    rect_title.center = (230, 100)
    n = 0
    x = 150
    y = 250
    for hai in mati:
        filename = "gif/p_ms" + str(hai) + "_0.gif"
        exec("hai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_hai_" + str(n) + "= hai_" + str(n) + ".get_rect()") 
        exec("rect_hai_" + str(n) + ".center = (x, y)")
        x += 50
        n += 1
    n = 0
    x = 150
    y = 500
    for hai in tehai:
        filename = "gif/p_ms" + str(hai) + "_0.gif"
        exec("hai_m_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_hai_m_" + str(n) + "= hai_m_" + str(n) + ".get_rect()") 
        exec("rect_hai_m_" + str(n) + ".center = (x, y)")
        x += 50
        n += 1

    while(True):
        screen.fill((0, 0, 0, 0))
        screen.blit(title, rect_title)
        
        for i in range(len(mati)):
            exec("screen.blit(hai_" + str(i) + ", rect_hai_" + str(i) + ")")
        for i in range(len(tehai)):
            exec("screen.blit(hai_m_" + str(i) + ", rect_hai_m_" + str(i) + ")")
        
        
        pygame.time.wait(10)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                main_loop()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()


def main(tehai):
    pygame.init()
    (w, h) = (900,600)
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Main Page")
    ans_button = pygame.image.load("gif/ans.png").convert_alpha()
    rect_ans_button = ans_button.get_rect()
    rect_ans_button.center = (400, 350)
    title = pygame.image.load("gif/title.png").convert_alpha()
    rect_title = title.get_rect()
    rect_title.center = (230, 50)
    
    list_type = [0,0,0,0,0,0,0,0,0]

    n = 0
    x = 150
    y = 500
    for hai in tehai:
        filename = "gif/p_ms" + str(hai) + "_0.gif"
        exec("hai_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
        exec("rect_hai_" + str(n) + "= hai_" + str(n) + ".get_rect()") 
        exec("rect_hai_" + str(n) + ".center = (x, y)")
        x += 50
        n += 1

    while(True):
        x = 200
        y = 200
        n = 1
        for i in list_type:
            if i == 0:
                filename = "gif/p_ms" + str(n) + "_0.gif"
            elif i == 1:
                filename = "gif/p_ms" + str(n) + "_1.gif"
            exec("hai_m_" + str(n) + "= pygame.image.load(filename).convert_alpha()")
            exec("rect_hai_m_" + str(n) + "= hai_m_" + str(n) + ".get_rect()") 
            exec("rect_hai_m_" + str(n) + ".center = (x, y)")
            x += 50
            n += 1

        screen.fill((0, 0, 0, 0))
        screen.blit(ans_button, rect_ans_button)
        screen.blit(title, rect_title)
        l = len(tehai)
        for i in range(l):
            exec("screen.blit(hai_" + str(i) + ", rect_hai_" + str(i) + ")")
        for i in range(1,10):
            exec("screen.blit(hai_m_" + str(i) + ", rect_hai_m_" + str(i) + ")")
        pygame.time.wait(10)
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                #print(x,y)
                if (170 < y and y < 230):
                    for i in range(9):
                        if (185 + 50*i <= x and x <= 220 + 50*i):
                            list_type[i] = (list_type[i]+1)%2

                if 360 <= x and x <= 440:
                    if 325 <= y and y <= 375:
                        list_sub = []
                        for j in range(1,10):        
                            if j*list_type[j-1] != 0:
                                list_sub.append(j)
                            
                        #print(list_sub)
                        #print(check.matihai(tehai))
                        if list_sub == check.matihai(tehai):
                            true(tehai)
                        else:
                            false(tehai)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                

def main_loop():
    yama = []
    for i in range(4):
        for j in range(1,10):
            yama.append(j)
    while True:
        list_a = []
        list_a = random.sample(yama, 13)
        list_a.sort()

        if check.matihai(list_a) != [0]:
            main(list_a)

if __name__ == "__main__":
    main_loop()
