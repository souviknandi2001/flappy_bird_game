import pygame
from pygame import mixer
import random
import time
pygame.init()
global c
c=0


screen = pygame.display.set_mode((300,500))
background = pygame.image.load("gamebackground.jpg")
mixer.music.load('backgroundmusic.wav')
mixer.music.play(-1)

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10
def show_score(x, y):
    score = font.render("SCORE : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))
# game over text
over_font = pygame.font.Font('freesansbold.ttf', 35)
def game_over_text():

    over_text = over_font.render(' GAME OVER ' ,True, (255, 25, 255))
    screen.blit(over_text, (30, 250))
    gameoverSound = mixer.Sound("gameover.wav")
    gameoverSound.play()
    time.sleep(3)
    return  False


# pipe
pipe1 = pygame.image.load('pipe.png')
pipe2 = pygame.image.load('pipe1.png')
pipe1y =random.randint(290,350)
pipe1x= 75
pipe2x= 150
pipe3x= 225
pipe4x= 300
pipe2y =random.randint(290,350)
pipe3y =random.randint(290,350)
pipe4y =random.randint(290,350)

pc=.5

#  player
player  = pygame.image.load('player.png')
playerx=40
playery=250
player_change = 1


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance1 = enemyY-bulletY
    if distance1 < 1:
        return True
    elif distance1 >150:
        return True
    else:
        return False

running = True

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        # controll player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_change=-1
            else:
                player_change=1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_change = 1



    playery+=player_change
    screen.blit(player,(playerx,playery))

    pipe1x -= pc
    if pipe1x<0:
        score_value += 1
        point= mixer.Sound('point.wav')
        point.play()
        pipe1x=300
        pipe1y=random.randint(280,350)
    else:
        screen.blit(pipe1,(pipe1x,pipe1y))
        screen.blit(pipe2, (pipe1x, ((228-(500-pipe1y)-80))))
        y = ((228 - (500 - pipe1y) - 80))
    collision = isCollision(y, pipe1y, playerx, playery)
    #if collision:
        #hit = mixer.Sound('hit.wav')
        #hit.play()
        #running = game_over_text()



    pipe2x -= pc
    if pipe2x < 0:
        point= mixer.Sound('point.wav')
        point.play()
        score_value += 1
        pipe2x = 300
        pipe2y = random.randint(280, 350)
    else:
        screen.blit(pipe1, (pipe2x, pipe2y))
        screen.blit(pipe2, (pipe2x, ((228-(500-pipe2y)-80))))
        y1 = ((228 - (500 - pipe2y) - 80))
    collision = isCollision(y1, pipe2y, playerx, playery)
    if collision:
        hit = mixer.Sound('hit.wav')
        hit.play()
        running = game_over_text()



    pipe3x -= pc
    if pipe3x < 0:
        point= mixer.Sound('point.wav')
        point.play()
        score_value += 1
        pipe3x = 300
        pipe3y = random.randint(280, 350)
    else:
        screen.blit(pipe1, (pipe3x, pipe3y))
        screen.blit(pipe2, (pipe3x,  ((228-(500-pipe3y)-80))))
        y2 = ((228 - (500 - pipe1y) - 80))
    collision = isCollision(y2, pipe3y, playerx, playery)
    if collision:
        hit = mixer.Sound('hit.wav')
        hit.play()
        running = game_over_text()


    pipe4x -= pc
    if pipe4x < 0:
        point= mixer.Sound('point.wav')
        point.play()
        score_value += 1
        pipe4x = 300
        pipe4y = random.randint(280, 350)
    else:
        screen.blit(pipe1, (pipe4x, pipe4y))
        screen.blit(pipe2, (pipe4x, ((228-(500-pipe4y)-80))))
        y3 = ((228 - (500 - pipe1y) - 80))

    collision = isCollision(y3, pipe4y, playerx, playery)
    if collision:
        hit = mixer.Sound('hit.wav')
        hit.play()
        running = game_over_text()

    show_score(textX,textY)
    pygame.display.update()