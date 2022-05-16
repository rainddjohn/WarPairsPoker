import display as display
import basic as basic
import random
import checkplay as checkplay
import undo as undo
import mulligan as mulligan

def makehandbuttons(mouse,screen,game):
    # turn off button if we're in menu screen
    if game.main[0] == -3 and game.main[1] == -3:
        return game
    if game.main[0]==2:
        return game
    x=0
    #create boxes to click on for bottom hand
    while x < len(game.player1): ###redo
        selectionadjustment=0
        if len(game.play)>0:
            if game.player1[x] in game.play:
                selectionadjustment=20
        if x<13:
            if 20+x*72+(3 * x) <= mouse[0] <= 92+x*72+(3 * x) and 450 -selectionadjustment <= mouse[1] <= 560- selectionadjustment:
                if len(game.play) != 0:
                    if game.player1[x] in game.play:
                        game.play.remove(game.player1[x]);
                        game=display.redrawgamewindow(screen,game)
                        break
                game.play.append(game.player1[x])
                game=display.redrawgamewindow(screen,game)
                break
            else:x+=1
        else:   #row 2
            if 20 + (x-13) * 72 + (3 * (x-13)) <= mouse[0] <= 92 + (x-13)* 72 + (3 * (x-13)) and 605 -selectionadjustment <= mouse[1] <= 715- selectionadjustment:
                if len(game.play) != 0:
                    if game.player1[x] in game.play:
                        game.play.remove(game.player1[x]);
                        game=display.redrawgamewindow(screen,game)
                        break
                game.play.append(game.player1[x])
                game=display.redrawgamewindow(screen,game)
                break
            else: x+=1
    return game

def makehand2buttons(mouse, screen, game):
    #turn off button if we're in menu screen
    if game.main[0] == -3 and game.main[1] == -3:
        return game
    if game.main[0]==1:
        return game
    x = 0
    # create boxes to click on for top hand
    while x < len(game.player2): ###redo
        selectionadjustment=0
        if len(game.play2)>0:
            if game.player2[x] in game.play2:
                selectionadjustment=15
        if x<13:
            if 20+x*72+(3 * x) <= mouse[0] <= 92+x*72+(3 * x) and 21 -selectionadjustment <= mouse[1] <= 133- selectionadjustment:
                if len(game.play2) != 0:
                    if game.player2[x] in game.play2:
                        game.play2.remove(game.player2[x])
                        game=display.redrawgamewindow(screen,game)
                        break
                game.play2.append(game.player2[x])
                game=display.redrawgamewindow(screen,game)
                break
            else:x+=1
        else:   #row 2
            if 20 + (x-13) * 72 + (3 * (x-13)) <= mouse[0] <= 92 + (x -13)* 72 + (3 * (x-13)) and 134 +selectionadjustment <= mouse[1] <= 244 + selectionadjustment:
                if len(game.play2) != 0:
                    if game.player2[x] in game.play2:
                        game.play2.remove(game.player2[x])
                        game=display.redrawgamewindow(screen,game)
                        break
                game.play2.append(game.player2[x])
                game=display.redrawgamewindow(screen,game)
                break
            else: x+=1
    return game

def makepilebuttons(mouse,screen,game):
    ## this does all drawing of the side pile

    # turn off button if we're in menu screen
    if game.main[0] == -3 and game.main[1] == -3:
        return game

    #turns off button if AI exists
    if game.main[0]==2 and game.AI:
        return game

    #can't click button if it's not the correct time to click it, will probably add a sound later
    if game.main[1] !=2:
        return game
    x=0
    y=[]
    z=0
    if len(game.pile)==0:
        return game

    #only 6 cards across, the x,y is location on screen
    while x < 6:
        if 751 + x * 35 + (2 * x) <= mouse[0] <= 787 + x * 35 + (2 * x) and 271 <= mouse[1] <= 381:
             if len(game.pile)<x:
                 break
             else:
                 y.append(game.pile[x])
                 break
        if x == 5 or x+1== len(game.pile):
            if 751 + x * 35 + (2 * x) <= mouse[0] <= 787 + x * 35 + (2 * x)+37 and 271 <= mouse[1] <= 381:
                if len(game.pile) < x:
                    break
                else:
                    y.append(game.pile[x])
                    break
        x+=1
    if len(game.pile)>6:
        z=1
    while z==1 and x<12:
        if 751 + (x-6) * 35 + (2 * (x-6)) <= mouse[0] <= 787 + (x-6) * 35 + (2 * (x-6)) and 298 <= mouse[1] <= 408:
            if len(game.pile) < x:
                break
            else:
                y.append(game.pile[x])
                break
        if x == 11 or x+1== len(game.pile):
            if 751 + (x-6) * 35 + (2 * (x-6)) <= mouse[0] <= 787 + (x-6) * 35 + (2 * (x-6))+37 and 298 <= mouse[1] <= 408:
                if len(game.pile) < x:
                    break
                else:
                    y.append(game.pile[x])
                    break
        x+=1
    if len(y)==2:
        y.pop(0)
    if len(y)==0:
        return game
    else:
        if game.main[0]==1:
            game.log.append(y[0])
            game.log.append(list(game.main))
            game.log.append([0,0,0])
            game.log.append(5)
            game.pile.remove(y[0])
            game.player1.append(y[0])
            y.pop(0)   ##there was a comma here wtf?
            game.fplay=[]
            game=ok(screen,game)
        else:
            game.log.append(y[0])
            game.log.append(list(game.main))
            game.log.append([0,0,0])
            game.log.append(5)
            game.pile.remove(y[0])
            game.player2.append(y[0])
            y.pop(0)
            game.fplay=[]
            game=ok(screen,game)
    return game

def gameendfct(mouse,screen,game):
    #button to play again
    if 380 <= mouse[0] <= 380 + 251 and 480 <= mouse[1] <= 480 + 76 and game.main == [-2, 0]:
        game.replay=False
        #basic.startgame
        game=basic.startgame(screen,game)

    if 380 <= mouse[0] <= 380 + 251 and 50 <= mouse[1] <= 50 + 76 and game.main == [-3, 0]:
        game.replay=False
        # basic.startgame
        game=basic.startgame(screen,game)
    return game

def mullfct(mouse,screen,game):
    #starts the mulligan process, once 3 cards by each player are selected they get moved to the pile and the player who goes first is determined
    if game.main !=[0,0]:
        return game
    if 120 <= mouse[0] <= 200 and 323 <=mouse[1] <=383:
        if game.automull==True and len(game.player2)==16 or game.AI==True and len(game.player2)==16:
            #mulligan player2
            game=mulligan.mulligan(game)

        if len(game.play2) == 3:
            game.log.append(list(game.play2))
            game.log.append([0,0])
            game.log.append([0,0,0])
            game.log.append(-2)
            game=addpile(game.play2,game)
            game.play2,game.player2=use(game.play2,game.player2)
            game.player2=basic.sort(game.player2)
            game.play2.clear()
            game=display.redrawgamewindow(screen,game)

        if game.automull==True and len(game.player1)==16 :
            p2copyjustforthis=list(game.player2);game.player2=list(game.player1)
            #mulligan player1
            game=mulligan.mulligan(game)
            game.play=list(game.play2)
            game.player2=list(p2copyjustforthis)

        if len(game.play) == 3:
            game.log.append(list(game.play))
            game.log.append([0,0])
            game.log.append([0,0,0])
            game.log.append(-1)
            game=addpile(game.play,game)
            game.play,game.player1=use(game.play,game.player1)
            game.player1=basic.sort(game.player1);
            game=display.redrawgamewindow(screen,game)
        if len(game.pile)==6:
            game.play=[]
            game.play2=[]
            game=basic.seewhogoesfirst(game)
            game=display.redrawgamewindow(screen,game)
    return game

def drawfct(mouse,screen,game):
    #draws a card and moves the main to it's proper status, also adds it to the log for the undo function, ok() is the step after the draws are locked in
    if game.main==[1,2] or game.main==[1,3]:
        if 640 <= mouse[0] <=720 and 323 <= mouse[1] <= 383:
            game.fplay=[]
            game=decksize(game)
            game.player1.append(game.deck[0])
            game.log.append(game.deck[0])
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(2)
            game.deck.pop(0)
            game.main[1]=int(game.main[1]+1)

            if game.main[1]==4 and game.p1redraw == False:
                game=ok(screen,game)
            else:
                game=display.redrawgamewindow(screen,game)
    if game.main==[2,2] or game.main==[2,3]:
        if game.AI:
            return game
        if 640 <= mouse[0] <=720 and 323 <= mouse[1] <= 383:
            game.fplay=[]
            game=decksize(game)
            game.player2.append(game.deck[0])
            game.log.append(game.deck[0])
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(2)
            game.deck.pop(0)
            game.main[1]=int(game.main[1]+1)
            if game.main[1]==4 and game.p2redraw==False:
                game=ok(screen,game)
            else:
                game=display.redrawgamewindow(screen,game)
    return game

def redrawfct(mouse,screen,game):
    tolog=[]
    #redraw is a free action each player gets once per game and they can redraw all cards they drew that turn and draw again, all the code is just removing/adding things to the lists where they belong
    if game.main==[1,3] and game.p1redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(game.log[-4])
            game.pile.append(game.log[-4])
            game.player1.remove(game.log[-4])
            game=decksize(game)
            game.player1.append(game.deck[0])
            tolog.append(game.deck[0])
            game.deck.pop(0)
            game.p1redraw=False;
            game.log.append(tolog)
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(3)
            game=ok(screen,game)

    if game.main==[1,4]and game.p1redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(game.log[-4])
            game.pile.append(game.log[-4])
            game.player1.remove(game.log[-4])
            tolog.append(game.log[-8])
            game.pile.append(game.log[-8])
            game.player1.remove(game.log[-8])
            game=decksize(game)
            game.player1.append(game.deck[0])
            tolog.append(game.deck[0])
            game.deck.pop(0)
            game=decksize(game)
            game.player1.append(game.deck[0])
            tolog.append(game.deck[0])
            game.deck.pop(0)
            game.p1redraw=False
            game.log.append(tolog)
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(3)
            game=ok(screen,game)

    if game.main==[2,3]and game.p2redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(game.log[-4])
            game.pile.append(game.log[-4])
            game.player2.remove(game.log[-4])
            game=decksize(game)
            game.player2.append(game.deck[0])
            tolog.append(game.deck[0])
            game.deck.pop(0)
            game.p2redraw=False
            game.log.append(tolog)
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(3)
            game=ok(game)

    if game.main==[2,4]and game.p2redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(game.log[-4])
            game.pile.append(game.log[-4])
            game.player2.remove(game.log[-4])
            tolog.append(game.log[-8])
            game.pile.append(game.log[-8])
            game.player2.remove(game.log[-8])
            game=decksize(game)
            game.player2.append(game.deck[0])
            tolog.append(game.deck[0])
            game.deck.pop(0)
            game=decksize(game)
            game.player2.append(game.deck[0])
            tolog.append(game.deck[0])
            game.deck.pop(0)
            game.p2redraw=False
            game.log.append(tolog)
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(3)
            game=ok(screen,game)
    return game

def okfct(mouse,screen,game):
    if game.main[1]==3 or game.main[1]==4:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            game=ok(screen,game)
    return game

def ok(screen,game):
    ## cleans up odds and ends before moving on to the next action in the game
    game.showlast = []
    game.showlast = list(game.showthis)
    game.showthis= []
    game.fplay=[]
    game.log.append(0)
    game.log.append(list(game.main))
    game.log.append(list(game.gamemode))
    game.log.append(6)
    game.gamemode=[0,0,0]
    game.play.clear()
    game.play2.clear()
    game.lastmouse1=[0,0]
    #changes turn in game
    if game.main[0]==1:
        game.main=[2,1]
        game.player1=basic.sort(game.player1)
    else:
        game.main=[1,1];
        game.player2=basic.sort(game.player2)
    game=display.redrawgamewindow(screen,game)
    return game

def passturn(mouse,screen,game):
    #turns off button if the AI exists
    if game.AI==True and game.main[0]==2:
        return game
    #passes the turn in game
    if game.main[1] != 1: return game
    if 120 <= mouse[0] <= 200 and 280 <= mouse[1] <= 310:
        if game.main[0] == 1:
            game.log.append(0)
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(4)
            game.main = [2, 0]
            game=display.redrawgamewindow(screen,game)
        else:
            game.log.append(0)
            game.log.append(list(game.main))
            game.log.append(list(game.gamemode))
            game.log.append(4)
            game.main = [1,0]
            game=display.redrawgamewindow(screen,game)
    return game

def use(play0,player0):   ###find where this is used
    #removes cards from the play list and player hand list, cards played will be inside both
    while len(play0) !=0:
        player0.remove(play0[0])
        play0.pop(0)
    return play0,player0

def addpile(play,game):
    x = 0  ###redo
    #adds cards from mulligan or redraw into the pile
    while x !=len(play):
        game.pile.append(str(play[x]))
        x+=1
    return game

def decksize(game):
    #if we run out of cards we need to reshuffle the used pile back in
    if len(game.deck) !=0:
        return game
    if len(deck)==0:  ###redo
        x=0
        while x<len(game.showthis):
            game.used.remove(game.showthis[x])
            x+=1
    game.deck=list(game.used)
    random.shuffle(game.deck)
    return game

def testbutton(mouse,game):
    #used to test the contents of lists
    if 70 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
        print('main/gamemode =',game.main,game.gamemode)
        #print('log is',game.log)
        print('used is',game.used)



def optionbuttons(mouse,screen,game):
    #options menu clickable buttons
    if game.main !=[-3,-3] and 10 <= mouse[0] <= 40 and 323 <= mouse[1] <= 383:
        game.backupmain=list(game.main)
        game.main=[-3,-3]
        game=display.optionwindow(screen,game)
        return game

    if game.main==[-3,-3] and 10 <= mouse[0] <= 100 and 323 <= mouse[1] <= 383:
        game.main=list(game.backupmain)
        game=display.redrawgamewindow(screen,game)

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 18 <= mouse[1] <= 78:   #showtop
        print('showtop=',game.showtop)
        if game.showtop==True:
            game.showtop=False

        else:
            game.showtop=True

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 384 <= mouse[1] <= 444:   #showthisoff
        if game.optionslist[0]==0:
            game.optionslist=[1,0,0,0,0,0]
            display.displayshowstuff(game.showthis,screen)
        else:
            game.optionslist[0]=0

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 445 <= mouse[1] <= 505:   #showlastoff
        if game.optionslist[1]==0:
            game.optionslist=[0,1,0,0,0,0]
            display.displayshowstuff(game.showlast,screen)
        else:
            game.optionslist[1]=0

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 506 <= mouse[1] <= 566:   #revealhandoff
        if game.altreveal==False:
            game.altreveal=True
        else:
            game.altreveal=False

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 567 <= mouse[1] <= 627:   #rules
        if game.optionslist[3]==0:
            game.optionslist=[0,0,0,1,0,0]
        else:
            game.optionslist[3]=0

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 628 <= mouse[1] <= 688:   #concede
        if game.optionslist[4]==0:
            game.optionslist=[0,0,0,0,1,0]
        elif game.optionslist[4]==1:
            game.concede=True
            game=display.gameend(screen,game)

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 262 <= mouse[1] <= 322: #undo button
        game=undo.undo(screen,game)

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 201 <= mouse[1] <= 261: #replay game
        if game.optionslist[2]==0:
            game.optionslist=[0,0,1,0,0,0]
        elif game.optionslist[2]==1:
            game.replay=True
            game = basic.startgame(screen,game)

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 140 <= mouse[1] <= 200: #AI
        if game.AI:
            game.AI=False
        else:
            game.AI=True

    if game.main == [-3, -3] and 10 <= mouse[0] <= 90 and 79 <= mouse[1] <= 139: #automull
        if game.automull:
            game.automull=False
        else:
            game.automull=True

    if game.main==[-3,-3]:
        display.optionwindow(screen,game)
    return game

def buttons(mouse,screen,game):
    #a list of clickable buttons in the game, have to put this in a different area in the code than everything else
    game=makehandbuttons(mouse,screen,game)
    game=makehand2buttons(mouse,screen,game)
    game=makepilebuttons(mouse,screen,game)
    testbutton(mouse,game)
    game=passturn(mouse,screen,game)
    game=optionbuttons(mouse,screen,game)
    game=checkplay.playfct(mouse,screen,game)
    game=okfct(mouse,screen,game)
    game=mullfct(mouse,screen,game)
    game=drawfct(mouse,screen,game)
    game=redrawfct(mouse,screen,game)
    game=gameendfct(mouse,screen,game)
    return game