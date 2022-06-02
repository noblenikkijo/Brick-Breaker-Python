#has multiple balls, 1 paddle,  multiple bricks , and  1 overlay, health, score
#For those state with multiple create a sprit group, pygame.sprite.spritegroup (balls and bricks)

import random
import sys
import pygame as pg
from Paddle import Paddle
from Ball import Ball
from Overlay import Overlay
from Brick import Brick

pg.init()

# Set up background music
file = 'pyGame_Music.mp3'
pg.mixer.init()
pg.mixer.music.load(file)
pg.mixer.music.play(-1)

#Open a new window
screen = pg.display.set_mode((800,600))
pg.display.set_caption ("BREAKOUT")

#create paddle
paddle = Paddle()
paddle.rect.x = 20
paddle.rect.y = 550

# create ball
ball = Ball()
ball.rect.x = 345
ball.rect.y = 195

sprites = pg.sprite.Group()

bricks = pg.sprite.Group()
for i in range(28):
    r = random.randint(50, 200)
    g = random.randint(50, 200)
    b = random.randint(50, 200)
    brick = Brick((r, g, b))
    brick.rect.x = (i%9)*90

    if(i <= 9):
        brick.rect.y = 60
    elif(i >= 19):
        brick.rect.y = 140
    else:
        brick.rect.y = 100
    sprites.add(brick)
    bricks.add(brick)

#sprites list
# Add the paddle

overlay = Overlay()

sprites.add(paddle)
sprites.add(ball)
# sprites.add(bricks)


#clock controls speed of screen updates
clock = pg.time.Clock()
#running until user exits
running = True
score = 0;
lives = 3;

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Moving the paddle when the use uses the arrow keys
    arrows = pg.key.get_pressed()
    if arrows[pg.K_LEFT]:
        paddle.moveLeft()
    if arrows[pg.K_RIGHT]:
        paddle.moveRight()
        
    sprites.update()
    overlay.update(screen)
    
    #Check if the ball hits a wall
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
        lives -= 1
        if lives == 0:
            font = pg.font.Font(None, 74)
            text = font.render("GAME OVER", 1, (0,0,0))
            screen.blit(text, (250,300))
            pg.display.flip()
            pg.time.wait(3000)
            #Stop the Game
            running=False
 
    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]
 
    #Detect collisions between the ball and the paddles
    if pg.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()
 
    #Check if there is the ball collides with any of bricks
    brickCollisions= pg.sprite.spritecollide(ball,bricks,False)
    for brick in brickCollisions:
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()
        score += 1
        brick.kill()
        if len(bricks)==0:
           #Display Level Complete Message for 3 seconds
            font = pg.font.Font(None, 74)
            text = font.render("WINNER", 1, (0,0,0))
            screen.blit(text, (200,300))
            pg.display.flip()
            pg.time.wait(3000)
            #Stop the Game
            running=False
            
    screen.fill((255, 255, 255))
    pg.draw.line(screen, (0, 0, 0), [0, 38], [800, 38], 2)
    sprites.draw(screen)
    for brick in bricks:
        brick.draw(screen)
 
    pg.display.flip()
    
    clock.tick(60)

pg.quit()
sys.exit(0)