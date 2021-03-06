import pygame
import math
import random

from pygame import mixer




#initialize 
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load('background.png')

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)
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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6 

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet
# ready - you cant sê the bullet on the screen
# Fire - the bullet í currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10 
testY = 10 

#Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))




def player(x, y):
    screen.blit(playerImg, (x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))


def isCollision(enemyX, enemyY, bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False



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
                    buller_sound = mixer.Sound('laser.wav')
                    buller_sound.play()
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
    for i in range(num_of_enemies):
        #Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

         #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX,bulletY)

        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state= "ready"
            score_value += 1
            
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i], i )



    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    

    

   

    player(playerX, playerY)
    show_score(textX,testY)
    pygame.display.update()




#https://www.youtube.com/watch?v=FfWpgLFMI7w




