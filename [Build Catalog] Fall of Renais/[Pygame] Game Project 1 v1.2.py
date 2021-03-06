import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,176,80)

bright_red = (255,96,96)
bright_green = (96,255,96)

block_color = (200,249,251)

Eirika_width = 50
Eirika_height = 70

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Game Project 1")
clock = pygame.time.Clock()



EirikaImg = pygame.image.load('eirika_masterlord_sword (1).png')



def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def Eirika(x,y):
    gameDisplay.blit(EirikaImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    
    time.sleep(2)

    game_loop()



    
def crash():
    message_display('You Died')

def button(msg,x,y,w,h,ic,ac,action=None):
    #ic = Inactive Color
    #ac = Active Color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)

    if x+w > mouse[0] >x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] ==1 and action !=None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
        
    gameDisplay.blit(textSurf, textRect)

def quit_game():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Game Project 1", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Start!", 150,450,100,50, green, bright_green,game_loop)
        button("Quit...", 550,450,100,50, red, bright_red,quit_game)
        
        pygame.display.update()
        clock.tick(15)
    
def game_loop():
    x = (display_width * 0.8)
    y = (display_height * 0.8)

    x_change = 0


    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 10
    thing_width = 100
    thing_height = 100

    dodged = 0
    
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change



        gameDisplay.fill(white)

        #thing(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        Eirika(x,y)
        things_dodged(dodged)

        if x > display_width - Eirika_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed +=1
            thing_width += (dodged * 1.2)
            

        if y + Eirika_height > thing_starty and y < thing_starty + thing_height:
            #print('Y Crossover')
                
            if x + Eirika_width > thing_startx and x < thing_startx + thing_width:
                #print('X Crossover')
                crash()

##        if y < thing_starty + thing_height:
##            #print('Y Crossover')
##                
##            if x + Eirika_width > thing_startx and x < thing_startx + thing_width:
##                #print('X Crossover')
##                crash()






        pygame.display.update()
        clock.tick(30)

game_intro()
game_loop()
pygame.quit()
quit()
