import pygame
import time
import random
import RPi.GPIO as GPIO

servoPIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
 
pygame.init()#initialize pygame
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0)
 
white = (255, 255, 255)#make pretty colors
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (200, 50, 100)
green = (0, 255, 0)
blue = (50, 150, 200)
 
dis_width = 600 #setup display
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10#size of snake block
snake_speed = 15#i am speed
 
font_style = pygame.font.SysFont("arial", 25)#arial>times new roman
score_font = pygame.font.SysFont("arial", 35)
 
def our_snake(snake_block, snake_list): #making snake from list
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop(): #main loop
    game_over = False #initiallizing all parts
    game_close = False 
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    snake_Length = 1
    scolor = red
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("Game over! Press P-Play Again or Q-Quit", black)
 
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #movement
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            if event.type == pygame.QUIT:
                game_over = True
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
      #  if (scolor % 2) == 0: #changes color everytime
       #     snakecolor = red
      #  else:
       #     snakecolor = green
        pygame.draw.rect(dis, scolor, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_Length:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)

 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody: #when fruit is touched
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_Length += 1
            r = random.randint(0,255) #randomize color everytime fruit is touched
            g = random.randint(0,255)
            b = random.randint(0,255)
            scolor = [r,g,b]
            p.ChangeDutyCycle(6)
            time.sleep(0.3)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.3)
            p.ChangeDutyCycle(6)
            time.sleep(0.3)
            p.ChangeDutyCycle(0)
            time.sleep(0.3)
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
