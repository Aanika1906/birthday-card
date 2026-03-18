import pygame
import time
pygame.init()
screen=pygame.display.set_mode((600,600))

pygame.display.set_caption("Birthday Card")#give window title
imageone=pygame.image.load("l5-birthdaycard/mainpage.jpg")#load the image
finalimage=pygame.transform.scale(imageone,(600,600))#resizes the image to the screen size






while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    font=pygame.font.SysFont("Serif",50)#decide the font and size
    text=font.render("Happy Birthday:)  ",True,"purple")#writes it on the screen #
    textwo=font.render("Have a good day",True ,"purple")
    screen.fill("black")
    screen.blit(finalimage,(0,0))#adding final image
    screen.blit(text,(140,200))#adding the text
    screen.blit(textwo,(140,280))#adding the text
    pygame.display.update()#updates the screen
    time.sleep(2)#It wil stay for two seconds

    imagetwo=pygame.image.load("l5-birthdaycard/gift.jpg")#load the image
    finimage=pygame.transform.scale(imagetwo,(600,600))#resizes the image to the screen size
    font=pygame.font.SysFont("Serif",50)#decide the font and size
    textt=font.render("Hope you like your gift  ",True,"purple")#writes it on the screen 
    screen.fill("black")
    screen.blit(finimage,(0,0))#adding final image
    screen.blit(textt,(110,180))#adding the text
    pygame.display.update()#updates the screen
    time.sleep(2)#It wil stay for two seconds
    
    imagethree=pygame.image.load("l5-birthdaycard\cake.jpg")#load the image
    fimage=pygame.transform.scale(imagethree,(600,600))#resizes the image to the screen size
    font=pygame.font.SysFont("Serif",50)#decide the font and size
    textth=font.render("Enjoy your cake  ",True,"purple")#writes it on the screen 
    screen.fill("black")
    screen.blit(fimage,(0,0))#adding final image
    screen.blit(textth,(110,400))#adding the text
    pygame.display.update()#updates the screen
    time.sleep(2)#It wil stay for two seconds

