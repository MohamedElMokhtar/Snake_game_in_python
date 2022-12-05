import pygame
import random

# initialize all modules of pygame 
pygame.init()

# colors that we're gonna use in this game color = (red,green,blue) 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)

window_width = 800
window_height = 500

# setting the window's width, height and title 
dis = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game by Mohamed')

# to track time
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# using pygame fonts
font_style = pygame.font.SysFont("bahnschrift", 40)
score_font = pygame.font.SysFont("comicsansms", 20)

# function to display the score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# The length of the snake is contained in a list and the initial size is one block (10 * 10)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


# function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [window_width / 8, window_height / 2])

def gameLoop():
    close_game = False
    game_over = False

    # initial location of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # variables used for moving the snake
    x1_move = 0
    y1_move = 0

    snake_List = []
    Length_of_snake = 1

    # random location of the food
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not close_game:

        while game_over == True:
            # when you lose
            dis.fill(black)
            message("You Lost! Press R to Play Again or Q to Quit", yellow)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # restart game or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        close_game = True
                        game_over = False
                    if event.key == pygame.K_r:
                        gameLoop()

        # for moving the snake 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_move = -snake_block
                    y1_move = 0
                elif event.key == pygame.K_RIGHT:
                    x1_move = snake_block
                    y1_move = 0
                elif event.key == pygame.K_UP:
                    y1_move = -snake_block
                    x1_move = 0
                elif event.key == pygame.K_DOWN:
                    y1_move = snake_block
                    x1_move = 0

        # if the snake hits the boundaries you lose
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True
        
        # updating the snake's position
        x1 += x1_move
        y1 += y1_move
        
        dis.fill(black)
        
        # the food 
        pygame.draw.rect(dis, white, [foodx, foody, 10, 10])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # if the snake hits itself you lose
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        # update the snake and the score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()  
           
        # when the snake hits the food, the food randomly changes location and the snake's size increases by 1 block 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    # uninitialize all modules of pygame
    pygame.quit()
    quit()


gameLoop()