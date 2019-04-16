#import game
import pygame
import random


#initialize
pygame.init()



#here is where we define the images
imageone = pygame.image.load('flappy.png')
imageone = pygame.transform.scale(imageone, (90,40))
imagetop = pygame.image.load('pipe.png')
imagetop = pygame.transform.scale(imagetop, (30,20))

#screen.blit(imgTop,(xloc,yloc))
#screen.blit(imgBottom,(xloc,yloc))



#define colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (78,66,244)
red = (255,0,0)
skyblue = (0,191,255)



#define screen size
size = (500,600)
screen = pygame.display.set_mode(size)



#define screen title
pygame.display.set_caption("Flappy bird")



#boolean to control game logic
done= False



#set speed
clock = pygame.time.Clock()
x = 100
y = 250
x_speed = 0
y_speed = 15



#x axis 
xloc = 500

#y axis
yloc = 0 

#width of blocks
xsize = 70

#random generator
ysize = random.randint(0,350)

#space between blocks
space = 150

#speed
obspeed = 15

#global position 
ground = 500

#score keeper 
score = 0

def obstacles(xloc,yloc,xsize,ysize):

    #here is where then images get called for pipes

    imgTop = pygame.image.load('pipe.png')



    imgBottom = pygame.image.load('pipe.png')



    imgTop = pygame.transform.rotate(imgTop, 180)



    imgTop = pygame.transform.scale(imgTop, (xsize, ysize))



    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))



    



    screen.blit(imgTop, (xloc, yloc))



    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)))





    #pygame.draw.rect(screen,red, [xloc,yloc,xsize,ysize])

    #pygame.draw.rect(screen, red,[xloc,int(yloc+ysize+space),xsize,ysize+500])





#define function to draw circle
def ball(x,y,image):

    screen.blit(image, (x,y))

    #pygame.draw.circle(screen,green,(x,y),20)


#Game Over
def gameover():

    font= pygame.font.SysFont(None,25)

    text = font.render("Game over",True,red)

    screen.blit(text,[150,250])

    



#function to keep score
def Score(score):

    font = pygame.font.SysFont(None,75)

   

   #we use str to convert score value to string
    text = font.render("Score: "+str(score),True,black)

    screen.blit(text, [20,20])



    

    

#while logic that keeps game running
while not done:

    

    #capture input events so we can act upon it
    for event in pygame.event.get():

      

      #if user select escape key or press windows X 
        if event.type == pygame.QUIT:

            done = True

        #VERTICAL
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                y_speed= -10

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:

              y_speed = 10

        

        #HORIZONTAL
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

              x_speed = -10

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:

              x_speed = 10

        

    screen.fill(skyblue)

   

   #draw obstacles
    obstacles(xloc,yloc,xsize,ysize)

    

    #draw balL
    ball (x,y,imageone)

    

    #if the ball is between two obstacles
    Score(score)

    y += y_speed

    x += x_speed

    xloc -= obspeed

    

    #obstacle hit top
    if x+20 > xloc and y-20 < ysize and x-15 < xsize+xloc:

        y_speed = 2

        gameover()

        obspeed = 0

      

   

       #bottom block
    if x+20 > xloc and y+20> ysize+space and x-15 < xsize+xloc:

       y_speed = 2

       gameover()

       obspeed = 0

       

   

        #loop for making obstacle
    if xloc < -80:

        xloc = 500

        ysize =  random.randint(0,350)

    

        #ADDS SCORE
    if x>xloc and x < xloc+3:

        score = (score + 1 )

   

       #hit the ground and youre done 
    if y >ground:

        gameover()

        obspeed = 0

        y_speed = 0

    

    #keeps game moving
    pygame.display.flip()

    

    #define fps 
    clock.tick(1000)



#once logic ends
pygame.quit()
