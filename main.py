import pygame
from pygame import mixer

pygame.init()
#creating game window,caption,icon,font
win = pygame.display.set_mode((800,600))
font = pygame.font.SysFont('freesansbold.ttf', 30,True)
pygame.display.set_caption("Ping Pong @PythonIsPie")
icon = pygame.image.load('pongg.png')
pygame.display.set_icon(icon)
#creating player class or paddle
class player_1(object):
    def __init__(self,x,y,width,height,):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel = 14
        self.score = 0

    def draw(self,win): #creating paddle properties
        pygame.draw.rect(win, (169, 131, 123), (self.x,self.y,self.width,self.height))
#creating ball for the game
class projectile(object):
    def __init__(self, x,y,radius,color):#properties of ball
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel1 = 16
        self.vel2= -16
    def draw(self,win):#creating ball 
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


#defining a new function where we will draw whole thing on window
def draw_on_win():
    text1 =font.render('PLAYER_1:' + str(paddle_a.score) ,1,(255,255,255))#player score
    win.blit(text1, (170,10))#sticking it on window
    text2 =font.render('PLAYER_2:' + str(paddle_b.score) ,1,(255,255,255))
    win.blit(text2, (570,10))
    paddle_a.draw(win)#drawing paddle a on window
    paddle_b.draw(win)#drawing paddle b on window
    pygame.draw.line(win, (255,255,255),(400,0),(400,600))#drawing a seperate line to sep
    ball.draw(win)#drawing ball on window
    pygame.display.update()#updating the window each time



ball = projectile(400,300,25,(192,192,192))#calling the projectile class
paddle_a = player_1(10,225,25,150)#calling the player_1 class
paddle_b=player_1(765,225,25,150)#calling the player_1 class
run=True

while run:
    pygame.time.delay(100)
    ball.x+=ball.vel1
    ball.y+=ball.vel2
    if ball.y<25:
        ball.vel2*=-1
        ball_sound=mixer.Sound("hit.wav")
        ball_sound.play()
    if ball.y>575:
        ball.vel2*=-1
        ball_sound=mixer.Sound("hit.wav")
        ball_sound.play()
    if ball.x<5:
        ball.x,ball.y = 400,300
        ball.vel1 *= -1
        paddle_b.score +=1
        print(paddle_b.score)
        
    
    if ball.x>795:
        ball.x,ball.y = 400,300
        ball.vel1 *= -1
        paddle_a.score+=1
        print(paddle_a.score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.y>0:
        paddle_a.y -= paddle_a.vel
    if keys[pygame.K_s] and paddle_a.y<449:
        paddle_a.y += paddle_a.vel

    if keys[pygame.K_UP] and paddle_b.y>0:
        paddle_b.y -= paddle_b.vel
    if keys[pygame.K_DOWN] and paddle_b.y<449:
        paddle_b.y += paddle_b.vel
    if ball.x <paddle_a.x + 45 and (ball.y > paddle_a.y and ball.y<paddle_a.y+150):
        ball.vel1 *= -1
        ball_sound=mixer.Sound("hit.wav")
        ball_sound.play()
        

    if ball.x >paddle_b.x -28 and (ball.y > paddle_b.y and ball.y<paddle_b.y+150):
        ball.vel1 *= -1
        ball_sound=mixer.Sound("hit.wav")
        ball_sound.play()
    win.fill((0,0,0))
    draw_on_win()
pygame.quit()
