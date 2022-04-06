import pygame

def redrawgamewindow(screen,game):
    # redraws screen using updated information
    screen.fill(game.background_color)
    displayhand1(screen,game)
    displayhand2(screen,game)
    displayfplay(screen,game)
    if game.lastmouse1 !=[0,0] and game.main!=[-3,-3]:
        pygame.draw.line(screen, (255, 255, 255), [game.lastmouse1[0] - 3, game.lastmouse1[1] + 75],[game.lastmouse1[0] + 3, game.lastmouse1[1] + 75],width=2)
    # disallows vision of the pile list while you're not allowed to see it
    displaypile(screen,game)
    game=gameend(screen,game)
    if game.main==[-2,0]:
        #this feature is so you can see the computers hand after the game
        displayhand2(screen, game)
    loadmainbuttons(screen,game)
    pygame.display.update()
    return game

def gameend(screen,game):
    #checks to see if the game is over
    if game.backupmain==[0,0] and game.concede==True:
        game.player1.clear()

    if game.backupmain[0] == 1 and game.concede == True:
        game.player2.clear()

    if game.backupmain[0] == 2 and game.concede == True:
        game.player1.clear()

    if len(game.player1) == 26:
        game.player2.clear()
    if len(game.player2) == 26:
        game.player1.clear()

    if len(game.player1) == 0:
        game.main = [-2, 0]
        screen.fill(game.background_color)
        displayhand1(screen,game)
        displayhand2(screen,game)
        displayfplay(screen,game)
        displaypile(screen,game)
        a = pygame.image.load('ponewin.png')
        screen.blit(a, (380, 480))
        pygame.display.update()
        return game

    if len(game.player2) == 0:
        game.main = [-3, 0]
        screen.fill(game.background_color)
        displayhand1(screen,game)
        displayhand2(screen,game)
        displayfplay(screen,game)
        displaypile(screen,game)
        a = pygame.image.load('ptwowin.png')
        screen.blit(a, (380, 50))
        pygame.display.update()
        return game
    return game

def displayhand1(screen,game):
    y = 0 ###redo
    # placement on the screen, loads bottom hand
    while y < len(game.player1):
        card = game.player1[y]
        selectionadjustment = 0
        if game.altreveal == True and game.main[0] == 2:
            x = pygame.image.load('blueback.png')
        else: x = pygame.image.load(f'{card}.png')
        if y < 13:
            if card in game.play: selectionadjustment = 20
            screen.blit(x, (20 + y * 75, 450 - selectionadjustment))
        # second row
        else:
            if card in game.play: selectionadjustment = 20
            screen.blit(x, (20 + (y - 13) * 75, 603 - selectionadjustment))
        y += 1

def displayhand2(screen,game):
    y=0  ###redo
    # placement on the screen, loads top hand
    while y < len(game.player2):
        card=game.player2[y]
        selectionadjustment=0
        if game.altreveal==True and game.main[0] == 1 or game.AI==True and game.main!=[-2,0]:
            x = pygame.image.load('blueback.png')
        else:
            x=pygame.image.load(f'{card}.png')
        if y<13:
            if card in game.play2: selectionadjustment = 15
            screen.blit(x, (20+y*75,20-selectionadjustment))
        #second row
        else:
            if card in game.play2: selectionadjustment = 15
            screen.blit(x, (20 + (y-13) * 75, 133+selectionadjustment))
        y+=1


def displayfplay(screen,game):
    y = 0 ###redo
    #shows played cards
    while y < len(game.fplay):
        card = game.fplay[y]
        x = pygame.image.load(f'{card}.png')
        if y < 13:
            screen.blit(x, (230 + y * 75, 280))
        y += 1


def displaypile(screen,game):
    if game.main[0] <1:return
    x = 0;y = 0   ###redo
    #shows side drawable pile
    while y < len(game.pile):
        card = game.pile[y]
        x = pygame.image.load(f'{card}.png')
        if y < 6:
            screen.blit(x, (750 + y * 37, 270))
        else:
            screen.blit(x, (750 + (y-6) * 37, 297))
        y += 1
    #return pile,screen

def loadmainbuttons(screen,game):
    #loads button picutres according to thier legality governed by the variable (main)
    a = pygame.image.load('optionslong.png')
    screen.blit(a, (10, 323))

    if game.main[0]==1:
        a=pygame.image.load('arrowdown.png')
        screen.blit(a,(80,260))

    if game.main[0]==2:
        a=pygame.image.load('arrowup.png')
        screen.blit(a,(80,260))

    if game.main==[0,0]or game.main==[-1,0]:
        a=pygame.image.load('mulligan.png')
        screen.blit(a,(120,323))

    if game.main[1]==0 and game.main[0] !=0:
        a = pygame.image.load('play.png')
        screen.blit(a, (120, 323))

    if game.main[1]==1:
        a = pygame.image.load('play.png')
        screen.blit(a, (120, 323))
        a = pygame.image.load('passturn.png')
        screen.blit(a, (120, 280))

    if game.main[1]==2:
        a = pygame.image.load('play.png')
        screen.blit(a, (120, 323))
        a = pygame.image.load('draw.png')
        screen.blit(a, (640, 323))

    if game.main[1]==3:
        a = pygame.image.load('draw.png')
        screen.blit(a, (640, 323))
        a = pygame.image.load('ok.png')
        screen.blit(a, (120, 323))
        if game.p1redraw==True and game.main[0]==1:
            a = pygame.image.load('redraw.png')
            screen.blit(a, (640, 280))
        if game.p2redraw == True and game.main[0]==2:
            a = pygame.image.load('redraw.png')
            screen.blit(a, (640, 280))

    if game.main[1]==4:
        a = pygame.image.load('ok.png')
        screen.blit(a, (120, 323))
        if game.p1redraw==True and game.main[0]==1:
            a = pygame.image.load('redraw.png')
            screen.blit(a, (640, 280))
        if game.p2redraw == True and game.main[0]==2:
            a = pygame.image.load('redraw.png')
            screen.blit(a, (640, 280))

    if game.main[0]==2 and game.AI==True:
        a = pygame.image.load('compplay.png')
        screen.blit(a, (120, 323))



def optionwindow(screen,game):
    #pictures for the options menu buttons
    screen.fill(game.background_color)
    a=pygame.image.load('back.png')
    screen.blit(a, (10, 323))
    a=pygame.image.load('undo.png')
    screen.blit(a, (10, 262))


    if game.optionslist[0]==0:
        a=pygame.image.load('showthisoff.png')
        screen.blit(a, (10, 384))

    else:
        a=pygame.image.load('showthison.png')
        screen.blit(a, (10, 384))
        displayshowstuff(game.showthis,screen)

    if game.optionslist[1]==0:
        a=pygame.image.load('showlastoff.png')
        screen.blit(a, (10, 445))
    else:
        a=pygame.image.load('showlaston.png')
        screen.blit(a, (10, 445))
        displayshowstuff(game.showlast,screen)

    if game.altreveal==False:
        a = pygame.image.load('altrevealoff.png')
        screen.blit(a, (10, 506))
    else:
        a = pygame.image.load('altrevealon.png')
        screen.blit(a, (10, 506))
    a =pygame.image.load('rules.png')    ##is this correct?
    screen.blit(a, (10, 567))

    if game.optionslist[3]==1:
        a =pygame.image.load('ruleslist.png')
        screen.blit(a, (250, 200))
        a =pygame.image.load('banner.png')
        screen.blit(a, (380, 10))

    if game.optionslist[4]==0:
        a = pygame.image.load('concede.png')
        screen.blit(a, (10, 628))

    elif game.optionslist[4]==1:
        a = pygame.image.load('areyousure.png')
        screen.blit(a, (10, 628))

    if game.optionslist[2]==0:
        a = pygame.image.load('replaygame.png')
        screen.blit(a, (10, 201))

    elif game.optionslist[2]==1:
        a = pygame.image.load('areyousure.png')
        screen.blit(a, (10, 201))

    if not game.AI:
        a = pygame.image.load('compoff.png')
        screen.blit(a, (10, 140))

    else:
        a = pygame.image.load('compon.png')
        screen.blit(a, (10, 140))

    if not game.automull:
        a = pygame.image.load('automulloff.png')
        screen.blit(a, (10, 79))
    else:
        a = pygame.image.load('automullon.png')
        screen.blit(a, (10, 79))
    pygame.display.update()
    return game

def displayshowstuff(list,screen):
    y=0  ###redo
    #displays cards for showthishand option and show last hand option
    while y < len(list):
        card = list[y]
        x = pygame.image.load(f'{card}.png')
        if y < 11: screen.blit(x, (170 + y * 75, 20))
        if 11 <= y <= 23: screen.blit(x, (170 + (y - 13) * 75, 133))
        if 24 <= y <= 36: screen.blit(x, (170 + (y - 26) * 75, 246))
        y += 1