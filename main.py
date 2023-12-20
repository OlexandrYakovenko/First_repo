from asyncio import sleep
import sys
#print (sys.path)
import os
import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana',28)

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_BLUE = (0,0,255)
COLOR_RED = (255,0,0)
COLOR_GREEN = (0,255,0)

PLAYER_SIZE = (20,20)
IMAGES_PATH="Pictures/Goose"
PLAYER_IMAGES=os.listdir(IMAGES_PATH)
#print(PLAYER_IMAGES)

main_display = pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.transform.scale(pygame.image.load("Pictures/background.png"),(WIDTH,HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

#player = pygame.Surface(PLAYER_SIZE) 
player = pygame.image.load("Pictures/player.png").convert_alpha()
#player.fill(COLOR_WHITE)
#player.fill(COLOR_BLACK)

player_rect = player.get_rect()
#player_rect=player_rect.move([player_rect.width/2,HEIGHT/2])
player_rect.center = main_display.get_rect().center
#player_rect.height = HEIGHT / 2
player_speed = [6,6]
player_move_down = [0,6]
player_move_right = [6,0]
player_move_left = [-6,0]
player_move_up = [0,-6]

name_audio_file="Beethoven_-_Sonata_opus_111_-2.ogg"
pygame.mixer.music.load(name_audio_file)#'Beethoven.ogg'
pygame.mixer.music.play()
sound_boom = pygame.mixer.Sound('mixkit-short-explosion-1694.wav') #'boom.wav'
#sound_boom.play()
sound_short = pygame.mixer.Sound('button-124476.mp3')

def create_enemy():
    ENEMY_SIZE = (30,30)
    # enemy = pygame.Surface(ENEMY_SIZE)
    # enemy.fill(COLOR_BLUE)
    enemy = pygame.image.load("Pictures/enemy.png").convert_alpha()
    enemy_height = enemy.get_height()
    x = WIDTH #WIDTH - enemy_height
    y = random.randint(enemy_height,HEIGHT-enemy_height)
    enemy_rect = pygame.Rect(x,y,*enemy.get_size())
    enemy_move = [random.randint(-8,-4),0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    BONUS_SIZE = (30,30)
    # bonus = pygame.Surface(BONUS_SIZE)
    # bonus.fill(COLOR_GREEN)
    bonus = pygame.image.load("Pictures/bonus.png").convert_alpha()
    bonus_width = bonus.get_width()
    bonus_height = bonus.get_height()
    x = random.randint(bonus_width,WIDTH-bonus_width)
    y = -bonus_height
    bonus_rect = pygame.Rect(x,y,*bonus.get_size())
    bonus_move = [0,random.randint(4,8)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = CREATE_ENEMY + 1
pygame.time.set_timer(CREATE_BONUS, 1500)

CHANGE_IMAGE = CREATE_BONUS + 1
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonuses = []

score = 0
image_index = 0

PLAYING = True
while PLAYING:
    FPS.tick(160)
    for event in pygame.event.get():
        if event.type == QUIT:
            PLAYING = False 
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGES_PATH,PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
    # main_display.fill(COLOR_BLACK) 
    bg_X1 -= bg_move
    bg_X2 -= bg_move
    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()
    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()    
    main_display.blit(bg,(bg_X1,0))
    main_display.blit(bg,(bg_X2,0))
    
    keys = pygame.key.get_pressed()
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect=player_rect.move(player_move_down)
    if keys[K_UP] and player_rect.top >= 0:
        player_rect=player_rect.move(player_move_up) 
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect=player_rect.move(player_move_right)        
    if keys[K_LEFT] and player_rect.left >= 0:
        player_rect=player_rect.move(player_move_left)
    
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2]) #enemy_rect, enemy_move
        main_display.blit(enemy[0],enemy[1])
        if player_rect.colliderect(enemy[1]):
            # print("Boom")
            print("Score=",score)
            sound_boom.play()
            #sleep(100000)
            pygame.time.delay(2000)
            PLAYING=False
            sys.exit()
    
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2]) #bonus_rect, bonus_move
        main_display.blit(bonus[0],bonus[1])
        if player_rect.colliderect(bonus[1]):
            # print("Yep")
            score += 1
            sound_short.play()
            bonuses.pop(bonuses.index(bonus))
    
    #main_display.blit(FONT.render(str(score),True,COLOR_WHITE),(WIDTH-50,20))
    main_display.blit(FONT.render("Score="+str(score),True,COLOR_RED),(WIDTH-200,20))
    main_display.blit(player,player_rect)
    
    # print("enemies=" , len(enemies))
    # print("bonuses" , len(bonuses))
    pygame.display.flip()
    for enemy in enemies:
        if enemy[1].right <0:
            enemies.pop(enemies.index(enemy))
    for bonus in bonuses:
        if bonus[1].bottom >HEIGHT:
            bonuses.pop(bonuses.index(bonus))                 