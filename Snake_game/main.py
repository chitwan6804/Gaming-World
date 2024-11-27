import pygame
import random

x = pygame.init()
pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Creating Windowṅ
screen_width = 900
screen_height = 600
border_size = 30  # Size of the border
gameWindow = pygame.display.set_mode((screen_width, screen_height))

bgimg = pygame.image.load("Snake_game/gallery/pictures/snake.jpg")
bgimg1 = pygame.image.load("Snake_game/gallery/pictures/first page.webp")
bgimg2 = pygame.image.load("Snake_game/gallery/pictures/game_over.webp")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, screen_height)).convert_alpha()
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()

# Game title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])
        if snake_list.index([x,y]) == len(snake_list) - 1:  # Head
            pygame.draw.polygon(gameWindow, green, [(x + snake_size // 2, y),
                                                    (x, y + snake_size),
                                                    (x + snake_size, y + snake_size)])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 210, 229))
        gameWindow.blit(bgimg1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_loop()
        pygame.display.update()
        clock.tick(60)

def game_loop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55

    init_velocity = 5
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(border_size, screen_width - border_size - 30)
    food_y = random.randint(border_size, screen_height - border_size - 30)
    score = 0
    snake_size = 30
    fps = 60

    snake_list = []
    snake_length = 1

    with open("Snake_game/highscore.txt", "r") as f:
        highscore = f.read()

    # Game Loop
    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(bgimg2, (0, 0))
            with open("Snake_game/highscore.txt", "w") as f:
                f.write(str(highscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                pygame.mixer.music.load('Snake_game/gallery/audio/Beep.mp3')
                pygame.mixer.music.play()
                score += 10
                snake_length += 2
                food_x = random.randint(border_size, screen_width - border_size - 30)
                food_y = random.randint(border_size, screen_height - border_size - 30)
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            
            # Draw borders
            pygame.draw.rect(gameWindow, black, [0, 0, screen_width, border_size])  # Top border
            pygame.draw.rect(gameWindow, black, [0, 0, border_size, screen_height])  # Left border
            pygame.draw.rect(gameWindow, black, [0, screen_height - border_size, screen_width, border_size])  # Bottom border
            pygame.draw.rect(gameWindow, black, [screen_width - border_size, 0, border_size, screen_height])  # Right border

            # Display score and high score inside top border
            text_screen("Score: " + str(score) + " Highscore: " + str(highscore), white, border_size + 10, border_size // 2 - 10)

            pygame.draw.circle(gameWindow, red, (food_x + snake_size // 2, food_y + snake_size // 2), snake_size // 2)
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Snake_game/gallery/audio/gameover.mp3')
                pygame.mixer.music.play()

            if snake_x < border_size or snake_x > screen_width - border_size - snake_size or \
               snake_y < border_size or snake_y > screen_height - border_size - snake_size:
                game_over = True
                pygame.mixer.music.load('Snake_game/gallery/audio/gameover.mp3')
                pygame.mixer.music.play()
            
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
