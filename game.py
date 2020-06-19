import pygame, random, math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500, 600))

background = pygame.image.load("background.png")

mixer.music.load("onceagain.mp3")
mixer.music.play(-1)

pygame.display.set_caption("green hat")
icon = pygame.image.load("green hat.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("basket.png")
playerX = 250
playerY = 480
player_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("fruit.png"))
    enemyX.append(random.randint(0, 436))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

v_enemyImg = []
v_enemyX = []
v_enemyY = []
v_enemyX_change = []
v_enemyY_change = []
v_num_of_enemies = 3

for i in range(v_num_of_enemies):
    v_enemyImg.append(pygame.image.load("dictionary.png"))
    v_enemyX.append(random.randint(0, 436))
    v_enemyY.append(random.randint(0, 150))
    v_enemyX_change.append(4)
    v_enemyY_change.append(40)

score_value = 0
font = pygame.font.Font('Lordcorps.ttf', 42)

textX = 10
testY = 10

over_font = pygame.font.Font('Lordcorps.ttf', 42)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (150, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def v_enemy(x, y, i):
    screen.blit(v_enemyImg[i], (x, y))

def collision(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt((math.pow(playerX-enemyX, 2))+(math.pow(playerY-enemyY, 2)))
    if distance < 27:
        return True
    else:
        return False

def v_collision(playerX, playerY, v_enemyX, v_enemyY):
    v_distance = math.sqrt((math.pow(playerX-v_enemyX, 2))+(math.pow(playerY-v_enemyY, 2)))
    if v_distance < 27:
        return True
    else:
        return False

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -9
            if event.key == pygame.K_RIGHT:
                player_change = 9
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    playerX += player_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 436:
        playerX = 436

    for i in range(num_of_enemies):
        enemyY[i] += enemyY_change[i]
        enemyY_change[i] = 0.4

        if v_enemyY[i] > 540:
            for j in range(v_num_of_enemies):
                v_enemyY[j] = 2000
            game_over_text()
            break
        elif enemyY[i] > 540:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        collision_enemy = collision(playerX, playerY, enemyX[i], enemyY[i])
        if collision_enemy:
            score_value += 1
            enemyX[i] = random.randint(0, 436)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    for i in range(v_num_of_enemies):
        v_enemyY[i] += v_enemyY_change[i]
        v_enemyY_change[i] = 0.45

        if v_enemyY[i] > 540:
            for j in range(v_num_of_enemies):
                v_enemyY[j] = 2000
            game_over_text()
            break
        elif enemyY[i] > 540:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        v_collision_enemy = v_collision(playerX, playerY, v_enemyX[i], v_enemyY[i])
        if v_collision_enemy:
            score_value += 2
            v_enemyX[i] = random.randint(0, 436)
            v_enemyY[i] = random.randint(50, 150)

        v_enemy(v_enemyX[i], v_enemyY[i], i)

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()