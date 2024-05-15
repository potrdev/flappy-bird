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
pipeSpawnRate = 6
pipeSpeed = 4

#Player
playerY = 0
velo = 0
score = 0

def jump():
  global velo
  velo = -12

def fall():
  global velo
  global playerY
  velo += 0.7
  playerY += velo

game = True

class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

pipes = []
points = []

while game:
    #Clock
    pg.time.Clock().tick(FPS)
    display.fill("white")

    #Draw player
    pg.draw.circle(display, "yellow", (50, playerY), 20)

    #Get keys
    keys = pg.key.get_pressed()

    #Quit check
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                jump()

    if time <= 30 * pipeSpawnRate:
        time += 1

    else:
        downPipe = Pipe(winX, random.randint(0, winY // 4) - 150)
        upPipe = Pipe(downPipe.x, downPipe.y + 450)
        point = Point(downPipe.x, downPipe.y + 350)
        points.append(point)
        pipes.append(downPipe)
        pipes.append(upPipe)
        time = 0
        
    for pipe in pipes:
        pipe.x -= pipeSpeed
        pg.draw.rect(display, "green", (pipe.x, pipe.y, 50, 300))
        
    for p in points:
        p.x -= pipeSpeed
        pg.draw.rect(display, "blue", (p.x, p.y, 50, 50))
        
    #Collision
    for pipe in pipes:
      if playerY > pipe.y and playerY < pipe.y + 300 and pipe.x < 60 and pipe.x > 40:
        game = False
        
    for p in points:
      if playerY > p.y - 50 and playerY < p.y + 100 and p.x < 60 and p.x > 40:
        score += 1
        points.pop(points.index(p))
        
    fall() 
      
    pg.display.update()