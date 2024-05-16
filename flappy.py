import pygame as pg
import time
import random

pg.init()
pg.display.set_caption("Flappy Bird")
pg.font.init()

font = pg.font.SysFont("mont.ttf", 80)

def changeY():
    global playerY
    playerY -= 2

#Settings
winX = 500
winY = 600
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
  velo = -10

def fall():
  global velo
  global playerY
  velo += 0.8
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

bg = pg.image.load("bg.png")

while game:
    display.fill("white")

    display.blit(pg.transform.scale(bg, (600, 600)), (0,0))

    #Draw player
    bird = pg.image.load("bird.png").convert_alpha()
    display.blit(pg.transform.scale(bird, (50, 40)), (50, playerY))

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
        
    #Collision
    for pipe in pipes:
      if playerY > pipe.y and playerY < pipe.y + 300 and pipe.x < 60 and pipe.x > 40:
        game = False

    if playerY >= winY or playerY <= -10:
       game = False
        
    for p in points:
      if playerY > p.y - 50 and playerY < p.y + 100 and p.x < 60 and p.x > 40:
        score += 1
        points.pop(points.index(p))
    
    #Score
    scoreText = font.render(f"{score}", True, "white", None)
    display.blit(scoreText, (winX // 2 - 20, 20))

    fall()
    
    #Clock
    pg.time.Clock().tick(FPS) 
    pg.display.update()