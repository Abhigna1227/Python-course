import math
import random
import pygame
#consonants
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=100
COLLISION_DISTANCE=27
pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background=pygame.image.load('background.jpg')
pygame.display.set_caption("space enemy.png")
icon=pygame.image.load('UFO.jpg')
pygame.display.set_icon(icon)
playerIMG=pygame.image.load('player.png')
playerx=PLAYER_START_X
playery=PLAYER_START_Y
playerx_change=0
enemyIMG=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
