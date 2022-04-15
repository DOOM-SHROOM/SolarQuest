import pygame
pygame.init()
import time
import random
import math
import numpy as np
ball_num = 10
ship_num = 1
bMass = []
xPos = []
yPos = []
xVel = []
yVel = []
shipx = []
shipy = []
shippoints = [(0, 0)]
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
ORALLOW = (255, 200, 100)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRUE = (0, 100, 255)
LBLUE = (100, 100, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BROWN = (139,69,19)
BLACK = (0, 0, 0)
LGREY = (180, 180, 180)
GREY = (140, 140, 140)
DGREY = (80, 80, 80)
WHITE = (255, 255, 255)
planetColor = [GREY, ORALLOW, GRUE, RED,
    ORALLOW, YELLOW, LBLUE, BLUE, BROWN, ORALLOW]
G = 2.
velocitysubtractrate = 15.
xScreenSize = 1800
yScreenSize = 900
xPlanetPos = xScreenSize / 2 - 150
yPlanetPos = yScreenSize / 2
size = (xScreenSize, yScreenSize)
maxMass = 2.
vMax = 1.
dt = 1.
timeDelay = 0.01
dist = 0.
xdist = 0.
ydist = 0.
for j in range (ball_num):
    velocitysubtractrate *= 1.05
    xPlanetPos -= 20
    bMass.append(int(maxMass))
    xPos.append(xPlanetPos)
    yPos.append(yPlanetPos)
    xVel.append(0)

    yVel.append(56 / velocitysubtractrate)
bMass[ball_num - 1] = 100
xPos[ball_num - 1] = xScreenSize / 2
yPos[ball_num - 1] = yScreenSize / 2
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for j in range (ball_num - 1):
        xPos[j] = xPos[j] + xVel[j]*dt
        yPos[j] = yPos[j] + yVel[j]*dt
        if (xPos[j] > xScreenSize):
            xVel[j] *= -1
        if (yPos[j] > yScreenSize):
            yVel[j] *= -1
        if (xPos[j] < 1):
            xVel[j] *= -1
        if (yPos[j] < 1):
            yVel[j] *= -1
    for j in range (ball_num):
        pygame.draw.circle(screen, planetColor[j],
            (int(xPos[j]), int(yPos[j])), int(bMass[j]), 0)
        pygame.draw.circle(screen, WHITE,
            (int(xPos[5]), int(yPos[5])), int(bMass[5]+4), 1)
        pygame.draw.circle(screen, planetColor[4],
            (int(xPos[4]), int(yPos[4])), int(bMass[4]+3), 0)
        pygame.draw.ellipse(screen, RED, (int(xPos[4]), int(yPos[4]), 4, 4))
        for r in range (ball_num-1):
            xdist = xPos[r] - xPos[9]
            ydist = yPos[r] - yPos[9]
            dist = np.sqrt((xdist * xdist) + (ydist * ydist))
            if dist != 0:
                fg = (bMass[r] * bMass[9] * G) / (dist * dist)
                acceleration = fg / bMass[r]
                xVel[r] -= (xdist/dist) * acceleration
                yVel[r] -= (ydist/dist) * acceleration
    for r in range (ball_num - 1):
        xdist = xPos[r] - xPos[9]
        ydist = yPos[r] - yPos[9]
        dist = np.sqrt((xdist * xdist) + (ydist * ydist))
        if dist != 0:
            fg = (bMass[r] * bMass[9] * G) / (dist * dist)
            acceleration = fg / bMass[r]
            xVel[r] -= (xdist/dist) * acceleration
            yVel[r] -= (ydist/dist) * acceleration
    pygame.display.flip()
    time.sleep(timeDelay)
    screen.fill(BLACK)

