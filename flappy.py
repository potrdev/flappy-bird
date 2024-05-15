import pygame as pg
import time
import random

pg.init()

def changeY():
    global playerY
    playerY -= 2

#Settings
winX = 800
winY = 500
FPS = 60

#Dislay
display = pg.display.set_mode((winX, winY))

#Pipes
maxPipes = 5
time = 0
pipeSpawnRate = 3

#Player
playerY = 0
isFalling = True

game = True

class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pipes = []

while game:
    #Clock
    pg.time.Clock().tick(FPS)
    display.fill("white")

    #Draw player
    pg.draw.circle(display, "yellow", (50, playerY), 30)

    #Velocity
    if isFalling:
        playerY += 5

    #Get keys
    keys = pg.key.get_pressed()

    #Quit check
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and isFalling:
                isFalling = False
                for i in range(60):
                    changeY()
                isFalling = True

    if time <= 30 * pipeSpawnRate:
        time += 1
        print(time)
    else:
        downPipe = Pipe(winX, random.randint(0, winY // 2))
        upPipe = Pipe(downPipe.x, downPipe.y + 10)
        pipes.append(downPipe)
        pipes.append(upPipe)
        time = 0
        
    for pipe in pipes:
        pipe.x -= 1
        
        if pipes.index(pipe) != 0:
            pg.draw.rect(display, "green", (pipe.x, pipe.y, 50, 250))
        


    
    
                

    pg.display.update()