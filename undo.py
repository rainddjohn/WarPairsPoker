import basic as basic;import display as display

def undo(screen,game):
    x=0
    #every event is added here as [cards used,main,gamemode,type of action]; types of action: -1,-2 mulligans, 1 play, 2 draw, 3 redraw, 4 is pass turn, 5 is pile, 6 is change of turn
    #AI 7 play 8 AI draw 9 AI pile (currently the AI does not draw from the pile)
    if len(game.log)==0:
        game.main=list(game.backupmain)
        game=display.redrawgamewindow(screen,game)
        return game
    game.play.clear()
    game.play2.clear()

    #handles player1 mulligan
    if game.log[-1]==-1:
        game.main=game.log[-3]
        while x < len(game.log[-4]):
            game.player1.append(game.log[-4][x])
            game.pile.remove(game.log[-4][x])
            x += 1
        game.main=list(game.log[-3])
        game=updatefplay(game)
        game.player1=basic.sort(game.player1)
        game.log=game.log[:-4]
        game.gamemode=[0,0,0]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)
        return game

    # handles player2 mulligan
    if game.log[-1]==-2:
        game.main=game.log[-3]
        while x < len(game.log[-4]):
            game.player2.append(game.log[-4][x])
            game.pile.remove(game.log[-4][x])
            x += 1
        game.main=list(game.log[-3])
        game=updatefplay(game)
        game.player2=basic.sort(game.player2)
        game.log = game.log[:-4]
        game.gamemode=[0,0,0]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)
        return game

    # handles play action
    if game.log[-1]==1:
        while x < len(game.log[-4]):
            game.log[-4][x] = str(game.log[-4][x])
            x += 1
        game.log[-4] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in game.log[-4]]

        #player1
        if game.log[-3][0]==1:
            x=0
            while x<len(game.log[-4]):
                game.player1.append(game.log[-4][x])
                game.used.remove(game.log[-4][x])
                if game.log[-4][x] in game.showthis:
                    game.showthis.remove(game.log[-4][x])
                x+=1
            game.main=game.log[-3]
            game=updatefplay(game)
            game.player1 = basic.sort(game.player1)
            game.log = game.log[:-4]
            if game.main[1]==1:
                game.gamemode=list([0,0,0])
            else:
                game.gamemode=list(game.log[-2])
            game=basic.seewhogoesfirst(game)
            game=display.redrawgamewindow(screen,game)
            return game

        #player2
        if game.log[-3][0]==2:
            x=0
            while x < len(game.log[-4]):
                game.player2.append(game.log[-4][x])
                game.used.remove(game.log[-4][x])
                if game.log[-4][x] in game.showthis:
                    game.showthis.remove(game.log[-4][x])
                x+=1
            game.main=game.log[-3]
            game=updatefplay(game)
            game.player2 = basic.sort(game.player2)
            game.log = game.log[:-4]
            if game.main[1]==1:
                game.gamemode=list([0,0,0])
            else:
                game.gamemode=list(game.log[-2])
            game=basic.seewhogoesfirst(game)
            game=display.redrawgamewindow(screen,game)
            return game

    #handles draw action
    if game.log[-1]==2:
        #player1
        if game.log[-3][0] == 1:
            game.main=game.log[-3]
            game=updatefplay(game)
            game.player1.remove(game.log[-4])
            game.deck.insert(0,game.log[-4])
            game.player1 = basic.sort(game.player1)
            game.gamemode = list(game.log[-2])
            game.log = game.log[:-4] #gamemode was after this

            game=basic.seewhogoesfirst(game)
            game=display.redrawgamewindow(screen,game)
            return game

        #player2
        if game.log[-3][0] == 2:
            game.main=game.log[-3]
            game=updatefplay(game)
            game.player2.remove(game.log[-4])
            game.deck.insert(0,game.log[-4])
            game.player2 = basic.sort(game.player2)
            game.gamemode = list(game.log[-2])
            game.log = game.log[:-4]

            game=basic.seewhogoesfirst(game)
            game=display.redrawgamewindow(screen,game)
            return game

    #handles redraw action
    if game.log[-1]==3:
        #player1 redrawing 1 card
        if game.log[-3][0] == 1:
            if game.log[-3][1] == 3:
                game.p1redraw = True
                game.player1.remove(game.log[-4][1])
                game.player1.append(game.log[-4][0])
                game.pile.remove(game.log[-4][0])
                game.main = game.log[-3]
                game=updatefplay(game)
                game.player1 = basic.sort(game.player1)
                game.log = game.log[:-4]
                game=basic.seewhogoesfirst(game)
                game=display.redrawgamewindow(screen,game)
                return game

            #player1 redrawing 2 cards
            if game.log[-3][1]==4:
                game.p1redraw=True
                game.player1.remove(game.log[-4][2])
                game.player1.remove(game.log[-4][3])
                game.player1.append(game.log[-4][0])
                game.player1.append(game.log[-4][1])
                game.pile.remove(game.log[-4][0])
                game.pile.remove(game.log[-4][1])
                game.main=game.log[-3]
                game=updatefplay(game)
                game.player1 = basic.sort(game.player1)
                game.log = game.log[:-4]
                game=basic.seewhogoesfirst(game)
                game=display.redrawgamewindow(screen,game)
                return game

        #player2 redrawing 1 card
        if game.log[-3][0] == 2:
            if game.log[-3][1] == 3:
                game.p2redraw = True
                game.player2.remove(game.log[-4][1])
                game.player2.append(game.log[-4][0])
                game.pile.remove(game.log[-4][0])
                game.main = game.log[-3]
                game=updatefplay(game)
                game.player2 = basic.sort(game.player2)
                game.log = game.log[:-4]
                game=basic.seewhogoesfirst(game)
                game=display.redrawgamewindow(screen,game)
                return game

            #player2 redrawing 2 cards
            if game.log[-3][1] == 4:
                game.p2redraw = True
                game.player2.remove(game.log[-4][2])
                game.player2.remove(game.log[-4][3])
                game.player2.append(game.log[-4][0])
                game.player2.append(game.log[-4][1])
                game.pile.remove(game.log[-4][0])
                game.pile.remove(game.log[-4][1])
                game.main=game.log[-3]
                game=updatefplay(game)
                game.player2 = basic.sort(game)
                game.log = game.log[:-4]
                game=basic.seewhogoesfirst(game)
                game=display.redrawgamewindow(screen,game)
                return game

    #pass the turn action
    if game.log[-1]==4:
        game.main=game.log[-3]
        game=updatefplay(game)
        game.log = game.log[:-4]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)
        return game

    #draw from the pile action
    if game.log[-1]==5:
        if game.log[-3][0]==1:
            game.player1.remove(game.log[-4])
            game.pile.append(game.log[-4])
        if game.log[-3][0]==2:
            game.player2.remove(game.log[-4])
            game.pile.append(game.log[-4])
        game.main = game.log[-3]
        game=updatefplay(game)
        game.log = game.log[:-4]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)
        return game

    #change of turn placeholder
    if game.log[-1]==6:
        game.gamemode=list(game.log[-2])
        game.main=game.log[-3]
        game=updatefplay(game)
        game.log = game.log[:-4]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)

        if game.log[-1]==5:
            game= undo(screen,game)
        return game

    #AI play action
    if game.log[-1]==7:
        if type(game.log[-4])==str:
            game.player2.append(game.log[-4])
        else:
            for i in game.log[-4]:
                game.player2.append(i)
                if i in game.used:
                    game.used.remove(i)
                if i in game.showthis:
                    game.showthis.remove(i) ##show this/used remove(i)

        game.fplay=list(game.log[-4])
        game.player2=basic.sort(game.player2)
        game.gamemode=list(game.log[-2])
        game.main=game.log[-3]
        game=updatefplay(game)
        game.log = game.log[:-4]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)

    #AI draw action
    if game.log[-1]==8:
        if len(game.log[-4])<3:
            for i in reversed(game.log[-4]):
                game.deck.insert(0,i)
                game.player2.remove(i)

        if len(game.log[-4])==4:
            counter=0
            for i in reversed(game.log[-4]):
                game.deck.insert(0,i)
                if counter<=1:
                    game.player2.remove(i)
                if counter>=2:
                    game.pile.remove(i)
                counter+=1
        game.p2redraw=True
        game.player2 = basic.sort(game.player2)
        game.gamemode = list(game.log[-2])
        game.main=game.log[-3]
        game=updatefplay(game)
        game.log = game.log[:-4]
        game=basic.seewhogoesfirst(game)
        game=display.redrawgamewindow(screen,game)
    return game
        
def updatefplay(game):
    x = 1
    #updates fplay when the undo button is used
    if game.main[1]==1:
        game.fplay=[]
        return game
    while len(game.log)>1+(x*4):   ### not sure about this one
        if game.log[-1+(x*-4)]==1:
            if game.log[-3][1]==2:
                game.fplay=list(game.log[-4+(x*-4)])
                return game
            else:
                return game
        else:
            x += 1
    game.fplay=[]
    return game
