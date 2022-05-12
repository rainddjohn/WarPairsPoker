import pygame;deck=[];import random; player1=[]; player2=[];play=[];play2=[];fplay=[];pile=[];main=[0,0];gamemode=[0,0,0];deck=[];pygame.init();p1redraw=True;p2redraw=True
showthis=[];showlast=[];backupmain=[0];optionslist=[0,0,0,0,0,0];used=[];log=[];concede=False;backupdeck=[];altreveal=False;replay=False; AI=True



(width,height)=(1033,750);background_color= (84,119,44);screen=pygame.display.set_mode((width,height));screen.fill(background_color);pygame.display.set_caption('WarPairsPoker')
###mulligan and segment AI variables
import copy;n2akout=[];hardmull=[];mullnotes=[];outliers=[];quads=[];mull=[];segp2=[[],[],[],[],[],[],[],[],[]];copyseg=[];finalseg=[];p2copy=[]
automull=True;lastmouse1=[0,0];AIinfo=[False,False,False,False,False,0,[],False]

def getdeck():
    global deck;global backupdeck
    suit=['s','h','c','d'];ranks=['2','3','4','5','6','7','8','9','10','11','12','13','14']    ##for spades cut 13 from this and add 14-16 to spades after
    #create our deck
    for r in ranks:
        for s in suit:
            deck.append(r+s)
    random.shuffle(deck) ##this shuffles
    #this is for the replay game function
    backupdeck=list(deck)
def deal():
    #deal hands
    while len(player1)<=15:
        player1.append(deck[0]); deck.pop(0)
    while len(player2)<=15:
        player2.append(deck[0]); deck.pop(0)
def sort(hand):
    nhand = [];i = 0; hand = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in hand]
    #because we have varchar we convert cards to numbers and sort it that way
    while i < len(hand):
        #we seperate the length 3 (9.3), and length 4 (10.3) sort them individually and join them again after
        if len(hand[i]) == 4:
            nhand.append(hand[i]);hand.remove(hand[i])
        else:
            i += 1
    #convert numbers back to card form
    hand.sort();nhand.sort();hand = hand + nhand;hand = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in hand]
    return hand
def displayhand1():
    y=0
    #placement on the screen, loads bottom hand
    while y < len(player1):
        card=player1[y];selectionadjustment=0
        if altreveal==True and main[0]==2: x=pygame.image.load('blueback.png')
        else:x=pygame.image.load(f'{card}.png')          ####loads images
        if y<13:
            if card in play:selectionadjustment=20
            screen.blit(x, (20+y*75,450-selectionadjustment))
        #second row
        else:
            if card in play: selectionadjustment = 20
            screen.blit(x, (20 + (y-13) * 75, 603-selectionadjustment))
        y+=1
def displayhand2():
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
def displayfplay():
    y = 0
    #shows played cards
    while y < len(fplay):
        card = fplay[y]
        x = pygame.image.load(f'{card}.png')  ####loads images
        if y < 13:
            screen.blit(x, (230 + y * 75, 280))
        y += 1
def displaypile():
    #if main != [0, 0]: return  TURN ON after test
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
def makehandbuttons(mouse,player1):
    # turn off button if we're in menu screen
    if main[0] == -3 and main[1] == -3:return
    if main[0]==2: return
    x=0
    #create boxes to click on for bottom hand
    while x < len(player1):
        selectionadjustment=0
        if len(play)>0:
            if player1[x] in play:selectionadjustment=20
        if x<13:
            if 20+x*72+(3 * x) <= mouse[0] <= 92+x*72+(3 * x) and 450 -selectionadjustment <= mouse[1] <= 560- selectionadjustment:
                if len(play) != 0:
                    if player1[x] in play: play.remove(player1[x]);redrawgamewindow();break
                play.append(player1[x]);redrawgamewindow();break
            else:x+=1
        else:   #row 2
            if 20 + (x-13) * 72 + (3 * (x-13)) <= mouse[0] <= 92 + (x-13)* 72 + (3 * (x-13)) and 605 -selectionadjustment <= mouse[1] <= 715- selectionadjustment:
                if len(play) != 0:
                    if player1[x] in play:play.remove(player1[x]);redrawgamewindow();break
                play.append(player1[x]);redrawgamewindow();break
            else: x+=1
def makehand2buttons(mouse,player2):
    #turn off button if we're in menu screen
    if main[0] == -3 and main[1] == -3: return
    if main[0]==1:return
    x = 0
    # create boxes to click on for top hand
    while x < len(player2):
        selectionadjustment=0
        if len(play2)>0:
            if player2[x] in play2:selectionadjustment=15
        if x<13:
            if 20+x*72+(3 * x) <= mouse[0] <= 92+x*72+(3 * x) and 21 -selectionadjustment <= mouse[1] <= 133- selectionadjustment:
                if len(play2) != 0:
                    if player2[x] in play2: play2.remove(player2[x]);redrawgamewindow();break
                play2.append(player2[x]);redrawgamewindow();break
            else:x+=1
        else:   #row 2
            if 20 + (x-13) * 72 + (3 * (x-13)) <= mouse[0] <= 92 + (x -13)* 72 + (3 * (x-13)) and 134 +selectionadjustment <= mouse[1] <= 244 + selectionadjustment:
                if len(play2) != 0:
                    if player2[x] in play2:play2.remove(player2[x]);redrawgamewindow();break
                play2.append(player2[x]);redrawgamewindow();break
            else: x+=1
def makepilebuttons(mouse,pile):
    global main;global fplay
    ## this does all drawing of the side pile
    # turn off button if we're in menu screen
    if main[0] == -3 and main[1] == -3: return
    #turns off button if AI exists
    if main[0]==2 and AI: return
    #can't click button if it's not the correct time to click it, will probably add a sound later
    if main[1] !=2:return
    x=0;y=[];z=0
    if len(pile)==0: return
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
    if len(y)==0:return
    else:
        if main[0]==1:
            log.append(y[0]);log.append(list(main));log.append([0,0,0]);log.append(5);pile.remove(y[0]);player1.append(y[0]),y.pop(0);fplay=[];ok();redrawgamewindow()
        else:log.append(y[0]);log.append(list(main));log.append([0,0,0]);log.append(5);pile.remove(y[0]);player2.append(y[0]),y.pop(0);fplay=[];ok();redrawgamewindow()
def use(play,player1):
    #removes cards from the play list and player hand list, cards played will be inside both
    while len(play) !=0:
        player1.remove(play[0])
        play.pop(0)
def fplayadd(play,backup):
    global fplay;x=0;fplay=[];global showthis;global used; global gamemode
    #move Aces to the front of poker hands so they look correct
    if round(gamemode[1])==5 and gamemode[2]==7 or gamemode[2]==3 and round(gamemode[1])==5:fplay.append(backup[-1]);backup.insert(0,fplay[0]);fplay=[];backup.pop(-1)
    #adds the cards used to the log for the undo feature
    log.append(backup);log.append(list(main));log.append(list(gamemode)); log.append(1)
    #adds used cards to fplay which shows the played cards, showthis which is a menu option to see that last played hand, and used which stores all used cards for the AI
    while x !=len(play):
        fplay.append(backup[x]);showthis.append(backup[x]);used.append(backup[x])
        x+=1
def cleanup():
    x=0;global fplay;global player1;global player2;global main;global lastmouse1
    #resets lastmouse1
    lastmouse1=[0,0]
    #if player 1's play remove player 1's played cards, else do player 2
    if main[0]==1:
        while x != len(fplay) :
            player1.remove(fplay[x])
            x+=1
    else:
        while x != len(fplay) :
            player2.remove(fplay[x])
            x+=1
    resetplay()
    #sets main to it's correct game state
    if main[0]==1:main=[2,2];return
    if main[0]==2:main=[1,2]
def resetplay():
    global play;global play2;global main
    #resets selected cards for undo button error prevention
    if main[0]==1:play=[]
    else:play2=[]
def addpile(play,pile):
    x = 0
    #adds cards from mulligan or redraw into the pile
    while x !=len(play):
        pile.append(str(play[x]))
        x+=1
def redrawgamewindow():
    global main;global player1;global player2
    #redraws screen using updated information
    screen.fill(background_color);displayhand1();displayhand2();displayfplay()
    if lastmouse1 !=[0,0] and main!=[-3,-3]:pygame.draw.line(screen, (255, 255, 255), [lastmouse1[0] - 3, lastmouse1[1] + 75],[lastmouse1[0] + 3, lastmouse1[1] + 75],width=2)
    #disallows vision of the pile list while you're not allowed to see it
    displaypile();gameend();loadmainbuttons(main);pygame.display.update()
def checkplay(play0,gamemode):
    #takes you to the correct check function to see if your play is legal
    global main; global play;global play2
    #added this function long after global play if hand 1 selected cards, play2 is hand 2 selected cards
    if main[0]==0:return
    play0=sort(play0)
    if len(play0)==1:
        if gamemode[0]==1 or gamemode[0]==0:
            len1check(play0)
    if len(play0)==2:
        if gamemode[0]==2 or gamemode[0]==0:
            len2check(play0)
    if gamemode[0]==3 or gamemode[0]==0:
        if len(play0)==3:
            len3check(play0)
        if len(play0)==4:
            len4check(play0)
        if len(play0)==5:
            len5check(play0)
    #this feature selects your whole hand if you click on the play button, useful for if your last cards are a poker hand
    if main[0]==1:
        if play0==[]:play=list(player1)
        else: play.clear()
    if main[0] == 2:
        if play0==[]:play2=list(player2)
        else:play2.clear()
    redrawgamewindow()
def len1check(play):
    global fplay;global main;backup = list(play)
    #card conversion to number
    play = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in play]
    #check if my card is higher/legal to play on your card
    if gamemode[1] < float(play[-1]):
        play[-1]=float(play[-1])
        if round(gamemode[1]) == 2 and round(play[-1]) == 14: return
        #sets gamemode to singles, gamemode[0]=1
        if gamemode[0]==0:gamemode[0]=1
        gamemode[1] = float(play[-1]);fplayadd(play,backup);cleanup();redrawgamewindow()
    else:
        play[-1]=float(play[-1])
        #check if it's a 2 that is played on an Ace which is legal
        if int(round(gamemode[1]))==14 and round(play[-1])==2:
                gamemode[1] = float(play[-1]);fplayadd(play,backup);cleanup();redrawgamewindow()
def len2check(play):
    global fplay;global main;backup = list(play)
    play = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play]
    #card conversion to number, checks to see if we have a legal pair
    if round(float(play[0])) == round(float(play[1])) and float(play[1])> float(gamemode[1]):
        play[-1] = float(play[-1])
        #can't play Aces on 2's
        if round(gamemode[1]) == 2 and round(play[-1]) == 14: return
        #sets gamemode to pairs, gamemode[0]=2
        if  gamemode[0]==0:gamemode[0]=2
        gamemode[1] = float(play[-1]);fplayadd(play,backup);cleanup();redrawgamewindow()
    else:
        play[-1] = float(play[-1])
        #2's playable on Aces
        if int(round(gamemode[1])) == 14 and round(play[-1]) == 2:
            gamemode[1] = float(play[-1]);fplayadd(play,backup);cleanup();redrawgamewindow()
def len3check(play):
    global fplay;global main;backup = list(play)
    # card conversion to number
    play = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play]
    #checks for three of a kind
    if round(float(play[0])) == round(float(play[1]))== round(float(play[2])) and gamemode[2]<=2:
        if float(play[1]) > float(gamemode[1]) and gamemode[2]<=2 or gamemode[2]<2:
            play[-1] = float(play[-1])
            #no Aces on 2's
            ##  this line gets around a bug that disallows us to declare as int and round 9/1
            x=float(gamemode[1]);x=round(x);y=float(play[1]);y=round(y)
            if x==2 and y==14: return
            #sets gamemode to poker, gamemode[0]=3
            if gamemode[0]==0:gamemode[0]=3
            gamemode[1] = float(play[-1]);gamemode[2]=2;fplayadd(play,backup);cleanup(); redrawgamewindow()
        else:
            play[-1] = float(play[-1])
            #2's legal on Aces
            if int(round(gamemode[1])) == 14 and int(round(play[-1])) == 2:
                gamemode[1] = float(play[-1]);fplayadd(play, backup);cleanup();redrawgamewindow()
def len4check(play):
    global fplay;global main;backup = list(play);thishand=[0,0,0];hastwo=False
    # card conversion to number
    play = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play]
    #check if legal twopair/quads
    if round(float(play[0])) == round(float(play[1])) and round(float(play[2]))==round(float(play[3])):
        #hastwo variable used for twopair of twos beating twopair of aces
        if round(float(play[0])) == 2:hastwo = True
        #set gamemode to poker, gamemode[0]=3
        if gamemode[0]==0: gamemode[0]=3
        #if both pairs are equal we have quads, thishand[2]=6/gamemode[2]=6, otherwise thishand[2]=1/gamemode[2]=1
        if round(float(play[1]))==round(float(play[2])):thishand[2]=6
        else: thishand[2]=1
        thishand[1]=float(play[-1])
        #changes game state to play the new hand
        if thishand[2]>gamemode[2]:
            gamemode[1]=float(thishand[1]);gamemode[2]=int(thishand[2]);fplayadd(play,backup);cleanup();redrawgamewindow();return
        #checks if the new poker hand is hgiher than the old one
        if thishand[2]==gamemode[2]:
            if gamemode[1]<thishand[1]:
                #can't play Aces on 2's
                if round(gamemode[1]) == 2 and round(thishand[1]) == 14: return
                gamemode[1] = float(thishand[1]);fplayadd(play, backup);cleanup();redrawgamewindow();return
            else:
                #2's on Aces legal
                if round(gamemode[1])==14 and hastwo==True:
                    gamemode[1]=float(play[1]);fplayadd(play, backup);cleanup();redrawgamewindow()
def len5check(play):
    global fplay;global main;x=0;global gamemode;backup=list(play);thishand=[0,0,0];hastwo=False
    #checks if we have a flush, sets variable to 4 if we do
    if play[0][-1] == play[1][-1] == play[2][-1] == play[3][-1] == play[4][-1]: thishand[2]=4
    # card conversion to number after we check for flushes
    play = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in play];backup3=list(play)
    while x != len(play):
        play[x] = int(play[x][:-2]);x += 1
    play.sort()
    #allows 2 high flushes to beat Ace high flushes
    if thishand[2] == 4:
        thishand[1] = float(backup3[-1])
        if round(float(backup3[0]))==2:
            hastwo=True
    #check for straights
    if play[0]+1==play[1] and play[1]+1==play[2] and play[2]+1==play[3] and play[3]+1==play[4]:
        #if the play is a straight and a flush we have a straight flush, thishand[1] is the card to beat in the poker hand (high card for straight/stfl)
        if thishand[2] == 4: thishand[2] = 7;thishand[1]=float(backup3[-1])
        else:thishand[2]=3;thishand[1]=float(backup3[-1])
    #check if hand is a through straight
    if play == [2, 11, 12, 13, 14] or play == [2, 3, 12, 13, 14] or play == [2, 3, 4, 13, 14] or play == [2, 3, 4, 5, 14]:
        if thishand[2]==4:thishand[2]=7
        else:thishand[2]=3
        x=0
        #finds the high card for the through straight
        while x<len(play):
            if play[x]+9 ==play[x+1]:
                thishand[1]=float(backup3[x]);break
            else:x += 1
    #fullhouse/4 of a kind check, we don't get a legal kicker with two pair
    x = play.count(play[0]);y = play.count(play[-1])
    #quads check
    if x==4 or y==4:
        thishand[1]=play[2];thishand[2]=6
    #full house check
    if x==3 and y==2 or y==3 and x==2:
        thishand[1]=play[2];thishand[2]=5
    #if we don't have a legal poker hand at this point we return
    if thishand==[0,0,0]:return
    #if the new hand is higher than the old one we game gamemode and move the correct cards to thier new spots
    if gamemode[2]<thishand[2]:gamemode[0]=3;gamemode[1]=float(thishand[1]);gamemode[2]=int(thishand[2]);fplayadd(play,backup);cleanup();redrawgamewindow();return
    #if the poker hand is the same type of hand we have to check to see if the new one is higher
    if gamemode[2]==thishand[2]:
        if gamemode[1] < thishand[1]:
            #can't play 2's on Aces
            if round(gamemode[1])==2 and round(thishand[1])==14: return
            gamemode[1] = float(thishand[1]);gamemode[2] = int(thishand[2]);fplayadd(play, backup);cleanup();redrawgamewindow()
        else:
            #allows 2 high poker hands to be played on Ace high poker hands
            if round(gamemode[1])==14 and round(thishand[1])==2:
                 gamemode[1] = float(thishand[1]);fplayadd(play,backup);cleanup();redrawgamewindow()
            #allows 2 high flushes to be played on Ace high flushes
            if round(gamemode[1])==14 and hastwo==True:
                gamemode[1]=float(backup3[0]);fplayadd(play,backup);cleanup();redrawgamewindow()
def loadmainbuttons(main):
    global p1redraw;global p2redraw;global AI
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
def mullfct(mouse):
    global main;global player1;global player2;global automull;global play;global play2;global pile;global AI
    #starts the mulligan process, once 3 cards by each player are selected they get moved to the pile and the player who goes first is determined
    if main !=[0,0]: return
    if 120 <= mouse[0] <= 200 and 323 <=mouse[1] <=383:
        if automull==True and len(player2)==16 or AI==True and len(player2)==16: mulligan()
        if len(play2) == 3:
            log.append(list(play2));log.append([0,0]);log.append([0,0,0]);log.append(-2);addpile(play2,pile);use(play2,player2);player2=sort(player2);play2.clear();redrawgamewindow()
        if automull==True and len(player1)==16 :   ###does mulligan for player1
            p2copyjustforthis=list(player2);player2=list(player1);mulligan();play=list(play2);player2=list(p2copyjustforthis)
        if len(play) == 3:
            log.append(list(play));log.append([0,0]);log.append([0,0,0]);log.append(-1);addpile(play,pile);use(play,player1);player1=sort(player1);redrawgamewindow()
        if len(pile)==6:
            play=[];play2=[];seewhogoesfirst();redrawgamewindow()
def playfct(mouse,play,play2,main):
    global AI
    #play is the variable where the players hand input if placed, all cards in play are also in the players hands. Checkplay determines if the play is legal
    if main ==[1,0] or main ==[1,1]or main==[1,2]:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            checkplay(play,gamemode)
    if main==[2,0] or main ==[2,1] or main==[2,2]:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            checkplay(play2,gamemode)
            if AI and main==[2,0] or AI and main==[2,1] or AI and main==[2,2]: segmenthand();AImove()
def drawfct(mouse,player1,player2):
    global deck;global main; global p1redraw;global p2redraw;global fplay;global gamemode;global AI
    #draws a card and moves the main to it's proper status, also adds it to the log for the undo function, ok() is the step after the draws are locked in
    if main==[1,2] or main==[1,3]:
        if 640 <= mouse[0] <=720 and 323 <= mouse[1] <= 383:
            fplay=[];decksize();player1.append(deck[0]);log.append(deck[0]);log.append(list(main)); log.append(list(gamemode));log.append(2);deck.pop(0);main[1]=int(main[1]+1)
            if main[1]==4 and p1redraw == False: ok()
            else:redrawgamewindow()
    if main==[2,2] or main==[2,3]:
        if AI:return
        if 640 <= mouse[0] <=720 and 323 <= mouse[1] <= 383:
            fplay=[];decksize();player2.append(deck[0]);log.append(deck[0]);log.append(list(main));log.append(list(gamemode)); log.append(2);deck.pop(0);main[1]=int(main[1]+1)
            if main[1]==4 and p2redraw==False: ok()
            else:redrawgamewindow()
def redrawfct(mouse,player1,player2):
    global pile; global main;global p1redraw;global p2redraw
    tolog=[]
    #redraw is a free action each player gets once per game and they can redraw all cards they drew that turn and draw again, all the code is just removing/adding things to the lists where they belong
    if main==[1,3] and p1redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player1.remove(log[-4]);decksize();player1.append(deck[0]);tolog.append(deck[0]);deck.pop(0)   ###player[-1] to log[-4]
            p1redraw=False;log.append(tolog);log.append(list(main)); log.append(list(gamemode));log.append(3);ok()
    if main==[1,4]and p1redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player1.remove(log[-4]);tolog.append(log[-8]);pile.append(log[-8]);player1.remove(log[-8]);decksize()
            player1.append(deck[0]);tolog.append(deck[0]);deck.pop(0);decksize();player1.append(deck[0]);tolog.append(deck[0]);deck.pop(0);p1redraw=False
            log.append(tolog);log.append(list(main)); log.append(list(gamemode));log.append(3);ok()
    if main==[2,3]and p2redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player2.remove(log[-4]);decksize();player2.append(deck[0]);tolog.append(deck[0]);deck.pop(0)
            p2redraw=False;log.append(tolog);log.append(list(main)); log.append(list(gamemode));log.append(3);ok()
    if main==[2,4]and p2redraw==True:
        if 640<=mouse[0]<=720 and 280<=mouse[1]<=310:
            tolog.append(log[-4]);pile.append(log[-4]);player2.remove(log[-4]);tolog.append(log[-8]);pile.append(log[-8]);player2.remove(log[-8]);decksize()
            player2.append(deck[0]);tolog.append(deck[0]);deck.pop(0);decksize();player2.append(deck[0]);tolog.append(deck[0]);deck.pop(0);p2redraw=False
            log.append(tolog);log.append(list(main));log.append(list(gamemode)); log.append(3);ok()
def okfct(mouse,main):
    if main[1]==3 or main[1]==4:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            ok()
def ok():
    global main;global gamemode; global player1;global player2;global fplay;global showlast;global showthis;global log;global lastmouse1
    showlast=[];showlast=list(showthis);showthis=[]
    fplay=[];log.append(0);log.append(list(main));log.append(list(gamemode));log.append(6);gamemode=[0,0,0];play.clear();play2.clear();lastmouse1=[0,0]
    #changes turn in game
    if main[0]==1:main=[2,1];player1=sort(player1)
    else:main=[1,1];player2=sort(player2)
    redrawgamewindow()

def passturn():
    global main;global AI
    #turns off button if the AI exists
    if AI==True and main[0]==2:return
    #passes the turn in game
    if main[1] != 1: return
    if 120 <= mouse[0] <= 200 and 280 <= mouse[1] <= 310:
        if main[0] == 1:
            log.append(0);log.append(list(main));log.append(list(gamemode)); log.append(4);main = [2, 0];redrawgamewindow()
        else:
            log.append(0);log.append(list(main));log.append(list(gamemode)); log.append(4);main = [1,0];redrawgamewindow()

def gameend():
    global main;global concede;global backupmain
    #checks to see if the game is over
    if backupmain==[0,0] and concede==True: player1.clear()
    if backupmain[0] == 1 and concede == True: player2.clear()
    if backupmain[0] == 2 and concede == True: player1.clear()
    if len(player1) == 26: player2.clear()
    if len(player2) == 26: player1.clear()
    if len(player1) == 0: main = [-2, 0];screen.fill(background_color);displayhand1();displayhand2();displayfplay();displaypile();a = pygame.image.load('ponewin.png');screen.blit(a, (380, 480));pygame.display.update();return
    if len(player2) == 0: main = [-3, 0];screen.fill(background_color);displayhand1();displayhand2();displayfplay();displaypile();a = pygame.image.load('ptwowin.png');screen.blit(a, (380, 50));pygame.display.update();return

def gameendfct():
    global main; global replay
    #button to play again
    if 380 <= mouse[0] <= 380 + 251 and 480 <= mouse[1] <= 480 + 76 and main == [-2, 0]: replay=False;startgame()
    if 380 <= mouse[0] <= 380 + 251 and 50 <= mouse[1] <= 50 + 76 and main == [-3, 0]: replay=False;startgame()


    ######################   ACTUAL GAME STUFF  ^^^^^


def testbutton(mouse,gamemode,main):
    #used to test the contents of lists
    if 70 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
       print('gamemode =',gamemode);print('log is',log)

def buttons():
    #a list of clickable buttons in the game, have to put this in a different area in the code than everything else
    makehandbuttons(mouse,player1);makehand2buttons(mouse,player2);makepilebuttons(mouse,pile);testbutton(mouse,gamemode,main);passturn();optionbuttons()
    playfct(mouse,play,play2,main);okfct(mouse,main);mullfct(mouse);drawfct(mouse,player1,player2);redrawfct(mouse,player1,player2);gameendfct()
def startgame():
    #all actions needed to start the game
    global player1;global player2;global main;global gamemode;global backupdeck;global deck;global AIinfo
    global p1redraw;global p2redraw;global optionslist;global concede;global replay;global optionslist
    if replay==True:deck.clear();deck=list(backupdeck)
    else:deck=[];backupdeck.clear();replay=False;getdeck()
    player1.clear();player2.clear();play.clear();fplay.clear();play2.clear();main=[0,0]; gamemode=[0,0,0];pile.clear();p1redraw=True;p2redraw=True
    showlast.clear();showthis.clear();used.clear();log.clear();concede=False;optionslist=[0,0,0,0,0,0];AIinfo=[False,False,False,False,False,0,[],False]
    deal();player1 = sort(player1);player2 = sort(player2);redrawgamewindow()

def optionbuttons():
    #options menu clickable buttons
    global main; global backupmain;global optionslist;global showthis;global showlast;global concede;global altreveal;global replay;global AI;global automull
    if main !=[-3,-3] and 10 <= mouse[0] <= 40 and 323 <= mouse[1] <= 383:
        backupmain=list(main);main=[-3,-3];optionwindow();return
    if main==[-3,-3] and 10 <= mouse[0] <= 100 and 323 <= mouse[1] <= 383:
        main=list(backupmain);redrawgamewindow()
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 384 <= mouse[1] <= 444:   #showthisoff
        if optionslist[0]==0: optionslist=[1,0,0,0,0,0];displayshowstuff(showthis)  ###maybecut
        else: optionslist[0]=0
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 445 <= mouse[1] <= 505:   #showlastoff
        if optionslist[1]==0: optionslist=[0,1,0,0,0,0];displayshowstuff(showlast)  ###maybecut
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
            concede=True;gameend()
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 262 <= mouse[1] <= 322: #undo button
        undo()
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 201 <= mouse[1] <= 261:
        if optionslist[2]==0:optionslist=[0,0,1,0,0,0]
        elif optionslist[2]==1:replay=True;startgame()
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 140 <= mouse[1] <= 200:
        if AI: AI=False
        else: AI=True
    if main == [-3, -3] and 10 <= mouse[0] <= 90 and 79 <= mouse[1] <= 139:
        if automull: automull=False
        else: automull=True
    if main==[-3,-3]:optionwindow()
def optionwindow():
    #pictures for the options menu buttons
    global optionslist;global altreveal;global concede
    screen.fill(background_color);a=pygame.image.load('back.png');screen.blit(a, (10, 323));a=pygame.image.load('undo.png');screen.blit(a, (10, 262))
    if optionslist[0]==0: a=pygame.image.load('showthisoff.png');screen.blit(a, (10, 384))
    else: a=pygame.image.load('showthison.png');screen.blit(a, (10, 384));displayshowstuff(showthis)
    if optionslist[1]==0: a=pygame.image.load('showlastoff.png');screen.blit(a, (10, 445))
    else: a=pygame.image.load('showlaston.png');screen.blit(a, (10, 445));displayshowstuff(showlast)
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
def displayshowstuff(list):
    y=0
    #displays cards for showthishand option and show last hand option
    while y < len(list):
        card = list[y]
        x = pygame.image.load(f'{card}.png')
        if y < 11: screen.blit(x, (170 + y * 75, 20))
        if 11 <= y <= 23: screen.blit(x, (170 + (y - 13) * 75, 133))
        if 24 <= y <= 36: screen.blit(x, (170 + (y - 26) * 75, 246))
        y += 1
def decksize():
    global showthis;global deck
    #if we run out of cards we need to reshuffle the used pile back in
    if len(deck) !=0: return
    if len(deck)==0:
        x=0
        while x<len(showthis):
            used.remove(showthis[x])
            x+=1
    deck=list(used)
    random.shuffle(deck)
def undo():
    global log; global main;x=0;global pile;global player1; global player2;global showthis;global showlast;global p1redraw;global p2redraw;global fplay;global gamemode;global backupmain;global deck
    #every event is added here as [cards used,main,gamemode,type of action]; types of action: -1,-2 mulligans, 1 play, 2 draw, 3 redraw, 4 is pass turn, 5 is pile, 6 is change of turn
    #AI 7 play 8 AI draw 9 AI pile
    if len(log)==0: main=list(backupmain);redrawgamewindow();return
    play.clear();play2.clear()
    if log[-1]==-1:
        main=log[-3]
        while x < len(log[-4]):
            player1.append(log[-4][x]);pile.remove(log[-4][x]);x += 1
        main=list(log[-3]);updatefplay();player1=sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=[0,0,0];seewhogoesfirst();redrawgamewindow();return
    if log[-1]==-2:
        main=log[-3]
        while x < len(log[-4]):
            player2.append(log[-4][x]);pile.remove(log[-4][x]);x += 1
        main=list(log[-3]);updatefplay();player2=sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=[0,0,0];seewhogoesfirst();redrawgamewindow();return
    if log[-1]==1:
        while x < len(log[-4]):
            log[-4][x] = str(log[-4][x]);x += 1
        log[-4] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in log[-4]]
        if log[-3][0]==1:
            x=0
            while x<len(log[-4]):
                player1.append(log[-4][x]);used.remove(log[-4][x])
                if log[-4][x] in showthis:
                    showthis.remove(log[-4][x])
                x+=1
            main=log[-3];updatefplay();player1 = sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
            if main[1]==1:gamemode=list([0,0,0])
            else: gamemode=list(log[-2])
            seewhogoesfirst();redrawgamewindow();return
        if log[-3][0]==2:
            x=0
            while x < len(log[-4]):
                player2.append(log[-4][x]);used.remove(log[-4][x])
                if log[-4][x] in showthis:
                    showthis.remove(log[-4][x])
                x+=1
            main=log[-3];updatefplay();player2 = sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
            if main[1]==1:gamemode=list([0,0,0])
            else: gamemode=list(log[-2])
            seewhogoesfirst();redrawgamewindow();return
    if log[-1]==2:
        if log[-3][0] == 1:
            main=log[-3];updatefplay();player1.remove(log[-4]);deck.insert(0,log[-4]);player1 = sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=list(log[-2]);seewhogoesfirst();redrawgamewindow();return
        if log[-3][0] == 2:
            main=log[-3];updatefplay();player2.remove(log[-4]);deck.insert(0,log[-4]);player2 = sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=list(log[-2]);seewhogoesfirst();redrawgamewindow();return
    if log[-1]==3:
        if log[-3][0] == 1:
            if log[-3][1] == 3:
                p1redraw = True;player1.remove(log[-4][1]);player1.append(log[-4][0]);pile.remove(log[-4][0])
                main = log[-3];updatefplay();player1 = sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();return
            if log[-3][1]==4:
                p1redraw=True
                player1.remove(log[-4][2]);player1.remove(log[-4][3]);player1.append(log[-4][0]);player1.append(log[-4][1]);pile.remove(log[-4][0]);pile.remove(log[-4][1])
                main=log[-3];updatefplay();player1 = sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();return
        if log[-3][0] == 2:
            if log[-3][1] == 3:
                p2redraw = True;player2.remove(log[-4][1]);player2.append(log[-4][0]);pile.remove(log[-4][0])
                main = log[-3];updatefplay();player2 = sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();return
            if log[-3][1] == 4:
                p2redraw = True
                player2.remove(log[-4][2]);player2.remove(log[-4][3]);player2.append(log[-4][0]);player2.append(log[-4][1]);pile.remove(log[-4][0]);pile.remove(log[-4][1])
                main=log[-3];updatefplay();player2 = sort(player2);log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();return
    if log[-1]==4:
        main=log[-3];updatefplay();log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();return
    if log[-1]==5:
        if log[-3][0]==1:
            player1.remove(log[-4]);pile.append(log[-4])
        if log[-3][0]==2:
            player2.remove(log[-4]);pile.append(log[-4])
        main = log[-3];updatefplay();log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();return
    if log[-1]==6:
        gamemode=list(log[-2]);main=log[-3];updatefplay();log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow();
        if log[-1]==5:undo()
        return
    if log[-1]==7:
        if type(log[-4])==str:player2.append(log[-4])  ###changed not sure about this one
        else:
            for i in log[-4]:
                player2.append(i);
                if i in used:
                    used.remove(i)
                if i in showthis:
                    showthis.remove(i) ##show this/used remove(i)
        fplay=list(log[-4]);player2=sort(player2);gamemode=list(log[-2]);main=log[-3];updatefplay();log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow()
    if log[-1]==8:
        if len(log[-4])<3:
            for i in reversed(log[-4]): deck.insert(0,i);player2.remove(i)
        if len(log[-4])==4:
            counter=0
            for i in reversed(log[-4]):
                deck.insert(0,i)
                if counter<=1:player2.remove(i)
                if counter>=2:pile.remove(i)
                counter+=1
        p2redraw=True;player2=sort(player2);gamemode=list(log[-2]);main=log[-3];updatefplay();log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1);seewhogoesfirst();redrawgamewindow()
def updatefplay():
    global fplay;global log;x=1;global main
    #updates fplay when the undo button is used, needs to be fixed
    if main[1]==1: fplay=[];return
    while len(log)>1+(x*4):   ### not sure about this one
        if log[-1+(x*-4)]==1:
            if log[-3][1]==2: fplay=list(log[-4+(x*-4)]);return
            else: return
        else:x += 1
    fplay=[]
def seewhogoesfirst():
    global main;global log;global pile
    #function to see who has the lowest card in hand and that player goes first
    if len(log)==0: return
    if len(pile)!=6:return
    if log[-1]==-1 or log[-1]==-2 or main==[0,0]:
        x = (player1[0].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4'));y = (player2[0].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4'))
        if x < y:
            main = [1, 1]
        else:
            main = [2, 1]


############################### MULLIGAN AND SEGMENT CODE VVVVVV  WARPAIRS CODE ^^^^^^^^^^

def n2aksetup():
    global hand;global outliers;x=0; global n2akout;global quads;this=[];temp=[];global player2;hand=list(player2);global hardmull
    #remove 2ak and add to its own list
    while x != len(hand):
        if int(hand[x][:-1]) == 2 or int(hand[x][:-1]) == 13 or int(hand[x][:-1]) == 14:  ##terrible code but 14 literally didnt work
            n2akout.append(hand[x]);hand.pop(x);x -= 1
        x += 1
    #change hand into int
    hand = [x[:-1] for x in hand];hand = list(map(int, hand));x = 0;y = 0
    #move the outliers to its list
    while x != len(hand):
        if hand[x] == hand[x + 1]:
            x += 1;y += 1
            if x==len(hand)-1:break
            else:continue
        else:
            if y == 0: outliers.append(hand[x])
        x += 1;y = 0
        if x == len(hand) - 1:break
    if y == 0: outliers.append(hand[x])
    x=0
    #sets quads, then removes it from hand
    for i in hand:
        if hand.count(i)==4 and i not in quads:quads.append(i)
    for i in quads:hand.remove(i);hand.remove(i);hand.remove(i);hand.remove(i)

    #change 2ak to numbers
    while x!=len(n2akout):
        n2akout[x]=int(n2akout[x][:-1]);x+=1
    #check for quads in 2ak
    for i in n2akout:
        k=n2akout.count(i)
        for j in range(k):
            if k==4 and i not in quads: quads.append(i);n2akout.remove(i)
    #add outliers to the mulligan
    for i in outliers:
        this.append(i)
        if len(this)==3: break
    #if we don't have enough outliers we figure out what gets mulliganed, 'this'  variable is the list of mulligned cards and temp is the variabled turned into cards
    if len(this) < 3: hardmull = [];hardermull();hardmull.sort();this = list(hardmull)
    #readjust hand and outliers to remove the mulligan and also adds the correct outliers to outliers
    outliersonlythis=list(outliers);handbackup=list(hand)
    for i in this:
        if i in hand:hand.remove(i)
        if i in outliersonlythis:outliersonlythis.remove (i)
    for i in hand:
        if hand.count(i)==1 and i not in outliers:outliersonlythis.append(i)
    mulltiebreaker=sum(outliersonlythis)
    x=0;y=0
    #find cards in the hand and add it to the mulligan possibilities
    while x!=3:
        while y!=len(player2):
            if this[x]==int(player2[y][:-1])and player2[y] not in temp:temp.append(player2[y]);break
            y+=1
        x+=1;y=0
    if len(outliersonlythis)>0: mullnotes.append(len(outliersonlythis))
    else:mullnotes.append(0)
    mullnotes.append(mulltiebreaker);mullnotes.append('b');mull.append(temp);hand=list(handbackup)

def finalstraight():
    must=[];global hand;global outliers;global quads; straightmull=[];global player2;testmust=[[],[],0];must1=0;global mull;global hardmull;hand0=[];handbackup=list(hand)
    #not enough outliers for a straight, return
    #find possible straights, and finish them into variable must
    for i in outliers:
        for j in outliers:
            if 4 >= j - i >= 0: testmust[0].append(j)
        if len(testmust[0]) < 3:testmust[0].clear();continue
        else:
            #this fills in the middle
            for k in range (testmust[0][-1]-testmust[0][0]):
                if testmust[0][0]+k in hand:
                    if testmust[0][0]+k not in testmust[0]:testmust[1].append(testmust[0][0]+k)
                else:testmust[0].clear();testmust[1].clear();break

            testmust[2] = int(len(testmust[0]));testmust[0] = testmust[0] + list(testmust[1]);testmust[0].sort();testmust[1].clear()
            if len(testmust[0]) == 0: continue
            #this fills in the ends, because the loop only loops ythrough outliers we need the before straight part
            if len(testmust[0]) != 5:
                if testmust[0][0] - 1 in hand and len(testmust[0]) != 5: testmust[0].append(testmust[0][0] - 1);testmust[0].sort()
                if testmust[0][0] - 1 in hand and testmust[0][0] - 1 in hand and len(testmust[0]) != 5:testmust[0].append(testmust[0][0] - 1);testmust[0].sort()
                if testmust[0][-1] + 1 in hand and len(testmust[0]) != 5: testmust[0].append(testmust[0][-1] + 1);testmust[0].sort()
                if testmust[0][-1] + 1 in hand and testmust[0][-1] + 2 in hand and len(testmust[0]) != 5:testmust[0].append(testmust[0][-1] + 1);testmust[0].sort()
            if len(testmust[0]) != 5: testmust[0].clear();testmust[1].clear();testmust[2] = 0
            if testmust[2] > must1: must = list(testmust[0]);must1 = int(testmust[2])
            testmust[0].clear();testmust[1].clear();testmust[2] = 0
    #continue if we have a straight, return if we have no possible straights
    if not must:hand=list(handbackup);return
    #remove straight from hand
    #straight adjustment x2 we mull the low cards instead of the top end of the straight
    if must[-1]+1 in outliers: hand.sort();must.pop(0);outliers.remove(must[-1]+1);must.append(must[-1]+1)
    if must[-1]+1 in outliers: hand.sort();must.pop(0);outliers.remove(must[-1] + 1);must.append(must[-1] + 1)
    for i in must:
        hand.remove(i)
        if i in outliers: outliers.remove(i)
    #adjust the rest of the cards that need adjusting from removing the straight from the hand
    for i in hand:
        if hand.count(i)==1 and i not in outliers: outliers.append(i)
    outliers.sort()
    for i in outliers:
        straightmull.append(i)
        if len(straightmull)==3:break
    #if we have less then 3 outliers we have to figure out what gets mulliganed using hardermull
    if len(straightmull)<3:hardmull=[];hardermull();hardmull.sort();straightmull=list(hardmull)
    #remove the correct cards from the hand and add it to the list of mulligan possibilities
    for i in straightmull:
        if i in hand:hand.remove(i)
    for i in hand:
        if hand.count(i)==1:hand0.append(i)
    outliers=list(hand0);x = 0;y = 0
    mulltiebreaker=sum(outliers)
    #turn the numbers in the mulligan into cards
    while y!=3:
        if int(player2[x][:-1])==straightmull[y]:
            straightmull[y]=str(player2[x]);y+=1
        x+=1
    #append the cards mulliganed and the number of outliers removed to the list mull/mullnotes
    if len(outliers)<0:mullnotes.append(0)
    else:mullnotes.append(int(len(outliers))) #test
    mull.append(straightmull);mullnotes.append(mulltiebreaker);mullnotes.append('t');hand=list(handbackup)


def finalflush():
    pokerremove=[];must=[];w=0;x = 0;y=0;possflush=[];global hand; global outliers;global quads;flushmull=[];firsttwo=[];flushnotes=[];oldhand=list(hand);oldoutliers=list(outliers);temp=[];global player2;global hardmull;hand0=[]
    # not enough outliers for a flush, return
    suits = [[], [], [], []]
    #seperate hand into suits, skip 2ak
    while x != len(player2):
        if int(player2[x][:-1])==2 or int(player2[x][:-1])==13 or int(player2[x][:-1])==14: x+=1; continue
        if int(player2[x][:-1]) in quads: x += 1;continue
        if player2[x][-1:] == 'd': suits[0].append(int(player2[x][:-1]))
        if player2[x][-1:] == 'c': suits[1].append(int(player2[x][:-1]))
        if player2[x][-1:] == 'h': suits[2].append(int(player2[x][:-1]))
        if player2[x][-1:] == 's': suits[3].append(int(player2[x][:-1]))
        x += 1
    x = 0
    #check if we have 5 in a suit
    while x != len(suits):
        if len(suits[x]) >= 5:
            possflush.append(suits[x])
            if x==0:flushnotes.append('d')
            if x == 1: flushnotes.append('c')
            if x == 2: flushnotes.append('h')
            if x == 3: flushnotes.append('s')
        x += 1
    #return if we don't have 5
    if not possflush:return
    x=0;y=0;z=1;a=0
    #check if we have a viable straightflush
    while x != (len(possflush)):  ### stfl test, pretty sure this is correct, y should only be 0 if its 5 card stfl and max 1 if it's 6 cards, needs to be redone
        while y <= len(possflush[x]) - 4: #not 100% about this sign
            if possflush[x][y]+z in possflush[x] and z>4: z+=1; continue
            else:
                if z>=4:
                    for i in range (z):
                        temp.append(possflush[x][y]+a);a+=1
                a=0;z=0;y+=1
                if temp: break
        if temp:possflush.append(temp);flushnotes.append(flushnotes[x]+'stfl');temp=[]
        x+=1
    x=0;temp=[]
    #loop through all available flushes
    while w!=len(possflush):
        while x!=len(possflush[w]):
            #check if we have enough cards to have a viable flush
            if int(possflush[w][x]) in outliers:must.append(possflush[w][x])
            else:
                if len(firsttwo)<2:firsttwo.append(possflush[w][x])
            x+=1
        #we don't have enough for a flush, continue
        if len(must)<3:must=[];w+=1;x=0;flushnotes.pop(0);continue
        #we have 3 outliers for a flush so we use them and the lowest 2 usable in suit to make our flush
        if len(must)==3:pokerremove=list(must);pokerremove.append(firsttwo[0]);pokerremove.append(firsttwo[1]);pokerremove.sort();outliers.append(firsttwo[0]);outliers.append(firsttwo[1]);outliers.sort()
        #we have 4 outliers for a flush and we use the lowest available in suit to make our flush
        if len(must)==4:pokerremove=list(must);pokerremove.append(firsttwo[0]);pokerremove.sort();outliers.append(firsttwo[0]);outliers.sort()
        #if we have more than 5 usable cads of a suit we use the lowest 5
        if len(must)>5:
            for i in must:
                must.pop(0)
                if len(must)==5:break
        #remove the cards from where they need to go and add them to thier new lists, pokerremove/must is our flush
        for i in pokerremove: hand.remove(i)
        outliers=[]
        for i in hand:
            if hand.count(i) == 1: outliers.append(i)
        #add new outliers to our mulligan
        for i in outliers:
            if len(flushmull)<3:flushmull.append(i)
        #if we don't have enough outliers for our mulligan we figure out what cards to mulligan
        if len(flushmull) <3:hardmull=[];hardermull();hardmull.sort();flushmull=list(hardmull)
        #remove excess pairs from outliers, I don't remember why we need to do this
        for i in flushmull:
            if i in hand: hand.remove(i)
        for i in hand:
            if hand.count(i) == 1: hand0.append(i)
        outliers = list(hand0)
        mulltiebreaker=sum(outliers)
        x=0; y=0
        # remove the correct cards from hand and add it to the list of possibilities to mulligan
        for i in flushmull:
            for j in player2:
                if i==int(j[:-1]) and j[-1]!=flushnotes[0]:  # stops mulligan from mulliganing the flush
                    if j in temp:continue
                    else: temp.append(j);break
                if len(temp)==3:break
            if len(temp) == 3: break
        mull.append(temp)
        if len(outliers) <0: mullnotes.append(0)
        else: mullnotes.append(len(outliers))
        mullnotes.append(mulltiebreaker);mullnotes.append(flushnotes[0]);flushnotes.pop(0)
        w+=1;x=0;hand=list(oldhand);firsttwo=[];outliers=list(oldoutliers);flushmull=[];must=[];temp=[]

def hardermull():
    global quads;global hardmull;global outliers;global n2akout;global hand;n2akline=['13d', '14d', '13c', '14c', '2d', '2c', '2h', '13h', '14h', '2s', '13s', '14s'];n2akoutliers=[0, 0, 0];c2=0;c3=0;c22=0;c33=0;c333=0;global player2
    for i in hand:
        #figures out low pair and low trips, c22 is second lowest pair
        if hand.count(i)==2 and c2==0:c2=i
        if hand.count(i) == 3 and c3==0:c3=i
        if hand.count(i) == 2 and c22==0 and i!=c2: c22 = i
        if hand.count(i)==3 and c33==0 and i!=c3: c33=i
        if hand.count(i)==3 and c333==0 and c33!=0 and i!=c3 and i!=c33:c333=i
    if not quads:
        if len(outliers)==1 and c2 !=0:hardmull.append(c2);hardmull.append(c2);hardmull.append(outliers[0])
        if len(outliers)==1 and len(hardmull)!=3 and c33 !=0:hardmull.append(outliers[0]);hardmull.append(c3);hardmull.append(c33)
        if len(outliers)==1 and len(hardmull)!=3 and c33 ==0:
            if outliers[0]>c3:hardmull.append(outliers[0]);hardmull.append(c3);hardmull.append(c3)
            else:hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
        if len(outliers)==2 and c3==0:
            hardmull.append(c2);hardmull.append(outliers[0])
            if c2>outliers[1]:hardmull.append(outliers[1])
            else: hardmull.append(c2)
        if len(outliers)==2 and c3!=0:hardmull.append(c3);hardmull.append(outliers[0]);hardmull.append(outliers[1])
        if len(outliers)==0 and c3!=0:hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
        if len(outliers)==0 and c3==0:hardmull.append(c2);hardmull.append(c2);hardmull.append(c22)
        hardmull.sort()
    else:
        #outliers are in base numbers, we already removed poker hands at this point
        backup2ak=list(n2akout);y=0
        #while y !=len(n2akout):n2akout[y]=int(n2akout[y][:-1]);y+=1 commented out 7/28
        n2akoutliers[0]=n2akout.count(2);n2akoutliers[1]=n2akout.count(13);n2akoutliers[2]=n2akout.count(14);y=0
        if len(outliers)==1:
            hardmull.append(outliers[0])
            if n2akoutliers==[1,1,1]:
                for i in n2akline:
                    if i in player2: #only referance to player2
                        hardmull.append(int(i[:-1]));y+=1
                    if y==2:break
            if c33 !=0 and len(hardmull)!=3:
                hardmull.append(c3)
                hardmull.append(c33)
            if c3 !=0 and 3 in n2akoutliers and len(hardmull)!=3:
                if n2akoutliers[0]==3:hardmull.append(c3);hardmull.append(2)
                if n2akoutliers[1] == 3: hardmull.append(c3);hardmull.append(13)
                if n2akoutliers[2] == 3: hardmull.append(c3);hardmull.append(14)
            if c2 !=0and len(hardmull)!=3:hardmull.append(c2);hardmull.append(c2)
            if len(quads)>=2 and len(hardmull)!=3:
                quads.sort();hardmull.append(quads[0]);hardmull.append(quads[0])
            if c3!=0 and len(hardmull)!=3:
                if hardmull[0]<c3:hardmull.append(c3);hardmull.append(c3)
                else:hardmull.clear();hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
            if len(hardmull)!=3:
                for i in n2akline:
                    if i in player2:
                        hardmull.append(int(i[:-1]))
                        if len(hardmull)==3: break
        if len(outliers)==2:
            hardmull.append(outliers[0]);hardmull.append(outliers[1])
            #1 outlier in n2ak, take one of them
            if 1 in n2akoutliers and len(hardmull)!=3:
                mulloneofthese=[]
                if n2akoutliers[0]==1: mulloneofthese.append(2)
                if n2akoutliers[1]==1: mulloneofthese.append(13)
                if n2akoutliers[2]==1: mulloneofthese.append(14)
                #this makes it so that we follow the 2akline with this block of code
                for i in n2akline:
                    if i in hand and int(i[:-1]) in mulloneofthese:
                        hardmull.append(i)
            #2 outliers in n2ak, take according to n2akline
            if n2akoutliers.count(1)==2 and len(hardmull)!=3:
                for i in n2akline:
                    if i in hand:hardmull.append(i)
            #the rest of the possibilities
            if c3 !=0 and len(hardmull)!=3: hardmull.append(c3)
            if c2!=0 and len(hardmull)!=3:hardmull.append(c2)
            if len(hardmull)==2:
                for i in n2akline:
                    if i in player2:
                        hardmull.append(int(i[:-1]));break
        if len(outliers)==0:  ##here is where the changes go
            if n2akoutliers.count(1)==0 and len(hardmull)!=3:
                if c2!=0 and c3!=0 and c2<c3:hardmull.append(c2);hardmull.append(c2);hardmull.append(c22)  # do I need to do this clause on other things
                if c2!=0 and c3!=0 and c2>c3:hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
                if c3==0 and c2!=0 and c22!=0:hardmull.append(c2);hardmull.append(c2);hardmull.append(c22)
            if n2akoutliers.count(1) == 1 and len(hardmull)!=3:
                #break low trips(c3) if we have 3 trips at this stage including 2ak
                if c333!=0:hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
                if c33!=0 and 3 in n2akoutliers and len(hardmull)!=3:hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
                if c3!=0 and n2akoutliers.count(3)==2 and len(hardmull)!=3: hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
                #if we have a 4 pair+trip hand we mull bottom pair (c2) +2ak
                if c2 != 0 and len(hardmull) != 3:
                    hardmull.append(c2);hardmull.append(c2);mulloneofthese = []
                    if n2akoutliers[0] == 1 and len(hardmull) != 3: mulloneofthese.append(2)
                    if n2akoutliers[1] == 1 and len(hardmull) != 3: mulloneofthese.append(13)
                    if n2akoutliers[2] == 1 and len(hardmull) != 3: mulloneofthese.append(14)
                    for i in n2akline:
                        if i in hand and int(i[:-1]) in mulloneofthese:
                            hardmull.append(i)
                if len(hardmull) != 3:  #idk if this is needed
                    for i in n2akline:
                        if i in player2:
                            hardmull.append(int(i[:-1]))
                            if len(hardmull) == 3: break
            if n2akoutliers.count(1) == 2 and len(hardmull)!=3:
                #first add a n2ak outlier, if we have a low pair break it, otherwise break low quads, note: not sure if there are any more cases beyond this but it is extremely low %
                if c3!=0:
                    hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
                if c2 !=0 and c22!=0 and len(hardmull)!=3:
                    hardmull.append(c2);hardmull.append(c2);hardmull.append(c22)
                for i in n2akline:
                    if i in player2:
                        if len(hardmull)!=3:hardmull.append(int(i[:-1]))
                        else: break
                if len(quads)==2 and len(hardmull)!=3:
                    hardmull.append(quads[0]);hardmull.append(quads[0])
            if n2akoutliers.count(1) == 3 and len(hardmull)!=3:
                if c3!=0:
                    hardmull.append(c3);hardmull.append(c3);hardmull.append(c3)
                if c2 !=0 and c22!=0 and len(hardmull)!=3:
                    hardmull.append(c2);hardmull.append(c2);hardmull.append(c22)
                if len(hardmull)!=3:hardmull.append(n2akout[0]);hardmull.append(n2akout[1]);hardmull.append(n2akout[2])
    hardmull.sort()


####################### SEGMENT CODE VVV ######### MULLIGAN CODE ^^^^^^^^

def remove2ak():
    global p2copy
    #remove 2ak from hand because we won't use them in poker hands and we don't want them to interfere
    for i in p2copy:
        if int(i[:-1])==2 or int(i[:-1])==13 or int(i[:-1])==14:
            segp2[0].append(i)
    for i in segp2[0]:p2copy.remove(i)
def detectpairs(p2copy):
    hand = list(p2copy);x=0;count=1;global segp2;global finalseg;numberhand=[];currentnumber=0
    #move pairs to segp2[2], trips to segp2[3], and quads to segp2[4]
    for i in p2copy:
        numberhand.append(int(i[:-1]))
    for i in numberhand:
        if i == currentnumber: continue
        if not currentnumber: currentnumber = i
        move = numberhand.count(i)
        if move == 1:
            for j in p2copy:
                if str(i) == j[:-1]:
                    segp2[1].append(j)
        if move == 2:
            for j in p2copy:
                if str(i) == j[:-1] and j not in segp2[2]:segp2[2].append(j)
        if move == 3:
            for j in p2copy:
                if str(i) == j[:-1] and j not in segp2[3]:segp2[3].append(j)
        if move == 4:
            for j in p2copy:
                if str(i) == j[:-1] and j not in segp2[4]:segp2[4].append(j)
        if i != currentnumber: currentnumer = i
    finalseg=copy.deepcopy(segp2)
def redetectpairs(hand):
    #make sure you use copyseg as a variable; exact same code as detectpairs except this doesn't change segp2, it changes copyseg
    x=0;count=0;global copyseg;global segp2
    organizer=[[],[],[],[],[]]
    while x!=len(hand):
        if len(hand)==1:organizer[1].append(hand[x]);break
        if hand[x][:-1]==hand[x+1][:-1]:
            count+=1;x+=1
            if x!=len(hand)-1: continue
        if count==0:organizer[1].append(hand[x])
        if count==1:organizer[2].append(hand[x-1]);organizer[2].append(hand[x])
        if count==2:organizer[3].append(hand[x-2]);organizer[3].append(hand[x-1]);organizer[3].append(hand[x])
        if count == 3: organizer[4].append(hand[x - 3]);organizer[4].append(hand[x - 2]);organizer[4].append(hand[x-1]);organizer[4].append(hand[x])
        count = 0;x += 1
        #gets the last card in the sequence if it isn't a pair
        if x==len(hand)-1:organizer[1].append(hand[x]);break
    copyseg[1]=copy.deepcopy((organizer[1]));copyseg[2]=copy.deepcopy(list(organizer[2]));copyseg[3]=copy.deepcopy(list(organizer[3]));copyseg[4]=copy.deepcopy(list(organizer[4]))
def detectflush(p2copy):
    x=0;suits=[[],[],[],[]];y=0
    #finds flushes
    while x!=len(p2copy):
        if p2copy[x][-1:] == 'd': suits[0].append(p2copy[x])
        if p2copy[x][-1:] == 'c': suits[1].append(p2copy[x])
        if p2copy[x][-1:] == 'h': suits[2].append(p2copy[x])
        if p2copy[x][-1:] == 's': suits[3].append(p2copy[x])
        x+=1
    x=0
    #if 2 outliers aren't in the flush then it most likely can't be used
    while x!=len(suits):
        if len(suits[x]) >=5:
            for i in suits[x]:
                if i in segp2[1]:y+=1
            segp2[6].append(suits[x])
            if x==0: segp2[8].append('d')
            if x == 1: segp2[8].append('c')
            if x == 2: segp2[8].append('h')
            if x == 3: segp2[8].append('s')
            segp2[8].append(int(y))
            y=0
        x+=1
def detectstr(p2copy):
    x = 0;y=0;st=[]
    #finds straights
    if not p2copy:return
    while x!=len(p2copy)-1:
        if int(p2copy[x][:-1])==int(p2copy[x + 1][:-1]): st.append(p2copy[x]);x+=1;continue
        if int(p2copy[x + 1][:-1]) == int(p2copy[x][:-1])+1:st.append(p2copy[x]);y+= 1;x+=1;continue
        else:
            if y>=4:st.append(p2copy[x]);segp2[5].append(st);st=[];y=0
            else:st=[];y=0
        x+=1
    if y >= 4:st.append(p2copy[x]);segp2[5].append(st)
def remove(removezone):
    #only usable for copyseg
    y=0;copy1=copy.deepcopy(removezone);global copyseg
    for i in removezone:
        if i in copyseg[1]:
            copyseg[1].remove(i);copy1.remove(i);y+=1
            if y == 5: break
    removezone=list(copy1)
    for i in removezone:
        if i in copyseg[3]:
            copyseg[3].remove(i);copy1.remove(i);y+=1
            if y == 5: break
    removezone = list(copy1)
    for i in removezone:
        if i in copyseg[2]:
            copyseg[2].remove(i);y+=1
            if y==5:break
    remake=list(copyseg[1]+copyseg[2]+copyseg[3])
    copyseg[1]=[];copyseg[2]=[];copyseg[3]=[];remake=sort(remake);redetectpairs(remake)
def removeflush(removezone):
    #only usable for copyseg
    y=0;copy1=copy.deepcopy(removezone);global copyseg;flush=[]
    for i in removezone:
        if y == 5: break
        if i in copyseg[1]:
            copyseg[1].remove(i);copy1.remove(i);flush.append(i);y+=1
            if y == 5: break
        if y == 5: break
    removezone=list(copy1)
    for i in removezone:
        if y == 5: break
        if i in copyseg[3]:
            copyseg[3].remove(i);copy1.remove(i);flush.append(i);y+=1
            if y == 5: break
        if y == 5: break
    removezone = list(copy1)
    for i in removezone:
        if y == 5: break
        if i in copyseg[2]:
            copyseg[2].remove(i);flush.append(i);y+=1
            if y==5:break
        if y == 5: break
    remake=list(copyseg[1]+copyseg[2]+copyseg[3])
    copyseg[1]=[];copyseg[2]=[];copyseg[3]=[];remake=sort(remake);redetectpairs(remake)
    flush=sort(flush)
    x=0
    #replaces the flush with the properly removed flush
    for i in copyseg[6]:
        if i[0][-1]==flush[0][-1]:break
        x+=1
    copyseg[6][x] = list(flush)
def removeflushwithstraight(removezone):
    #only usable for copyseg
    y=0;copy1=copy.deepcopy(removezone);global copyseg;flush=[];position=0
    for i in removezone:
        if i in copyseg[1]:
            copyseg[1].remove(i);copy1.remove(i);flush.append(i)
            if len(flush) == 5: break
        else:   #his else statement in the next 3 parts finds if we have a straight that uses a flush piece but the straight has a card it can use instead
                # the straight will use the other piece and the flush will take it's card it has to use
            for k in copyseg[1]:
                if i[:-1] in k:
                    for j in copyseg[5]:
                        if i[:-1] in j:
                            flush.append(i);copyseg[5][position] = k;copyseg[1].remove(k);copy1.remove(i)
                            if len(flush) == 5: break
                        position += 1
                        if len(flush) == 5: break
                    position = 0
                    if len(flush) == 5: break
                if len(flush) == 5: break
    removezone=list(copy1)
    for i in removezone:
        if i in copyseg[3]:
            copyseg[3].remove(i);copy1.remove(i);flush.append(i)
            if len(flush) == 5: break
        else:
            for k in copyseg[1]:
                if i[:-1] in k:
                    for j in copyseg[5]:
                        if i[:-1] in j:
                            flush.append(i);copyseg[5][position] = k;copyseg[1].remove(k);copy1.remove(i)
                            if len(flush) == 5: break
                        position += 1
                        if len(flush) == 5: break
                    position = 0
                    if len(flush) == 5: break
                if len(flush) == 5: break

    removezone = list(copy1)
    for i in removezone:
        if i in copyseg[2]:
            copyseg[2].remove(i);flush.append(i);y+=1
            if len(flush)==5:break
        else:
            for k in copyseg[1]:
                if i[:-1] in k:
                    for j in copyseg[5]:
                        if i[:-1] in j:
                            flush.append(i);copyseg[5][position] = k;copyseg[1].remove(k);copy1.remove(i)
                            if len(flush) == 5:break
                        position += 1
                        if len(flush) == 5: break
                    position = 0
                    if len(flush) == 5: break
                if len(flush) == 5: break
    flush=sort(flush);remake=list(copyseg[1]+copyseg[2]+copyseg[3])
    copyseg[1]=[];copyseg[2]=[];copyseg[3]=[];remake=sort(remake);redetectpairs(remake)
    #replaces the flush with the properly removed flush
    if len(flush)==5:
        copyseg[6] = list(flush)
    else:
        copyseg[6].clear()
def check():
    global finalseg; global copyseg; copysegtotal=0;finalsegtotal=0  # have to add the line for better outliers
    if len(copyseg[1])<len(finalseg[1]):finalseg=copy.deepcopy(copyseg)
    if len(copyseg[1])==len(finalseg[1]):
        for i in copyseg[1]:x=int(i[:-1]);copysegtotal=copysegtotal+x
        for i in finalseg[1]:x=int(i[:-1]);finalsegtotal=finalsegtotal+x
        if copysegtotal>finalsegtotal: finalseg=copy.deepcopy(copyseg)
def twoflushesviable():
    global segp2; global copyseg;global segp2;copyseg=copy.deepcopy(segp2)
    #this also check for 1 flush viability, still have to do stfl
    if len(copyseg[6])==3:
        remove(copyseg[6][0]);remove(copyseg[6][1]);remove(copyseg[6][2]);copyseg[5].clear();check()
    if len(copyseg[6])==2:
        #switching he flush with higher outliers in front, happens ONLY IN copyseg
        if copyseg[8][1]<copyseg[8][3]:copyseg[6].append(copyseg[6][0]);copyseg[6].pop(0);copyseg[8].append(copyseg[8][0]);copyseg[8].append(copyseg[8][1]);copyseg[8].pop(0);copyseg[8].pop(0)
        #checks if flush #2 is viable on its own
        if copyseg[8][3]>=3: backup=copy.deepcopy(copyseg);copyseg[6].pop(0);copyseg[8].pop(0);copyseg[8].pop(0); copyseg[5].clear();removeflush(copyseg[6][0]);check();copyseg=copy.deepcopy(backup)
        removeflush(copyseg[6][0]);copyseg[5].clear()
        x=0 ## change the #outliers of second flush, if it's not 3< no flush
        for i in copyseg[6][1]:
            if i in copyseg[1]: x+=1
        copyseg[8][3]=int(x)
        if x<3: return
        #checks if the two flushes together are viable
        removeflush(copyseg[6][1]);check()
    if len(copyseg[6])==1:
        copyseg[5].clear();removeflush(copyseg[6][0]);check()  ##getting fucked after this
def straightandflush():
    global segp2;global copyseg;global segp2;copyseg = copy.deepcopy(segp2);x=0;y=0;listofstraights=[];backupseg=[]
    #we have to find best individual straight, straight/flush combined
    usablecards=copy.deepcopy(copyseg[1]+copyseg[2]+copyseg[3]);usablecards=sort(usablecards)  # redetectpairs(usablecards)  this works
    #find usable straights; I have to remove all other poker hands, check then reset using 'copyseg = copy.deepcopy(segp2)'
    if len(copyseg[5])==0: return  ###needs to be change
    convertedseg=list(copyseg[5][0])
    while x!= len(convertedseg):convertedseg[x]=int(convertedseg[x][:-1]);x+=1
    x=0
    while x!=len(convertedseg):
        if len(listofstraights)>=1 and convertedseg[x]==listofstraights[-1][0]:x+=1;continue
        if convertedseg[x]+4 in convertedseg:
            slist=[convertedseg[x],convertedseg[x]+1,convertedseg[x]+2,convertedseg[x]+3,convertedseg[x]+4]
            for i in slist:
                if convertedseg.count(i)!=1:y+=1
            if y<=4:listofstraights.append(slist)
            y=0
        x+=1
    x=0;y=0
    #turn list of straights into actual cards
    while x!=len(listofstraights):
        while y!=len(listofstraights[x]):
            for i in copyseg[5][0]:
                if int(i[:-1])==listofstraights[x][y]:listofstraights[x][y]=str(i);break
            y+=1
        x+=1;y=0
    ##add straight flush here, go through flushes, see if straight flushes are viable then add them to listofstraights
    x=0 ## we hit vanilla straight, straight/flush (including second/third if we have it), 2 straights
    while x !=len(listofstraights):
        #you need 2 backup segs, the first to have all the card in to make decisions and backupseg2 it what we base decisions off of
        backupseg = copy.deepcopy(copyseg)
        remove(listofstraights[x])
        backupseg2=copy.deepcopy(copyseg)
        #checks the first removed straight
        copyseg[5]=list(listofstraights[x]);copyseg[6].clear();copyseg[7].clear();copyseg[8].clear();check();copyseg=copy.deepcopy(backupseg2)
        #checks straight+flush[0]; need to see if flush is still viable after removing straight
        if len(copyseg[6])>=1: #checks first flush
            copyseg[5]=list(listofstraights[x]);copyseg[6] = list(copyseg[6][0]);copyseg[8]=[copyseg[8][0],copyseg[8][1]];removeflushwithstraight(copyseg[6])
            if len (copyseg[6])==5:check()
            copyseg=copy.deepcopy(backupseg2)
        if len(copyseg[6])>=2: #checks second flush
            copyseg[5]=list(listofstraights[x]);copyseg[6] = list(copyseg[6][1]);copyseg[8]=[copyseg[8][2],copyseg[8][3]];removeflushwithstraight(copyseg[6])
            if len (copyseg[6])==5:
                check()
            copyseg=copy.deepcopy(backupseg2)
        if len(copyseg[6])==3: #checks third flush; didn't do a fourth flush might be needed later
            copyseg[5]=list(listofstraights[x]);copyseg[6] = list(copyseg[6][2]);copyseg[8]=[copyseg[8][4],copyseg[8][5]];removeflushwithstraight(copyseg[6])
            if len (copyseg[6])==5:
                check()
            copyseg=copy.deepcopy(backupseg2)
        #this checks 2 straights
        hand=list(copyseg[1]+copyseg[2]+copyseg[3]);hand=sort(hand);backuphand=copy.deepcopy(hand);position=0
        for i in hand:
            hand[position]=int(i[:-1]);position+=1
        position=0;rehand2=[];outliers = []
        rehand=list(hand)
        hand.sort()
        for i in hand:
            if i+1 in hand and i+2 in hand and i+3 in hand and i+4 in hand:outliers.append(i);outliers.append(i+1);outliers.append(i+2);outliers.append(i+3);outliers.append(i+4)
        #this break means second straight not viable
        #outliers is a dummy list will return if there is no hand, rehand2 is the correct hand
        if len(outliers)==0: x+=1; copyseg=copy.deepcopy(backupseg);continue
        for i in outliers:
            if i not in rehand2: rehand2.append(i)
        outliers=[]
        for i in rehand2:
            hand.remove(i)
        for i in hand:
            outliers.append(i)
        rehand3=[];used=[]
        for i in backuphand:
            if int(i[:-1]) in rehand2 and int(i[:-1]) not in used:rehand3.append(i);used.append(int(i[:-1]))
        for i in rehand3:
            if i in copyseg[1]:copyseg[1].remove(i)
            if i in copyseg[2]: copyseg[2].remove(i)
            if i in copyseg[3]: copyseg[3].remove(i)
        print(copyseg, hand)
        redetectpairs(copyseg[1]+copyseg[2]+copyseg[3])
        copyseg[5].clear();copyseg[6].clear();copyseg[8].clear();copyseg[5].append(listofstraights[x]);copyseg[5].append(rehand3)
        copyseg=copy.deepcopy(backupseg)
        x+=1
def segmenthand():
    global player2;global p2copy;global segp2;global finalseg;global copyseg
    segp2=[[],[],[],[],[],[],[],[],[]];copyseg=[];finalseg=[]
    p2copy=copy.deepcopy(list(player2))
    remove2ak();detectpairs(p2copy);detectflush(p2copy);detectstr(p2copy);twoflushesviable();straightandflush()
    segp2=list(finalseg)
    print('segment phase player2 =', segp2)
def mullselect():
    global mull; global mullnotes; global player2;x=0;y=0;final=[10,0,0];finalmull=[];global play2
    mullguide=['b','t','d','c','h','s','dstfl','cstfl','hstfl','sstfl'];play2=[]
    while len(mull) !=0:
        if final[0]>mullnotes[0]:final=[mullnotes[0],mullnotes[1],mullnotes[2]];finalmull=list(mull[0]);mull.pop(0);mullnotes.pop(0);mullnotes.pop(0);mullnotes.pop(0);continue
        if final[0]==mullnotes[0] and final[1]<mullnotes[1]:final=list([mullnotes[0],mullnotes[1],mullnotes[2]]);finalmull=mull[0];mull.pop(0);mullnotes.pop(0);mullnotes.pop(0);mullnotes.pop(0);continue
        if final[0]==mullnotes[0] and final[1]==mullnotes[1]:
            for i in mullguide:
                if final[0]==i:final=list([mullnotes[0],mullnotes[1],mullnotes[2]]);finalmull=list(mull[0]);mull.pop(0);mullnotes.pop(0);mullnotes.pop(0);mullnotes.pop(0);continue
                if mullnotes[0]==i: mull.pop(0);mullnotes.pop(0);mullnotes.pop(0);mullnotes.pop(0);continue
        mull.pop(0);mullnotes.pop(0);mullnotes.pop(0);mullnotes.pop(0)
    play2=list(finalmull)
def mulligan():
    global player2
    if main!=[0,0]:return
    if len(player2)==13:return
    n2akout.clear();hardmull.clear();mullnotes.clear();outliers.clear();quads.clear();mull.clear()
    player2 = sort(player2)
    n2aksetup();finalflush();finalstraight(); mullselect()

    ###################  AI SECTION   #######################


def coveragefinder():
    global player2;global AIinfo;player2=sort(player2);p2copy2=copy.deepcopy(player2);global gamemode
    #this functions find if you just want to win the game in singles
    rangecards = ['11d', '11c', '11h', '11s', '12d', '12c', '12h', '12s', '13d', '13c', '13h', '13s', '14d', '14c','14h', '14s']
    coverage = 0;twocount = 0;rangecap=0;AKcount=0;badcardscount=0;Acecount=0
    for i in p2copy2:
        if int(i[:-1])==2: twocount+=1
        if 2<int(i[:-1])<11: badcardscount+=1
        if int(i[:-1])>=11:rangecap=str(i);break
    twocountbackup = int(twocount)
    for i in reversed(rangecards):
        if i in p2copy2:
            coverage+=1
            if i[:-1] == '13':AKcount += 1
            if i[:-1] == '14': AKcount += 1;Acecount+=1
        else:
            if i[:-1]=='14' and twocount>0: twocount-=1
            else:
                coverage-=1
                if coverage==-5: AIinfo[4]=0;return ### if we have a huge hole in coverage we don't go on
        if i==rangecap: break
    twocount=int(twocountbackup)
    leftover2s= Acecount+twocount-4
    if leftover2s>0:badcardscount=badcardscount+ leftover2s;AIinfo[1]=True          ### if we have too many twos they are effectively worthless, the 2s is the exception
    twocount=twocount/2
    if gamemode[0] != 0: badcardscount += 1
    if '2s' in p2copy2:twocount+=.5
    if AKcount+twocount/2>badcardscount+1:AIinfo[0]=True     ##if we have enough AK2 to cover enough cards we play singles
    AIinfo[4]=int(coverage)
    print(coverage, twocount, rangecap, AKcount, badcardscount,AIinfo)
def AIflushstraight():
    global main;global gamemode; global finalseg;global AIinfo
    #functions plays straights and flushes if we have them
    # straight first
    if not AIinfo[6] and finalseg[5] and gamemode[0] == 3 or not AIinfo[6] and finalseg[5] and gamemode[0] == 0:
        if gamemode[2] < 3:
            AIinfo[6] = list(finalseg[5][0]);
            AIinfo[5] = 1
        if gamemode[2] == 3:
            for i in finalseg[5]:
                str = i[-1].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')
                print('straight strength is/gamemode[1],',str,gamemode[1])
                if gamemode[1] < float(str):
                    if round(gamemode[1]) != 2 and round(float(str)) != 14: AIinfo[6] = list(i);AIinfo[5] = 1
                else:
                    if round(float(str)) == 2 and round(gamemode[1]) == 14: AIinfo[6] = list(i);AIinfo[5] = 1

    if len(AIinfo[6])!=5 and AIinfo[6]:AIinfo[6]=finalseg[5]
    # flush
    if not AIinfo[6] and finalseg[6] and gamemode[0] == 3 or not AIinfo[6] and finalseg[6] and gamemode[0] == 0:
        if gamemode[2] < 4:
            AIinfo[6] = list(finalseg[6]);
            AIinfo[5] = 2
        if gamemode[2] == 4:
            for i in finalseg[6]:
                str = i[-1].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')
                if gamemode[1] < float(str):
                    if round(gamemode[1]) != 2 and round(float(str)) != 14: AIinfo[6] = list(i);AIinfo[5] = 2
                else:
                    if round(float(str)) == 2 and round(gamemode[1]) == 14: AIinfo[6] = list(i);AIinfo[5] = 2
def AIFullhHouseQuadsTwoPair():
    global finalseg;global AIinfo;counter=0;global gamemode;counter=0;valueseg=[];global player2;global player1
    TAK=[0,0,0];pairstotest=[];dummy=[]
    for i in finalseg:
        if counter==5:break
        x = finalseg[counter]
        x = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in x]
        x = [float(a) for a in x]
        if len(x)>1:
            if x[1]<1:x[0]=x[0]+x[1];x.pop(-1)
        valueseg.append(x)
        counter += 1
    doiwinseg =copy.deepcopy(valueseg)
    ##doiwinseg put everything into outliers/pairs/trips
    for i in doiwinseg[0]:
        if round(i)==2:TAK[0]+=1
        if round(i) == 13: TAK[1] += 1
        if round(i) == 14: TAK[2] += 1
    #assembles pairs to test to see if we can play them and win, and also moves them into doiwinseg
    for i in TAK:
        if i==1:doiwinseg[1].append(doiwinseg[0][0]);doiwinseg[0].pop(0)
        if i == 2: pairstotest.append([doiwinseg[0][0],doiwinseg[0][1]]);doiwinseg[2].append(doiwinseg[0][0]);doiwinseg[0].pop(0);doiwinseg[2].append(doiwinseg[0][0]);doiwinseg[0].pop(0)
        if i==3: pairstotest.append([doiwinseg[0][0],doiwinseg[0][1]]);doiwinseg[3].append(doiwinseg[0][0]);doiwinseg[0].pop(0);doiwinseg[3].append(doiwinseg[0][0]);doiwinseg[0].pop(0);doiwinseg[3].append(doiwinseg[0][0]);doiwinseg[0].pop(0)
    for i in doiwinseg[4]:
        dummy.append(round(i));doiwinseg[4].pop(0);doiwinseg[4].pop(0);doiwinseg[4].pop(0)
    doiwinseg[4]=list(dummy)
    print('1466doiwinseg/TAK/valueseg is',doiwinseg,TAK,valueseg)
    #odd straights and flushes
    if len(player2)==5 and len(doiwinseg[1])==5: #not calculating gamemode only do this if we win
        if gamemode[0]==0 or gamemode[0]==3:
            weirdstraight=copy.deepcopy(doiwinseg[1])
            weirdstraight.sort()
            weirdstraight=[round(i) for i in weirdstraight]
            print('weirdstraight is',weirdstraight)
            if weirdstraight==[2,3,4,13,14] or weirdstraight==[2,3,4,5,14] or weirdstraight==[2,3,12,13,14] or weirdstraight==[2,11,12,13,14] or weirdstraight==[10,11,12,13,14] or weirdstraight==[9,10,11,12,13]:
                AIinfo[6] = list(doiwinseg[1]);AIinfo[5] = 1
            if doiwinseg[1][0]*10%10==doiwinseg[1][1]*10%10==doiwinseg[1][2]*10%10==doiwinseg[1][3]*10%10==doiwinseg[1][4]*10%10:
                AIinfo[6] = list(doiwinseg[1]);AIinfo[5] = 2
            AIinfo[6]=sort(AIinfo[6])
            if AIinfo[6]:AIinfo[6] = [str(a) for a in AIinfo[6]];AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in AIinfo[6]]
            AIinfo[6]=sort(AIinfo[6])
    counter=0
    #trips and extra trips
    if gamemode[0]==3 and gamemode[2]<=2 or gamemode[0]==0:
        if not AIinfo[6]:
            if len(finalseg[2]) <= 2 and len(finalseg[3]) >= 6 or len(finalseg[3])==9 or len(finalseg[3]) >= 3 and len(finalseg[2])==0:
                for i in valueseg[3]:
                     if i>gamemode[1] or gamemode[2]<2:
                        AIinfo[6] = list(finalseg[3][0+counter:3+counter]);AIinfo[5]=3;break
                     counter+=1
                counter=0
            #win condition
            if len(doiwinseg[3]) == 3 and len(player2) == 3: AIinfo[6] = list(finalseg[0]);AIinfo[5] = 3
            ###have to add a rule for trip 2's
    #twopair before boat gamemode[2]=1
    if gamemode[0] == 3 and gamemode[2] <= 1 or gamemode[0] == 0:
        if not AIinfo[6]:
            if len(finalseg[2]) >= 6 and len(finalseg[3]) >= 3:
                for i in valueseg[2]:
                    if i > gamemode[1] or gamemode[2]<1:
                        AIinfo[6]=list(finalseg[2][0:2]+finalseg[2][0+counter:2+counter]);AIinfo[5]=4
                        if AIinfo[6][0]==AIinfo[6][2]:
                            AIinfo[6]=AIinfo[6]=list(finalseg[2][0:4]);AIinfo[5]=4
                        break
                    counter += 1
                counter = 0
            if len(player2)==4 and len(doiwinseg[2])==4:
                AIinfo[6]=list(player2)
    #exactly two boats gamemode[2]=5
    if gamemode[0] == 3 and gamemode[2] <= 5 or gamemode[0] == 0:
        if not AIinfo[6]:
            if len(finalseg[2]) >= 2 and len(finalseg[3]) >= 3:
                for i in valueseg[3]:
                    if i > gamemode[1] or gamemode[2]<5:
                        AIinfo[6]=list(finalseg[2][0:2]+finalseg[3][0+counter:3+counter]);AIinfo[5]=5;break
                    counter += 1
                counter = 0
            ## breaks a trip to play a boat
            if not AIinfo[6] and not finalseg[2] and len(finalseg[3])>=6:
                AIinfo[6] = list(finalseg[3][0:5]);AIinfo[5]=5;print('no pair 2 trips boat works ok')
            #win condition set
            if not AIinfo[6] and len(player2)==5 and len(doiwinseg[2])==2 and len(doiwinseg[3])==3:
                AIinfo[6].append(list(player2));AIinfo[5]=5
    #quads
    if gamemode[0] == 3 and gamemode[2] <= 6 or gamemode[0] == 0:

        if len(player2)<=11 or len(player1)<=7: ##not sure about this number but I don't want to be jamming quads
            if not AIinfo[6]:
                if len(finalseg[4]) >=4:
                    for i in valueseg[4]:
                        if i > gamemode[1] or gamemode[2]<6:
                            kicker=0
                            if len(finalseg[1])!=0: kicker=str(finalseg[1][0])
                            AIinfo[6]=list(finalseg[4][0:4])
                            if kicker:AIinfo[6].append(kicker);AIinfo[5]=6
                            break
                        counter += 1
                    counter = 0
                ## chooses a kicker, taking doiwin[0] isn't 100% correct
                if len(AIinfo[6])==4:
                    if doiwinseg[1]:
                        print('kicker conversion bug is',AIinfo[6])
                        kicker=[doiwinseg[1][0]]
                        kicker = [str(a) for a in kicker];kicker= [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in kicker]
                        kicker.append(AIinfo[6])
                if len(AIinfo[6])==4 and len(player2)==5:AIinfo[6]=list(player2)
    #straightflush
    if gamemode[0] == 3 and gamemode[2] <= 7 or gamemode[0] == 0:
        if not AIinfo[6]:
            if len(finalseg[7]) >=5:
                for i in valueseg[7]:
                    if i > gamemode[1] or gamemode[2]<7:
                        AIinfo[6]=list(finalseg[4][0:5]);AIinfo[5]=9;break
                    counter += 1
            counter = 0
    #normal pairs
    if gamemode[0] == 2 or gamemode[0] == 0:
        if not AIinfo[6] or not AIinfo[6] and not AIinfo[0] and gamemode[0]==0:
            if round(gamemode[1])==14:
                twocount=0;Acount=0
                for i in valueseg[0]:
                    if round(i)==2: twocount+=1
                    if round(i)==14: Acount+=1
                if twocount>=2 and Acount<2: AIinfo[6]=[finalseg[0][0],finalseg[0][1]];AIinfo[5]=7
                if len(player1)<=3 and Acount>=2 and 14.4 in valueseg[0]:AIinfo[6]=[finalseg[0][-2],finalseg[0][-1]];AIinfo[5]=7
            if len(finalseg[2]) >= 2 and not AIinfo[6]:
                for i in valueseg[2]:
                    if i > gamemode[1]:
                        if counter%2==0:
                            AIinfo[6]=list(finalseg[2][counter:2+counter]);AIinfo[5]=7;break
                        else:
                            AIinfo[6] = list(finalseg[2][counter-1:+counter+1]);AIinfo[5]=7;break
                    counter += 1
                counter = 0
            print('1595 2XA pairs doiwinseg is',doiwinseg)
            if TAK[0]==2 and TAK[2]==2 and len(doiwinseg[2])==6 and len(player2)==6:
                AIinfo[6].clear();AIinfo[6].append(doiwinseg[2][2]);AIinfo[6].append(doiwinseg[2][3]);print('2XA pair change needs test')
            #covers all playable pairs including 2AK
            if not AIinfo[6] and len(finalseg[2])!=0:AIinfo[5]=7; doiwin(doiwinseg)
            if AIinfo[3] and not AIinfo[6]:
                thepair=0
                for i in doiwinseg[2]:
                    if i>gamemode[1]:
                        thepair=round(i);break
                for i in doiwinseg[2]:
                    #if thepair>=13:print('dont want to play AK pair idk if correct');break
                    if round(i) == thepair: AIinfo[6].append(i)
                if doiwinseg[3]:
                    thepair = 0
                    for i in doiwinseg[3]:
                        # if thepair>=13:print('dont want to play AK pair idk if correct');break
                        if round(i)>gamemode[1]:
                            AIinfo[6].append(i)
                            if len(AIinfo[6])==2:print('test we broke trips');break
                print('untested opponent less then 2 cards(AIinfo[3]',AIinfo[3],AIinfo[6])
            if AIinfo[6]:
                AIinfo[6] = [str(a) for a in AIinfo[6]];AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in AIinfo[6]]
            else: AIinfo[5]=0
            if gamemode[0]==0 and len(player2)==2 and doiwinseg[2]:
                AIinfo[6]=list(player2)
    #singles
    if gamemode[0]==1 or gamemode[0]==0:
        #standard singles play section
        if not AIinfo[6]:
            if len(player1)>=len(player2) or gamemode[0]==0:
                for i in valueseg[1]:
                    if i > gamemode[1]:
                        AIinfo[6].append(finalseg[1][counter]);AIinfo[5]=8;break
                    counter += 1
            else:
                counter=len(valueseg[1])
                for i in reversed (valueseg[1]):
                    counter -= 1
                    if i > gamemode[1]:
                        AIinfo[6].append(finalseg[1][counter]);AIinfo[5]=8;break
                    counter -= 1
            counter=0
            pairstrips=list(valueseg[2])+list(valueseg[3]);pairstrips.sort()
            ##if we are just jamming singles we don't care about our pairs trips and play singles for gamemode[0]=0
            if gamemode[0]==0 and pairstrips and not AIinfo[6]:
                AIinfo[6].append(pairstrips[0]);AIinfo[5]=8
            if gamemode[0]==1 and pairstrips and not AIinfo[6]:
                if gamemode[1]<pairstrips[-1]:AIinfo[6].append(pairstrips[-1]);AIinfo[5]=8
            if round(gamemode[1])==14:
                #we're in trouble and need to play hard to not lose
                if AIinfo[3]==True or len(player2)>=len(player1):
                    for i in valueseg[0]:
                        if i > gamemode[1]:AIinfo[6].append(i);AIinfo[5]=8;break
                    if not AIinfo[6]:
                        for i in reversed(valueseg[0]):
                            if round(i)==2:AIinfo[6].append(i);AIinfo[5]=8;break
                ## here we're not in trouble and can make the value play
                else:
                    for i in valueseg[0]:
                        if round(i)==2:AIinfo[6].append(i);AIinfo[5]=8;break
                    if not AIinfo[6]:
                        for i in valueseg[0]:
                            if i > gamemode[1]:AIinfo[6].append(i);AIinfo[5]=8;break
            ## uses 2's in singles if 2's are useless
            if TAK[1]==0 and len(pairstrips)==0 and valueseg[1]==1 and TAK[0] !=0 and TAK[2]!=0 and AIinfo[6]:
                if TAK[0]>=2 and TAK[2] >=2:
                    AIinfo[6].clear();AIinfo[6].append(valueseg[0])
            #deletes play if we can't make a standard play so that we can go harder to not lose
            acestwos=0;playablesingles=list(valueseg[1])+list(valueseg[2])+list(valueseg[3]);playablesingles.sort()
            if TAK[0]+TAK[2]>4:acestwos=4
            else: acestwos=int(TAK[0])+int(TAK[2])
            if playablesingles:
                if acestwos+TAK[1]<len(player1) and playablesingles[-1] > gamemode[1] and gamemode[0] !=0:AIinfo[6].clear();AIinfo[6].append(playablesingles[-1]);print('switch gear1661 is',AIinfo[6])
            if AIinfo[3] and gamemode[0]!=0:
                if TAK[2]:
                    if round(gamemode[1])!=2:
                        AIinfo[6].clear();print('1clearing, they have less then 3 cards and we are playing AK')
                if TAK[1]:
                    AIinfo[6].clear();print('2clearing, they have less then 3 cards and we are playing AK')
            #make a function to get rid of excess 2's maybe at 5 cards or len(valueseg[0])==4/[1] ==1
            if len(player2) == 3 and '2s' in player2 and gamemode[0]==0:
                for i in player2:
                    if i != '2s': AIinfo[6].clear();AIinfo[6].append(i);break
            if len(player2) == 3 and 'As' in player2 and gamemode[0]==0:
                AIinfo[6].clear();AIinfo[6].append(player2[0])
            #converter
            if not type(AIinfo[6])== str and AIinfo[6]:
                print('1627AIinfo[6] convert bug',AIinfo[6])
                AIinfo[6][0] = str(AIinfo[6][0])
                AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in AIinfo[6]]
            print('1628singles final seg/TAK is',finalseg,TAK)
            if not AIinfo[6] and finalseg[0]:
                #adds quad 2ak into the cards playable in singles
                if valueseg[4]:
                    for i in valueseg[4]: ###have to add quad 2ak here just don't know how I should do it
                        if round(i)==14 or round(i)==13 or round(i)==2:
                            valueseg[0].append(i)
                    print('new post quads valueseg is',valueseg)
                # this is if no outliers and all we have is 2ak and we lead
                if gamemode[0]==0:
                    if TAK[0]>=TAK[1] and TAK[0]>=TAK[2]:
                        AIinfo[6].append(finalseg[0][0]);AIinfo[5]=8
                    if TAK[1]>TAK[0] and TAK[1]>=TAK[2] and not AIinfo[6]:
                        for i in finalseg[0]:
                            if i[:-1]=='13':AIinfo[6].append(finalseg[0][counter]);AIinfo[5]=8;break
                            counter+=1
                    if TAK[2]>TAK[0] and TAK[2]>TAK[1] and not AIinfo[6]:
                        for i in finalseg[0]:
                            if i[:-1]=='14':AIinfo[6].append(finalseg[0][counter]);AIinfo[5]=8;break
                            counter+=1
                    print('bug here is AIinfo[6] is []',AIinfo[6])
                #this is no outliers and we don't lead
                if gamemode[0]==1:
                    if round(gamemode[1])==14 and TAK[0]>=1:
                        if TAK[0]>=2 and len (player1)<=3:
                            AIinfo[6].append(finalseg[0][TAK[0]-1]);AIinfo[5] = 8
                        else:AIinfo[6].append(finalseg[0][0]);AIinfo[5]=8
                    if not AIinfo[6]:
                        print('we should play 2ak here')
                        Ks=False
                        if len (player1) <=2 and len(player2)>len(player1):
                            print('scared mode')
                            for i in reversed(valueseg[0]):
                                if gamemode[1] < i:
                                    if i==13.4: Ks=True;print('skip Ks');continue
                                    if round(gamemode[1])==2 and round(i)==14:
                                        continue
                                    else:
                                        AIinfo[6].append(i);AIinfo[5]=8;break
                        else:
                            print('value mode')
                            for i in valueseg[0]:
                                if gamemode[1] < i:
                                    if i==13.4: Ks=True;print('skip Ks');continue
                                    if round(gamemode[1])==2 and round(i)==14:
                                        break
                                    else:
                                        AIinfo[6].append(i);AIinfo[5]=8;break
                        #play Ks over As
                        if Ks and AIinfo[6]:
                            if AIinfo[6]==14.4:
                                if gamemode[1]<13.4:AIinfo[6]=[13.4]
                        #play Ks if we have nothing
                        if Ks and not AIinfo[6] and gamemode[1]<13.4:AIinfo[6]=[13.4]
                        #play Ks when they have 2 or less cards
                        if Ks and AIinfo[6] and len(player1)<=2:
                            if AIinfo[6][0]!=14.4: AIinfo[6]=[13.4]
                        ##add 3 card win cons here
                        #adjust if they have 3 or less, and adjust to be able play A on A
                        AIinfo[6] = [str(a) for a in AIinfo[6]];AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's')for word in AIinfo[6]]
                        print('AIinfo[6] hopefully 2ak is',AIinfo[6])
    print('actual AIinfo[6]/[5]=',AIinfo[6],AIinfo[5])
    if AIinfo[6]:
        if type(AIinfo[6][0])==list:
            AIinfo[6]=AIinfo[6][0]
    AIinfo[6]=sort(AIinfo[6])
def doiwin(doiwinseg):
    global AIinfo
    #you get basically 4 free poker hands if they have less than 4 cards
    counter=0;pairstotest=[];pair=[]
    print('doiwin',doiwinseg)
    strongpokerhand=False
    for i in doiwinseg[3]:
        if i>11 and doiwinseg[2] or i>11 and len(doiwinseg[3])>3:AIinfo[7]=True
    for i in doiwinseg[2]:
        if 13<i<14.5:
            pair.append(i)
            if len(pair)==2:pairstotest.append(pair);pair=[]
    #if we have a trips we aren't afraid of having an extra pair
    if AIinfo[2]==True or strongpokerhand==True:
        for i in pairstotest:
            backupcopy = copy.deepcopy(doiwinseg)
            for k in pairstotest[counter]:
                if k in doiwinseg[2]:doiwinseg[2].remove(k)
                if k in doiwinseg[1]:doiwinseg[1].remove(k)
                if k in doiwinseg[3]:doiwinseg[3].remove(k)
            if doiwinseg[3]:doiwinseg[2].clear()
            therest=doiwinseg[1]+doiwinseg[2]
            if 14.4 in therest and len(therest)<=4+len(doiwinseg[4]):
                if 14.3 or 14.2 in therest:
                    if 2.4 in therest:AIinfo[5]=9;AIinfo[6]=pairstotest[counter];return
                    badtwos=0
                    for j in therest:
                        if j==2.1 or j==2.2 or j==2.3:badtwos+=1
                    badtwos=badtwos-len(doiwinseg[4])
                    if badtwos<=1: AIinfo[5]=9;AIinfo[6]=pairstotest[counter];return
            if 14.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                badtwos=0
                for j in therest:
                    if j == 2.1 or j == 2.2 or j == 2.3: badtwos += 1
                badtwos = badtwos - len(doiwinseg[4])
                if 14.1 or 14.2 or 14.3 in therest:badtwos+=1
                if badtwos <= 1: AIinfo[5]=9;AIinfo[6]=pairstotest[counter];return
            if 13.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                for i in therest:
                    if round(i)==2: AIinfo[5]=9;AIinfo[6]=pairstotest[counter];return
            if 2.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                for i in therest:
                    if round(i)==14: AIinfo[5]=9;AIinfo[6]=pairstotest[counter];return
            if AIinfo[4] >=2: AIinfo[5]=9;AIinfo[6]=pairstotest[counter];return
            counter+=1
            doiwinseg = copy.deepcopy(backupcopy)

def AIdraw():
    global AIinfo;global finalseg;global p2redraw;global deck;plainnumseg=[[],[],[]];global pile;global player2;global log;global main;global gamemode;global fplay
    global showthis;global showlast;global play;global p2redraw
    draws=[];newgamemode=[]
    #for pile maybe above an 8 outlier draw it
    #pile draw if they have =<4 cards and you have 2 outliers pile draw one of them if possible
    #draw pair less then 6 cards keep it
    #less then 5 cards draw 1
    #drawing a 2 good if #A+#2 < 3
    if AIinfo[6]:
        fplay=list(AIinfo[6])
        log.append(list(AIinfo[6]));log.append(list(main));log.append(list(gamemode));log.append(7)
        newgamemode.append(AIinfo[6][-1])
        newgamemode = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in newgamemode]
        newgamemode= [float(a) for a in newgamemode]
        if len(AIinfo[6])==1:gamemode[0]=1
        if len(AIinfo[6]) == 2: gamemode[0] = 2
        if len(AIinfo[6]) >=3:
            gamemode[0] = 3
            if AIinfo[5]==9: gamemode[2]=7
            if AIinfo[5] == 6: gamemode[2] = 6
            if AIinfo[5] == 5: gamemode[2] = 5
            if AIinfo[5] == 4: gamemode[2] = 1
            if AIinfo[5] == 3: gamemode[2] = 2
            if AIinfo[5] == 1: gamemode[2] = 3
            if AIinfo[5] == 2: gamemode[2] = 4
        main=[1,2]
        if AIinfo[5]==5: #should do 2 high flush/straight eventually
            gamemode[1]=float(AIinfo[6][2][:-1])
        elif AIinfo[5]==6:gamemode[1]=float(AIinfo[6][3][:-1])
        else:
            gamemode[1]=float(newgamemode[-1])
        if len(AIinfo[6])!=0:
            for i in AIinfo[6]:
                player2.remove(i)
        if gamemode[2]==4:
            if int(AIinfo[6][0][:-1])+1==int(AIinfo[6][1][:-1]) and int(AIinfo[6][1][:-1])+1==int(AIinfo[6][2][:-1]) and int(AIinfo[6][2][:-1])+1==int(AIinfo[6][3][:-1]) and int(AIinfo[6][3][:-1])+1==int(AIinfo[6][4][:-1]):
                print('hotfix actually its straight flush');gamemode[2]=7
        AIinfo[5] = 0
        return
    showlast=[];showlast=list(showthis);showthis=[];play.clear();play2.clear();fplay.clear();AIinfo[5]=0
    for i in finalseg[1]:
        plainnumseg[0].append(i[:-1])
    plainnumseg[0] = [int(a) for a in plainnumseg[0]]
    for i in finalseg[2]:
        plainnumseg[1].append(i[:-1])
    plainnumseg[1] = [int(a) for a in plainnumseg[1]]
    for i in finalseg[3]:
        plainnumseg[2].append(i[:-1])
    plainnumseg[2] = [int(a) for a in plainnumseg[2]]
    for i in pile:
        pass #do this later
    draw=[]
    if int(deck[0][:-1]) in plainnumseg[0] or int(deck[0][:-1]) in plainnumseg[2] or deck[0][:-1]=='13' or deck[0][:-1]=='14'or len(player2)<=4: #AI 7 play 8 AI draw 9 AI pile
        print('draw1 done')
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0]
        return
    if int(deck[0][:-1]) in plainnumseg[0] or int(deck[0][:-1]) in plainnumseg[2] or deck[1][:-1] == '13' or deck[1][:-1] == '14' or deck[1][:-1]==deck[0][:-1]:
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);
        log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0]
        print('draw2 done');return
    if p2redraw:
        pile.append(deck[0]);draw.append(deck[0]);deck.pop(0);pile.append(deck[0]);draw.append(deck[0]);deck.pop(0)
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8)
        main=[1,1];gamemode=[0,0,0];p2redraw=False
        print('redraw');return
    if len(player2)>=4:
        print('draw1#2 done')
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0];return
    else:
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);
        log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0]
        print('draw2#2 done');return
def AImove():
    global AIinfo;global main;global gamemode;global player2
    if main[0] == 1: return
    if len(player1)<=2:AIinfo[3]=True
    else: AIinfo[3]=False
    if len(player1)<=4:AIinfo[2]=True
    if len(player1)>=9 and AIinfo[2]==True:AIinfo[2]=False
    if finalseg[4]:AIinfo[7]=True
    if finalseg[7]:AIinfo[7]=True
    coveragefinder();AIflushstraight();AIFullhHouseQuadsTwoPair();AIdraw();AIinfo[6].clear();player2=sort(player2);play2.clear();redrawgamewindow()

def keybinds():
    global play;global play2;global lastmouse1
    pass

startgame();redrawgamewindow();pygame.display.flip();running= True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False;pygame.quit();exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons()
            #print(mouse[0], mouse[1])  # shows mouse position
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                mouse = [120, 323];
                if main == [-3, 0]: mouse = [450, 90]
                if main == [-2, 0]: mouse = [450, 520]
                buttons()
            if event.key == pygame.K_q:
                if main[0] == 1: mouse = [55, 645]
                if main[0] == 2: mouse = [55, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_w:
                if main[0] == 1: mouse = [130, 645]
                if main[0] == 2: mouse = [130, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_e:
                if main[0] == 1: mouse = [205, 645]
                if main[0] == 2: mouse = [205, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_r:
                if main[0] == 1: mouse = [280, 645]
                if main[0] == 2: mouse = [280, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_t:
                if main[0] == 1: mouse = [355, 645]
                if main[0] == 2: mouse = [355, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_y:
                if main[0] == 1: mouse = [430, 645]
                if main[0] == 2: mouse = [430, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_u:
                if main[0] == 1: mouse = [505, 645]
                if main[0] == 2: mouse = [505, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_i:
                if main[0] == 1: mouse = [580, 645]
                if main[0] == 2: mouse = [580, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_o:
                if main[0] == 1: mouse = [655, 645]
                if main[0] == 2: mouse = [655, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_p:
                if main[0] == 1: mouse = [730, 645]
                if main[0] == 2: mouse = [730, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_LEFTBRACKET:
                if main[0] == 1: mouse = [805, 645]
                if main[0] == 2: mouse = [805, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_RIGHTBRACKET:
                if main[0] == 1: mouse = [880, 645]
                if main[0] == 2: mouse = [880, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_BACKSLASH:
                if main[0] == 1: mouse = [955, 645]
                if main[0] == 2: mouse = [955, 188]
                mouse = list(mouse)
                lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_1:
                if main[0] == 1: mouse = [55, 490]
                if main[0] == 2: mouse = [55, 60]
                if main == [-3, -3]: mouse = [20, 30]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_2:
                if main[0] == 1: mouse = [135, 490]
                if main[0] == 2: mouse = [135, 60]
                if main == [-3, -3]: mouse = [20, 90]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_3:
                if main[0] == 1: mouse = [205, 490]
                if main[0] == 2: mouse = [205, 60]
                if main == [-3, -3]: mouse = [20, 150]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_4:
                if main[0] == 1: mouse = [280, 490]
                if main[0] == 2: mouse = [280, 60]
                if main == [-3, -3]: mouse = [20, 210]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_5:
                if main[0] == 1: mouse = [355, 490]
                if main[0] == 2: mouse = [355, 60]
                if main == [-3, -3]: mouse = [20, 270]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_6:
                if main[0] == 1: mouse = [430, 490]
                if main[0] == 2: mouse = [430, 60]
                if main == [-3, -3]: mouse = [20, 330]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_7:
                if main[0] == 1: mouse = [505, 490]
                if main[0] == 2: mouse = [505, 60]
                if main == [-3, -3]: mouse = [20, 390]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_8:
                if main[0] == 1: mouse = [580, 490]
                if main[0] == 2: mouse = [580, 60]
                if main == [-3, -3]: mouse = [20, 450]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_9:
                if main[0] == 1: mouse = [655, 490]
                if main[0] == 2: mouse = [655, 60]
                if main == [-3, -3]: mouse = [20, 510]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_0:
                if main[0] == 1: mouse = [730, 490]
                if main[0] == 2: mouse = [730, 60]
                if main == [-3, -3]: mouse = [20, 570]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_MINUS:
                if main[0] == 1: mouse = [805, 490]
                if main[0] == 2: mouse = [805, 60]
                if main == [-3, -3]: mouse = [20, 630]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_EQUALS:
                if main[0] == 1: mouse = [880, 490]
                if main[0] == 2: mouse = [880, 60]
                if main == [-3, -3]: mouse = [20, 690]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_BACKSPACE:
                if main[0] == 1: mouse = [955, 490]
                if main[0] == 2: mouse = [955, 60]
                mouse = list(mouse)
                if main != [-3, -3]: lastmouse1 = list(mouse)
                buttons()
            if event.key == pygame.K_SPACE:
                mouse = [650, 350];
                buttons()
            if event.key == pygame.K_RALT:
                mouse = [650, 300];
                buttons()
            if event.key == pygame.K_TAB:
                mouse = [20, 350];
                buttons()
            if event.key == pygame.K_LEFT:
                if main[0] == 1:
                    backupplay = len(play);
                    backup = list(lastmouse1);
                    lastmouse1[0] = lastmouse1[0] - 75;
                    mouse = list(lastmouse1);
                    buttons();
                    if backupplay > len(play): buttons()
                    backupplay = len(play);
                    mouse = list(backup);
                    buttons()
                    if backupplay < len(play): buttons()
                if main[0] == 2:
                    backupplay = len(play2);
                    backup = list(lastmouse1);
                    lastmouse1[0] = lastmouse1[0] - 75;
                    mouse = list(lastmouse1);
                    buttons();
                    if backupplay > len(play2): buttons()
                    backupplay = len(play2);
                    mouse = list(backup);
                    buttons()
                    if backupplay < len(play2): buttons()
            if event.key == pygame.K_RIGHT:
                if main[0] == 1:
                    backupplay = len(play);
                    backup = list(lastmouse1);
                    lastmouse1[0] = lastmouse1[0] + 75;
                    mouse = list(lastmouse1);
                    buttons();
                    if backupplay > len(play): buttons()
                    backupplay = len(play);
                    mouse = list(backup);
                    buttons()
                    if backupplay < len(play): buttons()
                if main[0] == 2:
                    backupplay = len(play2);
                    backup = list(lastmouse1);
                    lastmouse1[0] = lastmouse1[0] + 75;
                    mouse = list(lastmouse1);
                    buttons();
                    if backupplay > len(play2): buttons()
                    backupplay = len(play2);
                    mouse = list(backup);
                    buttons()
                    if backupplay < len(play2): buttons()
            if event.key == pygame.K_F1:
                mouse = [751, 280];
                buttons()
            if event.key == pygame.K_F2:
                mouse = [788, 280];
                buttons()
            if event.key == pygame.K_F3:
                mouse = [825, 280];
                buttons()
            if event.key == pygame.K_F4:
                mouse = [865, 280];
                buttons()
            if event.key == pygame.K_F5:
                mouse = [910, 280];
                buttons()
            if event.key == pygame.K_F6:
                mouse = [950, 280];
                buttons()
            if event.key == pygame.K_F7:
                mouse = [751, 310];
                buttons()
            if event.key == pygame.K_F8:
                mouse = [788, 310];
                buttons()
            if event.key == pygame.K_F9:
                mouse = [825, 310];
                buttons()
            if event.key == pygame.K_F10:
                mouse = [865, 310];
                buttons()
            if event.key == pygame.K_F11:
                mouse = [910, 310];
                buttons()
            if event.key == pygame.K_F12:
                mouse = [950, 310];
                buttons()
            if event.key == pygame.K_UP:
                if main[0] == 1:
                    backupplay = len(play);
                    mouse = list(lastmouse1);
                    buttons()
                    if backupplay > len(play): buttons()
                if main[0] == 2:
                    backupplay = len(play2);
                    mouse = list(lastmouse1);
                    buttons()
                    if backupplay > len(play2): buttons()
            if event.key == pygame.K_DOWN:
                if main[0] == 1:
                    backupplay = len(play);
                    mouse = list(lastmouse1);
                    buttons()
                    if backupplay < len(play): buttons()
                if main[0] == 2:
                    backupplay = len(play2);
                    mouse = list(lastmouse1);
                    buttons()
                    if backupplay < len(play2): buttons()

        mouse = pygame.mouse.get_pos()