import pygame
import time
import random

# initialize all modules of pygame 
pygame.init()

# colors that we're gonna use in this game (red,green,blue) 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# setting height, width and title of the window 
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game by Mohamed')

# to track time 
clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    window.blit(value, [0, 0])

# The length of the snake is contained in a list and the initial size that is one block (10*10)
def our_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_size, snake_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

def gameLoop():
    close_game = False
    game_over = False

    x = window_width / 2
    y = window_height / 2

    x_move = 0
    y_move = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0

    while not close_game:

        while game_over == True:
            window.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close_game = True
                        game_over = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -snake_size
                    y_move = 0
                elif event.key == pygame.K_RIGHT:
                    x_move = snake_size
                    y_move = 0
                elif event.key == pygame.K_UP:
                    y_move = -snake_size
                    x_move = 0
                elif event.key == pygame.K_DOWN:
                    y_move = snake_size
                    x_move = 0

        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_over = True
        x += x_move
        y += y_move
        window.fill(blue)
        pygame.draw.rect(window, green, [foodx, foody, snake_size, snake_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        # update the size of the snake 
        our_snake(snake_size, snake_List)
        # update the score displayed 
        Your_score(Length_of_snake - 1)

        pygame.display.update()  

        # when the snake hits the food (eats it) : the food takes another position and the snake's size increases     
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, window_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
