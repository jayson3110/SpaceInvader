import pygame
import random


#initialize 
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.png')

#Title Icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playX_change = 0 
playY_change = 0 


#Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40

#Bullet
# ready - you cant sê the bullet on the screen
# Fire - the bullet í currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10

bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x,y))

def enemy(x, y):
    screen.blit(enemyImg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))


#Game loop - running always
running = True
while running:
    #RGB 
    screen.fill((0,0,0))

    #background Image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playX_change = -5
            if event.key == pygame.K_RIGHT:
                playX_change = 5

            if event.key == pygame.K_UP:
                playY_change =  -5
            if event.key == pygame.K_DOWN:
                playY_change =  5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                playX_change = 0
                playY_change = 0

  

    
    # Checking for boundaries of spaceship so it doesnt go out of bounđs
    playerX +=playX_change
    if playerX <=0:
        playerX = 0

    elif playerX >= 730:
        playerX = 730


    playerY +=playY_change
    if playerY <= 0:
        playerY = 0

    if playerY >= 530:
        playerY = 530

    #Enemy for boundaries of spaceship so it doesnt go out of bounđs

    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 4
        enemyY += enemyY_change

    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    

   

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


#https://www.youtube.com/watch?v=FfWpgLFMI7w




