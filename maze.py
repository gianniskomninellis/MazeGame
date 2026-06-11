import pygame
import time
import threading

pygame.init()

bob = pygame.display.set_mode((600,600))

done= False

clock = pygame.time.Clock()

x= 50
y= 50

playertime= 0
starttime= time.time()

growingx = 20

def resize():
    global growingx

    while True:
        for i in range(20):
            growingx = growingx + 5
            time.sleep(0.5)

        for i in range(20):
            growingx = growingx - 5
            time.sleep(0.5)

moveThread= threading.Thread(target= resize)
moveThread.daemon = True
moveThread.start()

while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            done = True


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: y = y - 3
    if pressed[pygame.K_s]: y = y + 3
    if pressed[pygame.K_a]: x = x - 3
    if pressed[pygame.K_d]: x = x + 3

    bob.fill((0,0,0))

    player1 = pygame.draw.rect(bob,(0,0,150), pygame.Rect(x,y,40,40))

    wallUp = pygame.draw.rect(bob,(20,140,20), pygame.Rect(0,0,600,20))
    wallDown = pygame.draw.rect(bob, (20, 140, 20), pygame.Rect(0,580, 600, 20))
    wallLeft = pygame.draw.rect(bob, (20, 140, 20), pygame.Rect(0,0, 15, 700))
    wallRight = pygame.draw.rect(bob, (20, 140, 20), pygame.Rect(589,0, 15, 700))

    wall1 = pygame.draw.rect(bob,(140,20,20), pygame.Rect(105,20,25,450))
    growingwall = pygame.draw.rect(bob, (140, 20, 20), pygame.Rect(475, -100, growingx, 550))
    wall2 = pygame.draw.rect(bob, (140, 20, 20), pygame.Rect(225,200, 100, 500))

    walls = [wallUp,wallDown,wallLeft,wallRight,wall1,wall2,growingwall]

    finish = pygame.draw.rect(bob,(255,255,0), pygame.Rect(525,50,50,50))

    for wall in walls:
        if player1.colliderect(wall):
            if pressed[pygame.K_w]:
                y = y+3
            if pressed[pygame.K_s]:
                y = y-3
            if pressed[pygame.K_a]:
                x = x+3
            if pressed[pygame.K_d]:
                x = x-3


    if player1.colliderect(finish):
        x = 50
        y=50
        finaltime= time.time()
        playertime =round(finaltime-starttime)
        starttime = time.time()


    font = pygame.font.SysFont("jokerman",30, bold =True, italic=True)
    timer = font.render("Your Time Was: "+str(playertime), True,(255,215,0))
    bob.blit(timer,(220,250))

    pygame.display.flip()
    clock.tick(60)

#SCRIPT FOR MOVING WALL----------------------------------------------------------------------------------------------
#movingwall = pygame.draw.rect(bob, (20, 140, 20), pygame.Rect(movingx/y, 600, 20))

#movingx/y = 200
#def move():
    #global movingx

    #While True:
        #for i in range(100):
            #movingx = movingx + 1
            #time.sleep(0.5)

        #for i in range(100):
            #movingx - 1
            #time.sleep(0.5)

#moveThread= threading.Thread(target=move)
#moveThread.daemon = True
#moveThread.start()