import pygame
import random
import os
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('start.wav')
pygame.mixer.music.play(-1)


white= pygame.Color(255,255,255)
red= pygame.Color(255,0,0)
black= pygame.Color(0,0,0)
carrot= (237,145,33)
green= (118,238,0)
blue= (151,255,255)
orange= (255,127,0)

screen_width= 1200
screen_height= 600
gameWindow= pygame.display.set_mode((screen_width, screen_height))
bgimg= pygame.image.load('img.jpg')
bgimg= pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Snake game with S.K.S.")
pygame.display.update()

clock= pygame.time.Clock()
font= pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
     screen_text= font.render(text, True, color)
     gameWindow.blit(screen_text, [x,y])
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y  in snk_list:
     pygame.draw.rect(gameWindow, red, [x, y, snake_size, snake_size])
def welcome():
    exit_game= False
    while not exit_game:
        bgimg1 = pygame.image.load('welcm.jpg')
        bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
        gameWindow.blit(bgimg1, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                exit_game= True
                pygame.quit()
            if event.type== pygame.KEYDOWN:
             if event.key== pygame.K_SPACE:
                pygame.mixer.music.load('back.wav')
                pygame.mixer.music.play(-1)
                gameloop()
            pygame.display.update()
            clock.tick(60)


def gameloop():
    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    fps = 50
    food_x = random.randint(20, screen_width / 3)
    food_y = random.randint(20, screen_height / 3)
    Score = 0
    init_velocity = 5
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write(0)
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            bgimg2 = pygame.image.load('over.jpg')
            bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(bgimg2, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        pygame.mixer.music.load('start.wav')
                        pygame.mixer.music.play()
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT or event.key== pygame.K_d:
                       velocity_x= 7
                       velocity_y= 0
                    if event.key == pygame.K_LEFT or event.key== pygame.K_a:
                        velocity_x=  -7
                        velocity_y= 0
                    if event.key == pygame.K_UP or event.key== pygame.K_w:
                        velocity_y=  -7
                        velocity_x= 0
                    if event.key == pygame.K_DOWN or event.key== pygame.K_s:
                       velocity_y= 7
                       velocity_x= 0
                    if event.key== pygame.K_q:
                        Score += 10
                    if event.key== pygame.K_r:
                        Score -= 5
            snake_x = snake_x + velocity_x
            snake_y= snake_y +velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                Score+= 10
                food_x = random.randint(20, screen_width / 3)
                food_y = random.randint(20, screen_height / 3)
                snk_length += 5
            if Score>int(highscore):
                highscore= Score
            gameWindow.fill(green)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score: " + str(Score) + " |  Highscore: "+ str(highscore), black, 5, 5)
            pygame.draw.rect(gameWindow, carrot, [food_x, food_y, snake_size, snake_size])
            head= []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)> snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over= True
                pygame.mixer.music.load('over.wav')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over= True
                pygame.mixer.music.load('over.wav')
                pygame.mixer.music.play()
            plot_snake(gameWindow, red, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()
