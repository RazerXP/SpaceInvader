import pygame
from pygame import mixer
import random
import math

pygame.init()

# Game window
screen = pygame.display.set_mode((800, 600))

# Background and Logo and bullet
background = pygame.image.load("F:\\Space Invader\\data\\background.png")
backgroundY = -8700
backgroundY_change = 0.05
logo = pygame.image.load("F:\\Space Invader\\data\\icon.png")
mixer.music.load("F:\\Space Invader\\data\\background.wav")
mixer.music.play(-1)

# Title and Icon
title = pygame.display.set_caption("Space Invader")
icon = pygame.display.set_icon(logo)

# Player
playerX = 370
playerY = 520
playerX_change = 0
def player(x, y):
    player = pygame.image.load("F:\\Space Invader\\data\\player.png")
    screen.blit(player, (playerX, playerY))

# Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_enemy = 6
for i in range(no_enemy):
    enemyIMG.append(pygame.image.load("F:\\Space Invader\\data\\enemy.png"))
    enemyX.append(random.randint(10, 740))
    enemyY.append(random.randint(10, 300))
    enemyX_change.append(2)
    enemyY_change.append(40)
def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))

# Bullets
bullet1X = 0
bullet1Y = 520
bullet1Y_change = 2
bullet_fire1 = "stationary"
bullet1 = pygame.image.load("F:\\Space Invader\\data\\bullet.png")
bullet1_show = pygame.image.load("F:\\Space Invader\\data\\bullet2.png")
bullet1_showX = 770
bullet1_showY = 100
bullet2X = 0
bullet2Y = 520
bullet2Y_change = 2
bullet_fire2 = "stationary"
bullet2 = pygame.image.load("F:\\Space Invader\\data\\bullet.png")
bullet2_show = pygame.image.load("F:\\Space Invader\\data\\bullet2.png")
bullet2_showX = 770
bullet2_showY = 150
def fire_bullet1(x, y):
    global bullet_fire1
    bullet_fire1 = "fired"
    screen.blit(bullet1, (x + 16, y + 30))
def bullet1show(x, y):
    screen.blit(bullet1_show, (770, 100))
def fire_bullet2(x, y):
    global bullet_fire2
    bullet_fire2 = "fired"
    screen.blit(bullet2, (x + 16, y + 30))
def bullet2show(x, y):
    screen.blit(bullet2_show, (770, 150))

# Collision
def ifCollision1():
    distance = math.sqrt(math.pow(enemyX[i] - bullet1X, 2) + math.pow(enemyY[i] - bullet1Y, 2))
    if distance < 45:
        return True
    else:
        return False
def ifCollision2():
    distance = math.sqrt(math.pow(enemyX[i] - bullet2X, 2) + math.pow(enemyY[i] - bullet2Y, 2))
    if distance < 45:
        return True
    else:
        return False

# Score
score_value = 0
font = pygame.font.Font('F:\\Space Invader\\data\\FRAMDCN.ttf', 28)
textX = 10
textY = 10
def score(x,y):
    score = font.render("SCORE : " + str(score_value),True, (255,255,255))
    screen.blit(score, (textX, textY))

# Game over
over_font = pygame.font.Font("F:\\Space Invader\\data\\FRAMDCN.ttf", 72)
ritam_font = pygame.font.Font("F:\\Space Invader\\data\\FRAMDCN.ttf", 32)
def Game_over():
    GameOver = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(GameOver, (200,240))
    Ritam = ritam_font.render("Copyright protected by RITAM", True, (255, 255, 255))
    screen.blit(Ritam, (190,380))


# Loop
status = True
while status:
    screen.blit(background, (0, backgroundY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False

        if event.type == pygame.KEYDOWN:
            # Player movements
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            # Bullets movements
            if event.key == pygame.K_1:
                bullet_sound = mixer.Sound("F:\\Space Invader\\data\\laser.wav")
                bullet_sound.play()
                if bullet_fire1 is "stationary":
                    bullet1X = playerX
                    fire_bullet1(bullet1X, bullet1Y)
            if event.key == pygame.K_2:
                bullet_sound = mixer.Sound("F:\\Space Invader\\data\\laser.wav")
                bullet_sound.play()
                if bullet_fire2 is "stationary":
                    bullet2X = playerX
                    fire_bullet2(bullet2X, bullet2Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Enemy movements
    for i in range(no_enemy):
        if enemyY[i] >= 460:
            for j in range(no_enemy):
                enemyY[j] = 2000
            Game_over()
            GameOverSound = mixer.Sound("F:\\Space Invader\\data\\gameover2.wav")
            GameOverSound.play(-1)
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 740:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collisions
        if ifCollision1():
            collision_sound = mixer.Sound("F:\\Space Invader\\data\\explosion.wav")
            collision_sound.play()
            bullet1Y = playerY
            bullet1X = playerX
            bullet_fire1 = "stationary"
            enemyX[i] = random.randint(10, 740)
            enemyY[i] = random.randint(10, 230)
            score_value += 1
        if ifCollision2():
            collision_sound = mixer.Sound("F:\\Space Invader\\data\\explosion.wav")
            collision_sound.play()
            bullet2Y = playerY
            bullet2X = playerX
            bullet_fire2 = "stationary"
            enemyX[i] = random.randint(10, 740)
            enemyY[i] = random.randint(10, 230)
            score_value += 1
        enemy(enemyX[i], enemyY[i], i)


    # Bullet movements
    if bullet1Y < -70:
        bullet1Y = playerY
        bullet_fire1 = "stationary"
        bullet1show(bullet1_showX, bullet1_showY)
    if bullet_fire1 is "fired":
        fire_bullet1(bullet1X, bullet1Y)
        bullet1Y -= bullet1Y_change
    if bullet2Y < -70:
        bullet2Y = playerY
        bullet_fire2 = "stationary"
        bullet2show(bullet2_showX, bullet2_showY)
    if bullet_fire2 is "fired":
        fire_bullet2(bullet2X, bullet2Y)
        bullet2Y -= bullet2Y_change

    # Boundaries
    if playerX <= 0:
        playerX = 0
    if playerX >= 740:
        playerX = 740

    # Background
    backgroundY += backgroundY_change

    # Player and Enemy
    player(playerX, playerY)
    playerX += playerX_change
    score(textX,textY)
    pygame.display.flip()
