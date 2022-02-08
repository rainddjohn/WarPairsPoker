import pygame

def redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain):
    # redraws screen using updated information
    screen.fill(background_color)
    displayhand1(player1, main, altreveal, screen, play)
    displayhand2(player2, main, altreveal, screen, play2)
    displayfplay(fplay, screen)
    if lastmouse1 !=[0,0] and main!=[-3,-3]:
        pygame.draw.line(screen, (255, 255, 255), [lastmouse1[0] - 3, lastmouse1[1] + 75],[lastmouse1[0] + 3, lastmouse1[1] + 75],width=2)
    # disallows vision of the pile list while you're not allowed to see it
    displaypile(pile, screen,main)
    #gameend
    main,player1,player2=gameend(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,pile,concede,backupmain)
    loadmainbuttons(main,screen, p1redraw,p2redraw,AI)
    pygame.display.update()
    return player1, player2,main

def gameend(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,pile,concede,backupmain):
    #checks to see if the game is over
    if backupmain==[0,0] and concede==True: player1.clear()
    if backupmain[0] == 1 and concede == True: player2.clear()
    if backupmain[0] == 2 and concede == True: player1.clear()
    if len(player1) == 26: player2.clear()
    if len(player2) == 26: player1.clear()
    if len(player1) == 0:
        main = [-2, 0];screen.fill(background_color)
        displayhand1(player1, main, altreveal, screen, play)
        displayhand2(player2, main, altreveal, screen, play2)
        displayfplay(fplay,screen)
        displaypile(pile,screen,main)
        a = pygame.image.load('ponewin.png');screen.blit(a, (380, 480));pygame.display.update()
        return main,player1,player2
    if len(player2) == 0:
        main = [-3, 0];screen.fill(background_color)
        displayhand1(player1, main, altreveal, screen, play)
        displayhand2(player2, main, altreveal, screen, play2)
        displayfplay(fplay,screen)
        displaypile(pile,screen,main)
        a = pygame.image.load('ptwowin.png');screen.blit(a, (380, 50));pygame.display.update()
        return main,player1,player2
    return main, player1, player2

def displayhand1(player1, main, altreveal, screen, play):
    y = 0
    # placement on the screen, loads bottom hand
    while y < len(player1):
        card = player1[y]
        selectionadjustment = 0
        if altreveal == True and main[0] == 2:x = pygame.image.load('blueback.png')
        else: x = pygame.image.load(f'{card}.png')  ####loads images
        if y < 13:
            if card in play: selectionadjustment = 20
            screen.blit(x, (20 + y * 75, 450 - selectionadjustment))
        # second row
        else:
            if card in play: selectionadjustment = 20
            screen.blit(x, (20 + (y - 13) * 75, 603 - selectionadjustment))
        y += 1
    #return player1, main, altreveal, screen, play

def displayhand2(player2, main, altreveal, screen, play2):
    y=0
    # placement on the screen, loads top hand
    while y < len(player2):
        card=player2[y];selectionadjustment=0
        if altreveal==True and main[0] == 1: x = pygame.image.load('blueback.png')
        else:x=pygame.image.load(f'{card}.png')          ####loads images
        if y<13:
            if card in play2: selectionadjustment = 15
            screen.blit(x, (20+y*75,20-selectionadjustment))
        #second row
        else:
            if card in play2: selectionadjustment = 15
            screen.blit(x, (20 + (y-13) * 75, 133+selectionadjustment))
        y+=1
    #return player2, main, altreveal, screen, play2

def displayfplay(fplay,screen):
    y = 0
    #shows played cards
    while y < len(fplay):
        card = fplay[y]
        x = pygame.image.load(f'{card}.png')  ####loads images
        if y < 13:
            screen.blit(x, (230 + y * 75, 280))
        y += 1
    #return fplay, screen

def displaypile(pile,screen,main):
    if main[0] <1:return
    x = 0;y = 0
    #shows side drawable pile
    while y < len(pile):
        card = pile[y]
        x = pygame.image.load(f'{card}.png')  ####loads images
        if y < 6:
            screen.blit(x, (750 + y * 37, 270))
        else:
            screen.blit(x, (750 + (y-6) * 37, 297))
        y += 1
    #return pile,screen

def loadmainbuttons(main,screen, p1redraw,p2redraw,AI):
    #loads button picutres according to thier legality governed by the variable (main)
    a = pygame.image.load('optionslong.png');screen.blit(a, (10, 323))
    if main[0]==1:
        a=pygame.image.load('arrowdown.png');screen.blit(a,(80,260))
    if main[0]==2:
        a=pygame.image.load('arrowup.png');screen.blit(a,(80,260))
    if main==[0,0]or main==[-1,0]:
        a=pygame.image.load('mulligan.png');screen.blit(a,(120,323))
    if main[1]==0 and main[0] !=0:
        a = pygame.image.load('play.png');screen.blit(a, (120, 323))
    if main[1]==1:
        a = pygame.image.load('play.png');screen.blit(a, (120, 323))
        a = pygame.image.load('passturn.png');screen.blit(a, (120, 280))
    if main[1]==2:
        a = pygame.image.load('play.png');screen.blit(a, (120, 323))
        a = pygame.image.load('draw.png');screen.blit(a, (640, 323))
    if main[1]==3:
        a = pygame.image.load('draw.png');screen.blit(a, (640, 323))
        a = pygame.image.load('ok.png');screen.blit(a, (120, 323))
        if p1redraw==True and main[0]==1: a = pygame.image.load('redraw.png');screen.blit(a, (640, 280))
        if p2redraw == True and main[0]==2: a = pygame.image.load('redraw.png');screen.blit(a, (640, 280))
    if main[1]==4:
        a = pygame.image.load('ok.png');screen.blit(a, (120, 323))
        if p1redraw==True and main[0]==1: a = pygame.image.load('redraw.png');screen.blit(a, (640, 280))
        if p2redraw == True and main[0]==2: a = pygame.image.load('redraw.png');screen.blit(a, (640, 280))
    if main[0]==2 and AI==True:
        a = pygame.image.load('compplay.png');screen.blit(a, (120, 323))



def optionwindow(screen,background_color,concede,optionslist, altreveal,showthis,showlast,AI,automull):
    #pictures for the options menu buttons
    screen.fill(background_color);a=pygame.image.load('back.png');screen.blit(a, (10, 323));a=pygame.image.load('undo.png');screen.blit(a, (10, 262))
    if optionslist[0]==0: a=pygame.image.load('showthisoff.png');screen.blit(a, (10, 384))
    else: a=pygame.image.load('showthison.png');screen.blit(a, (10, 384));displayshowstuff(showthis,screen)
    if optionslist[1]==0: a=pygame.image.load('showlastoff.png');screen.blit(a, (10, 445))
    else: a=pygame.image.load('showlaston.png');screen.blit(a, (10, 445));displayshowstuff(showlast,screen)
    if altreveal==False: a = pygame.image.load('altrevealoff.png');screen.blit(a, (10, 506))
    else: a = pygame.image.load('altrevealon.png');screen.blit(a, (10, 506))
    a =pygame.image.load('rules.png');screen.blit(a, (10, 567))
    if optionslist[3]==1: a =pygame.image.load('ruleslist.png');screen.blit(a, (250, 200));a =pygame.image.load('banner.png');screen.blit(a, (380, 10))
    if optionslist[4]==0: a = pygame.image.load('concede.png');screen.blit(a, (10, 628))
    elif optionslist[4]==1:  a = pygame.image.load('areyousure.png');screen.blit(a, (10, 628))
    if optionslist[2]==0:a = pygame.image.load('replaygame.png');screen.blit(a, (10, 201))
    elif optionslist[2]==1: a = pygame.image.load('areyousure.png');screen.blit(a, (10, 201))
    if not AI: a = pygame.image.load('compoff.png');screen.blit(a, (10, 140))
    else: a = pygame.image.load('compon.png');screen.blit(a, (10, 140))
    if not automull: a = pygame.image.load('automulloff.png');screen.blit(a, (10, 79))
    else:a = pygame.image.load('automullon.png');screen.blit(a, (10, 79))
    pygame.display.update()
    return concede,optionslist, altreveal,showthis,showlast,AI,automull

def displayshowstuff(list,screen):
    y=0
    #displays cards for showthishand option and show last hand option
    while y < len(list):
        card = list[y]
        x = pygame.image.load(f'{card}.png')
        if y < 11: screen.blit(x, (170 + y * 75, 20))
        if 11 <= y <= 23: screen.blit(x, (170 + (y - 13) * 75, 133))
        if 24 <= y <= 36: screen.blit(x, (170 + (y - 26) * 75, 246))
        y += 1