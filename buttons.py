import display as display;import basic as basic;import random;import checkplay as checkplay;import undo as undo;import mulligan as mulligan

def makehandbuttons(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain):
    # turn off button if we're in menu screen
    if main[0] == -3 and main[1] == -3:
        return player1, play
    if main[0]==2:
        return player1, play
    x=0
    #create boxes to click on for bottom hand
    while x < len(player1):
        selectionadjustment=0
        if len(play)>0:
            if player1[x] in play:selectionadjustment=20
        if x<13:
            if 20+x*72+(3 * x) <= mouse[0] <= 92+x*72+(3 * x) and 450 -selectionadjustment <= mouse[1] <= 560- selectionadjustment:
                if len(play) != 0:
                    if player1[x] in play:
                        play.remove(player1[x]);
                        player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
                play.append(player1[x])
                player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
            else:x+=1
        else:   #row 2
            if 20 + (x-13) * 72 + (3 * (x-13)) <= mouse[0] <= 92 + (x-13)* 72 + (3 * (x-13)) and 605 -selectionadjustment <= mouse[1] <= 715- selectionadjustment:
                if len(play) != 0:
                    if player1[x] in play:
                        play.remove(player1[x]);
                        player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
                play.append(player1[x])
                player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
            else: x+=1
    return player1, play

def makehand2buttons(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain):
    #turn off button if we're in menu screen
    if main[0] == -3 and main[1] == -3:
        return player2,play2
    if main[0]==1:
        return player2,play2
    x = 0
    # create boxes to click on for top hand
    while x < len(player2):
        selectionadjustment=0
        if len(play2)>0:
            if player2[x] in play2:selectionadjustment=15
        if x<13:
            if 20+x*72+(3 * x) <= mouse[0] <= 92+x*72+(3 * x) and 21 -selectionadjustment <= mouse[1] <= 133- selectionadjustment:
                if len(play2) != 0:
                    if player2[x] in play2: play2.remove(player2[x]);display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
                play2.append(player2[x]);display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
            else:x+=1
        else:   #row 2
            if 20 + (x-13) * 72 + (3 * (x-13)) <= mouse[0] <= 92 + (x -13)* 72 + (3 * (x-13)) and 134 +selectionadjustment <= mouse[1] <= 244 + selectionadjustment:
                if len(play2) != 0:
                    if player2[x] in play2:play2.remove(player2[x]);display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
                play2.append(player2[x]);display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain);break
            else: x+=1
    return player2,play2

def makepilebuttons(mouse,player1, player2,main, altreveal, screen, play,play2,background_color,lastmouse1,pile,AI,log,
                    p1redraw,p2redraw,concede,backupmain,gamemode,showthis,showlast,fplay):
    ## this does all drawing of the side pile
    # turn off button if we're in menu screen
    if main[0] == -3 and main[1] == -3:
        return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,gamemode
    #turns off button if AI exists
    if main[0]==2 and AI:
        return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,gamemode
    #can't click button if it's not the correct time to click it, will probably add a sound later
    if main[1] !=2:
        return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,gamemode
    x=0;y=[];z=0
    if len(pile)==0:
        return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log
    #only 6 cards across, the x,y is location on screen
    while x < 6:
        if 751 + x * 35 + (2 * x) <= mouse[0] <= 787 + x * 35 + (2 * x) and 271 <= mouse[1] <= 381:
             if len(pile)<x:break
             else:y.append(pile[x]);break
        if x == 5 or x+1== len(pile):
            if 751 + x * 35 + (2 * x) <= mouse[0] <= 787 + x * 35 + (2 * x)+37 and 271 <= mouse[1] <= 381:
                if len(pile) < x:break
                else:y.append(pile[x]);break
        x+=1
    if len(pile)>6:z=1
    while z==1 and x<12:
        if 751 + (x-6) * 35 + (2 * (x-6)) <= mouse[0] <= 787 + (x-6) * 35 + (2 * (x-6)) and 298 <= mouse[1] <= 408:
            if len(pile) < x:break
            else:y.append(pile[x]);break
        if x == 11 or x+1== len(pile):
            if 751 + (x-6) * 35 + (2 * (x-6)) <= mouse[0] <= 787 + (x-6) * 35 + (2 * (x-6))+37 and 298 <= mouse[1] <= 408:
                if len(pile) < x:break
                else:y.append(pile[x]);break
        x+=1
    if len(y)==2:
        y.pop(0)
    if len(y)==0:
        return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,gamemode
    else:
        if main[0]==1:
            log.append(y[0]);log.append(list(main));log.append([0,0,0]);log.append(5);pile.remove(y[0]);player1.append(y[0]),y.pop(0);fplay=[]
            #ok
            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main,
                altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,
                log,showthis,showlast,concede,backupmain)
        else:
            log.append(y[0]);log.append(list(main));log.append([0,0,0]);log.append(5);pile.remove(y[0]);player2.append(y[0]),y.pop(0);fplay=[]
            #ok

            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main,
                altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,
                showthis,showlast,concede,backupmain)
    return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,gamemode

def gameendfct(player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,showthis,used,log,concede,optionslist,AIinfo,play,play2,fplay,pile,mouse,replay,altreveal, screen,background_color,lastmouse1,AI,backupmain):
    #button to play again
    if 380 <= mouse[0] <= 380 + 251 and 480 <= mouse[1] <= 480 + 76 and main == [-2, 0]:
        replay=False
        #basic.startgame
        player1, player2, deck, backupdeck, main, gamemode, p1redraw, p2redraw, showlast, showthis, used, log, concede, \
        optionslist, AIinfo, play, play2, fplay, pile, altreveal, screen, background_color, \
        lastmouse1, AI, backupmain =basic.startgame(player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,
        showlast,showthis,used,log,concede,optionslist,AIinfo,play,play2,fplay,pile,altreveal, screen,background_color,
                                                    lastmouse1,AI,backupmain)
    if 380 <= mouse[0] <= 380 + 251 and 50 <= mouse[1] <= 50 + 76 and main == [-3, 0]:
        replay=False
        # basic.startgame
        player1, player2, deck, backupdeck, main, gamemode, p1redraw, p2redraw, showlast, showthis, used, log, concede, \
        optionslist, AIinfo, play, play2, fplay, pile, altreveal, screen, background_color, \
        lastmouse1, AI, backupmain =basic.startgame(player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,
        showlast,showthis,used,log,concede,optionslist,AIinfo,play,play2,fplay,pile,altreveal, screen,background_color,
                                                    lastmouse1,AI,backupmain)
    return player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,showthis,used,log,concede,optionslist,AIinfo,play,play2,fplay,pile,mouse,replay,altreveal,lastmouse1,AI,backupmain

def mullfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,
            p2redraw,AI,log,concede,backupmain,automull,gamemode,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,showthis,showlast):
    #starts the mulligan process, once 3 cards by each player are selected they get moved to the pile and the player who goes first is determined
    if main !=[0,0]:
        return player1, player2,main,pile,log,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,play2,showthis,showlast
    if 120 <= mouse[0] <= 200 and 323 <=mouse[1] <=383:
        if automull==True and len(player2)==16 or AI==True and len(player2)==16:
            #mulligan player2
            main,gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast=mulligan.mulligan(main,
                gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast)
        if len(play2) == 3:
            log.append(list(play2));log.append([0,0]);log.append([0,0,0]);log.append(-2);play2,pile=addpile(play2,pile);play2,player2=use(play2,player2)
            player2=basic.sort(player2);play2.clear()
            player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
        if automull==True and len(player1)==16 :
            p2copyjustforthis=list(player2);player2=list(player1)
            #mulligan player1
            main,gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast=mulligan.mulligan(main,
                gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast)
            play=list(play2);player2=list(p2copyjustforthis)
        if len(play) == 3:
            log.append(list(play));log.append([0,0]);log.append([0,0,0]);log.append(-1);play,pile=addpile(play,pile);play,player1=use(play,player1)
            player1=basic.sort(player1);
            player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
        if len(pile)==6:
            play=[];play2=[];main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
            player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return player1, player2,main,pile,log,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,play2,showthis,showlast

def drawfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,deck,used,showthis,showlast,log,gamemode,concede,backupmain):
    #draws a card and moves the main to it's proper status, also adds it to the log for the undo function, ok() is the step after the draws are locked in
    if main==[1,2] or main==[1,3]:
        if 640 <= mouse[0] <=720 and 323 <= mouse[1] <= 383:
            fplay=[];deck,showthis,used=decksize(deck,showthis,used);player1.append(deck[0]);log.append(deck[0]);log.append(list(main)); log.append(list(gamemode));log.append(2);deck.pop(0);main[1]=int(main[1]+1)
            if main[1]==4 and p1redraw == False:
                player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
            else:
                player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    if main==[2,2] or main==[2,3]:
        if AI:
            return player1, player2,main,gamemode,deck,log,fplay,lastmouse1,showthis,showlast
        if 640 <= mouse[0] <=720 and 323 <= mouse[1] <= 383:
            fplay=[];deck,showthis,used=decksize(deck,showthis,used);player2.append(deck[0]);log.append(deck[0]);log.append(list(main));log.append(list(gamemode)); log.append(2);deck.pop(0);main[1]=int(main[1]+1)
            if main[1]==4 and p2redraw==False:
                player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
            else:
                player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return player1, player2,main,gamemode,deck,log,fplay,lastmouse1,showthis,showlast

def redrawfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,deck,used,showthis,showlast,log,gamemode,concede,backupmain):
    tolog=[]
    #redraw is a free action each player gets once per game and they can redraw all cards they drew that turn and draw again, all the code is just removing/adding things to the lists where they belong
    if main==[1,3] and p1redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player1.remove(log[-4]);deck,showthis,used=decksize(deck,showthis,used);player1.append(deck[0]);tolog.append(deck[0]);deck.pop(0)   ###player[-1] to log[-4]
            p1redraw=False;log.append(tolog);log.append(list(main)); log.append(list(gamemode));log.append(3)
            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
    if main==[1,4]and p1redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player1.remove(log[-4]);tolog.append(log[-8]);pile.append(log[-8]);player1.remove(log[-8]);deck,showthis,used=decksize(deck,showthis,used)
            player1.append(deck[0]);tolog.append(deck[0]);deck.pop(0);deck,showthis,used=decksize(deck,showthis,used);player1.append(deck[0]);tolog.append(deck[0]);deck.pop(0);p1redraw=False
            log.append(tolog);log.append(list(main)); log.append(list(gamemode));log.append(3)
            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
    if main==[2,3]and p2redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player2.remove(log[-4]);deck,showthis,used=decksize(deck,showthis,used);player2.append(deck[0]);tolog.append(deck[0]);deck.pop(0)
            p2redraw=False;log.append(tolog);log.append(list(main)); log.append(list(gamemode));log.append(3)
            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
    if main==[2,4]and p2redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player2.remove(log[-4]);tolog.append(log[-8]);pile.append(log[-8]);player2.remove(log[-8]);deck,showthis,used=decksize(deck,showthis,used)
            player2.append(deck[0]);tolog.append(deck[0]);deck.pop(0);deck,showthis,used=decksize(deck,showthis,used);player2.append(deck[0]);tolog.append(deck[0]);deck.pop(0);p2redraw=False
            log.append(tolog);log.append(list(main));log.append(list(gamemode)); log.append(3)
            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
    return player1, player2,main,gamemode,deck,log,lastmouse1,showthis,showlast

def okfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain):
    if main[1]==3 or main[1]==4:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
    return player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast

def ok(player1,player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain):
    showlast = []; showlast = list(showthis) ; showthis= []
    fplay=[];log.append(0);log.append(list(main));log.append(list(gamemode));log.append(6);gamemode=[0,0,0];play.clear();play2.clear();lastmouse1=[0,0]
    #changes turn in game
    if main[0]==1:main=[2,1];player1=basic.sort(player1)
    else:main=[1,1];player2=basic.sort(player2)
    player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast

def passturn(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,log,gamemode,concede,backupmain):
    #turns off button if the AI exists
    if AI==True and main[0]==2:return main,log
    #passes the turn in game
    if main[1] != 1: return main,log
    if 120 <= mouse[0] <= 200 and 280 <= mouse[1] <= 310:
        if main[0] == 1:
            log.append(0);log.append(list(main));log.append(list(gamemode)); log.append(4);main = [2, 0]
            player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
        else:
            log.append(0);log.append(list(main));log.append(list(gamemode)); log.append(4);main = [1,0]
            player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return main,log

def use(play0,player0):
    #removes cards from the play list and player hand list, cards played will be inside both
    while len(play0) !=0:
        player0.remove(play0[0])
        play0.pop(0)
    return play0,player0

def addpile(play,pile):
    x = 0
    #adds cards from mulligan or redraw into the pile
    while x !=len(play):
        pile.append(str(play[x]))
        x+=1
    return play,pile

def decksize(deck,showthis,used):
    #if we run out of cards we need to reshuffle the used pile back in
    if len(deck) !=0: return deck,showthis,used
    if len(deck)==0:
        x=0
        while x<len(showthis):
            used.remove(showthis[x])
            x+=1
    deck=list(used)
    random.shuffle(deck)
    return deck,showthis,used

def testbutton(mouse,gamemode,main,log,pile):
    #used to test the contents of lists
    if 70 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
       print('gamemode =',gamemode);print('main is',main);print('log is',log)


def optionbuttons(mouse,main, backupmain, optionslist, showthis, showlast,concede, altreveal, replay, AI, automull,
                  screen,background_color,player1, player2, deck, backupdeck,gamemode, p1redraw,p2redraw, used, log,
                  AIinfo, play, play2, fplay, pile,lastmouse1):
    #options menu clickable buttons
    if main !=[-3,-3] and 10 <= mouse[0] <= 40 and 323 <= mouse[1] <= 383:
        backupmain=list(main);main=[-3,-3];concede,optionslist, altreveal,showthis,showlast,AI,automull=display.optionwindow(screen,background_color,concede,optionslist, altreveal,showthis,showlast,AI,automull)
        return main, backupmain, optionslist, showthis, showlast,concede, altreveal, replay, AI, automull,player1, \
               player2, deck, backupdeck,gamemode, p1redraw,p2redraw, used, log, AIinfo, play, play2, fplay, pile,lastmouse1
    if main==[-3,-3] and 10 <= mouse[0] <= 100 and 323 <= mouse[1] <= 383:
        main=list(backupmain)
        player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain)
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 384 <= mouse[1] <= 444:   #showthisoff
        if optionslist[0]==0: optionslist=[1,0,0,0,0,0];display.displayshowstuff(showthis,screen)
        else: optionslist[0]=0
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 445 <= mouse[1] <= 505:   #showlastoff
        if optionslist[1]==0: optionslist=[0,1,0,0,0,0];display.displayshowstuff(showlast,screen)
        else: optionslist[1]=0
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 506 <= mouse[1] <= 566:   #revealhandoff
        if altreveal==False: altreveal=True
        else: altreveal=False
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 567 <= mouse[1] <= 627:   #rules
        if optionslist[3]==0: optionslist=[0,0,0,1,0,0]
        else: optionslist[3]=0
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 628 <= mouse[1] <= 688:   #concede
        if optionslist[4]==0: optionslist=[0,0,0,0,1,0]
        elif optionslist[4]==1:
            concede=True;
            #gameend
            main, player1, player2=display.gameend(player1, player2,main, altreveal, screen, play,play2,fplay,
                                                           background_color,pile,concede,backupmain)
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 262 <= mouse[1] <= 322: #undo button
        main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2=undo.undo(log, main,
            pile, player1, player2, showthis, showlast, p1redraw, p2redraw, fplay, gamemode, backupmain,
             deck,play,play2,used,background_color,altreveal, screen,lastmouse1, AI, concede)
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 201 <= mouse[1] <= 261:
        if optionslist[2]==0:optionslist=[0,0,1,0,0,0]
        elif optionslist[2]==1:replay=True
        player1, player2, deck, backupdeck, main, gamemode, p1redraw, p2redraw, showlast, showthis, used, log, concede, \
        optionslist, AIinfo, play, play2, fplay, pile, altreveal, screen, background_color, \
        lastmouse1, AI, backupmain = basic.startgame(player1, player2, deck, backupdeck, main, gamemode, p1redraw,p2redraw, showlast, showthis, used, log, concede, optionslist, AIinfo, play, play2, fplay, pile, altreveal, screen,background_color, lastmouse1, AI, backupmain)
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 140 <= mouse[1] <= 200:
        if AI: AI=False
        else: AI=True
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 79 <= mouse[1] <= 139:
        if automull: automull=False
        else: automull=True
    if main==[-3,-3]:display.optionwindow(screen,background_color,concede,optionslist, altreveal,showthis,showlast,AI,automull)
    return main, backupmain, optionslist, showthis, showlast,concede, altreveal, replay, AI, automull,player1, player2, \
           deck, backupdeck,gamemode, p1redraw,p2redraw, used, log, AIinfo, play, play2, fplay, pile,lastmouse1

def buttons(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,
            p1redraw,p2redraw,deck,used,replay,backupdeck,concede,optionslist,AIinfo,gamemode,showthis,showlast,
            backupmain,automull,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,p2copy,segp2,copyseg,finalseg):
    #a list of clickable buttons in the game, have to put this in a different area in the code than everything else
    #makehandbuttons
    player1,play=makehandbuttons(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain)
    #makehand2buttons
    player2,play2=makehand2buttons(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,p1redraw,p2redraw,AI,concede,backupmain)
    #makepilebuttons
    player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,gamemode=makepilebuttons\
        (mouse,player1, player2,main, altreveal, screen, play,play2,background_color,lastmouse1,pile,AI,log,p1redraw,
         p2redraw,concede,backupmain,gamemode,showthis,showlast,fplay)
    testbutton(mouse,gamemode,main,log,pile)
    #passturn
    main,log=passturn(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,
                      p1redraw,p2redraw,AI,log,gamemode,concede,backupmain)
    #option buttons
    main, backupmain, optionslist, showthis, showlast,concede, altreveal, replay, AI, automull,player1, player2, deck,\
        backupdeck,gamemode, p1redraw,p2redraw, used, log, AIinfo, play, play2, fplay, pile,lastmouse1=optionbuttons\
        (mouse,main, backupmain, optionslist, showthis, showlast,concede, altreveal, replay, AI,
        automull,screen,background_color,player1, player2, deck, backupdeck,gamemode, p1redraw,p2redraw, used, log, AIinfo, play, play2, fplay, pile,lastmouse1)
    #playfct
    fplay,player1,player2,main,play,play2,gamemode,lastmouse1,finalseg,AIinfo,deck,p2redraw,log,pile=checkplay.playfct(
        mouse,player1, player2,main, altreveal,screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,
        p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode,p2copy,segp2,copyseg,finalseg,AIinfo,deck)
    #okfct
    player1, player2,main,gamemode,log,play,play2,fplay,lastmouse1,showthis,showlast=\
        okfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,
        p1redraw,p2redraw,AI,gamemode,log,showthis,showlast,concede,backupmain)
    #mullfct
    player1, player2,main,pile,log,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,play2,showthis,showlast=\
        mullfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,
        p1redraw,p2redraw,AI,log,concede,backupmain,automull,gamemode,outliers,n2akout,quads,hardmull,mullnotes,mull,
        hand,showthis,showlast)
    #drawfct
    player1, player2,main,gamemode,deck,log,fplay,lastmouse1,showthis,showlast=drawfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,
        background_color,lastmouse1,pile, p1redraw,p2redraw,AI,deck,used,showthis,showlast,log,gamemode,concede,backupmain)

    #redrawfct
    player1, player2,main,gamemode,deck,log,lastmouse1,showthis,showlast=\
        redrawfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,
        background_color,lastmouse1,pile, p1redraw,p2redraw,AI,deck,used,
        showthis,showlast,log,gamemode,concede,backupmain)

    #gameendfct
    player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,showthis,used,log,concede,optionslist,AIinfo,\
        play,play2,fplay,pile,mouse,replay,altreveal,lastmouse1,AI,backupmain=\
        gameendfct(player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,showthis,used,log,concede,
        optionslist,AIinfo,play,play2,fplay,pile,mouse,replay,altreveal, screen,background_color,lastmouse1,AI,backupmain)

    return player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,AI,log,p1redraw,\
           p2redraw,deck,used,replay,backupdeck,concede,optionslist,AIinfo,gamemode,showthis,showlast,backupmain,\
           automull,outliers,n2akout,quads,hardmull,mullnotes,mull,hand,finalseg