import basic as basic;import display as display;import buttons as buttons
import pygame;deck=[];import random; player1=[]; player2=[];play=[];play2=[];fplay=[];pile=[];main=[0,0];gamemode=[0,0,0]
pygame.init()
p1redraw=True;p2redraw=True
showthis=[];showlast=[];backupmain=[0,0];optionslist=[0,0,0,0,0,0];used=[];log=[];concede=False;backupdeck=[];altreveal=False;replay=False; AI=True
(width,height)=(1033,750);background_color= (84,119,44);screen=pygame.display.set_mode((width,height));screen.fill(background_color);pygame.display.set_caption('WarPairsPoker v1')
###mulligan and segment AI variables
import copy;n2akout=[];hardmull=[];mullnotes=[];outliers=[];quads=[];mull=[];segp2=[[],[],[],[],[],[],[],[],[]];copyseg=[];finalseg=[];p2copy=[]
automull=True;lastmouse1=[0,0];AIinfo=[False,False,False,False,False,0,[],False];hand=[]

pygame.display.update()

#basic.startgame
player1, player2, deck, backupdeck, main, gamemode, p1redraw, p2redraw, showlast, showthis, used, log, concede,\
    optionslist, AIinfo, play, play2, fplay, pile, altreveal, screen, background_color, \
    lastmouse1, AI, backupmain=basic.startgame(player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,
    showthis,used,log,concede,optionslist,AIinfo,play,play2,fplay,pile,altreveal, screen,background_color,lastmouse1,AI,backupmain)

#display.redrawgamewindow
player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,
                         p1redraw,p2redraw,AI,concede,backupmain)

pygame.display.flip();running= True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False;pygame.quit();exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #buttons.buttons
            player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log\
                ,p1redraw,p2redraw,deck,used,replay,backupdeck,concede,optionslist,AIinfo,gamemode,showthis,showlast,\
                backupmain,automull,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,finalseg=buttons.buttons\
                (mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI
                 ,log,p1redraw,p2redraw,deck,used,replay,backupdeck,concede,optionslist,AIinfo,gamemode,showthis,showlast
                 ,backupmain,automull,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,p2copy,segp2,copyseg,finalseg)
        mouse = pygame.mouse.get_pos()