import basic as basic;import display as display;import segment as segment;import AI as AIm

def playfct(mouse,screen,game):
    #play is the variable where the players hand input if placed, all cards in play are also in the players hands. Checkplay determines if the play is legal
    if game.main ==[1,0] or game.main ==[1,1] or game.main==[1,2]:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            play0=list(game.play)
            play0,game=checkplay(play0,game,screen)
    elif game.main==[2,0] or game.main ==[2,1] or game.main==[2,2]:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            play0=list(game.play2)
            play0,game=checkplay(play0,game,screen)
            if game.AI==True and game.main==[2,0] or game.AI==True and game.main==[2,1] or game.AI==True and game.main==[2,2]:  ##change later
                game=segment.segmenthand(game)
                game=AIm.AImove(screen,game)
                game.AIinfo[6].clear()
    return game

def checkplay(play0,game,screen):
    #takes you to the correct check function to see if your play is legal
    #added this function long after global play if hand 1 selected cards, play2 is hand 2 selected cards
    if game.main[0]==0:
        return play0,game
    play0=basic.sort(play0)

    if len(play0)==1:
        if game.gamemode[0]==1 or game.gamemode[0]==0:
            play0,game=len1check(play0,game,screen)

    if len(play0)==2:
        if game.gamemode[0]==2 or game.gamemode[0]==0:
            play0,game=len2check(play0,game,screen)

    if game.gamemode[0]==3 or game.gamemode[0]==0:
        if len(play0)==3:
            play0,game=len3check(play0,game,screen)

        if len(play0)==4:
            play0,game=len4check(play0,game,screen)

        if len(play0)==5:
            play0,game=len5check(play0,game,screen)

    #this feature selects your whole hand if you click on the play button, useful for if your last cards are a poker hand
    if game.main[0]==1:
        if play0==[]:
            game.play=list(game.player1)
        else:
            game.play.clear()
    elif game.main[0] == 2:
        if play0==[]:
            game.play2=list(game.player2)
        else:
            game.play2.clear()
    game=display.redrawgamewindow(screen,game)
    return play0,game

def len1check(play0,game,screen):
    #checks 1 card hands
    backup = list(play0)
    #card conversion to number
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in play0]
    #check if my card is higher/legal to play on your card
    if game.gamemode[1] < float(play0[-1]):
        play0[-1]=float(play0[-1])
        if round(game.gamemode[1]) == 2 and round(play0[-1]) == 14:
            return play0,game
        #sets gamemode to singles, gamemode[0]=1
        if game.gamemode[0]==0:
            game.gamemode[0]=1
        game.gamemode[1] = float(play0[-1])
        game=fplayadd(play0,backup,game)
        game = cleanup(game)
        game=display.redrawgamewindow(screen,game)
    else:
        play0[-1]=float(play0[-1])
        #check if it's a 2 that is played on an Ace which is legal
        if int(round(game.gamemode[1]))==14 and round(play0[-1])==2:
                game.gamemode[1] = float(play0[-1])
                game=fplayadd(play0,backup,game)
                game=cleanup(game)
                game=display.redrawgamewindow(screen,game)
    return play0,game

def len2check(play0,game,screen):
    #checks 2 card hands
    backup = list(play0)
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play0]
    #card conversion to number, checks to see if we have a legal pair
    if round(float(play0[0])) == round(float(play0[1])) and float(play0[1])> float(game.gamemode[1]):
        play0[-1] = float(play0[-1])
        #can't play Aces on 2's
        if round(game.gamemode[1]) == 2 and round(play0[-1]) == 14:
            return play0,game
        #sets gamemode to pairs, gamemode[0]=2
        if  game.gamemode[0]==0:
            game.gamemode[0]=2
        game.gamemode[1] = float(play0[-1])
        game=fplayadd(play0,backup,game)
        game = cleanup(game)
        game=display.redrawgamewindow(screen,game)
    else:
        play0[-1] = float(play0[-1])
        #2's playable on Aces
        if int(round(game.gamemode[1])) == 14 and round(play0[-1]) == 2:
            game.gamemode[1] = float(play0[-1])
            game=fplayadd(play0,backup,game)
            game=cleanup(game)
            game=display.redrawgamewindow(screen,game)
    return play0,game

def len3check(play0,game,screen):
    #checks 3 card hands
    backup = list(play0)
    # card conversion to number
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play0]
    #checks for three of a kind
    if round(float(play0[0])) == round(float(play0[1]))== round(float(play0[2])) and game.gamemode[2]<=2:
        if float(play0[1]) > float(game.gamemode[1]) and game.gamemode[2]<=2 or game.gamemode[2]<2:
            play0[-1] = float(play0[-1])
            #no Aces on 2's
            ##  this line gets around a bug that disallows us to declare as int and round 9/1
            x=float(game.gamemode[1])
            x=round(x)
            y=float(play0[1])
            y=round(y)
            if x==2 and y==14:
                return play0,game
            #sets gamemode to poker, gamemode[0]=3
            if game.gamemode[0]==0:
                game.gamemode[0]=3
            game.gamemode[1] = float(play0[-1])
            game.gamemode[2]=2
            game=fplayadd(play0,backup,game)
            game=cleanup(game)
            game=display.redrawgamewindow(screen,game)
        else:
            play0[-1] = float(play0[-1])

            #2's legal on Aces
            if int(round(game.gamemode[1])) == 14 and int(round(play0[-1])) == 2:
                game.gamemode[1] = float(play0[-1])
                game=fplayadd(play0,backup,game)
                game=cleanup(game)
                game=display.redrawgamewindow(screen,game)
    return play0,game

def len4check(play0,game,screen):
    #checks 4 card hands
    backup = list(play0)
    thishand=[0,0,0]
    hastwo=False
    # card conversion to number
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play0]
    #check if legal twopair/quads
    if round(float(play0[0])) == round(float(play0[1])) and round(float(play0[2]))==round(float(play0[3])):
        #hastwo variable used for twopair of twos beating twopair of aces
        if round(float(play0[0])) == 2:
            hastwo = True

        #set gamemode to poker, gamemode[0]=3
        if game.gamemode[0]==0:
            game.gamemode[0]=3

        #if both pairs are equal we have quads, thishand[2]=6/gamemode[2]=6, otherwise thishand[2]=1/gamemode[2]=1
        if round(float(play0[1]))==round(float(play0[2])):
            thishand[2]=6
        else:
            thishand[2]=1
        thishand[1]=float(play0[-1])

        #changes game state to play the new hand
        if thishand[2]>game.gamemode[2]:
            game.gamemode[1]=float(thishand[1])
            game.gamemode[2]=int(thishand[2])
            game=fplayadd(play0,backup,game)
            game=cleanup(game)
            game=display.redrawgamewindow(screen,game)
            return play0,game

        #checks if the new poker hand is hgiher than the old one
        if thishand[2]==game.gamemode[2]:
            if game.gamemode[1]<thishand[1]:
                #can't play Aces on 2's
                if round(game.gamemode[1]) == 2 and round(thishand[1]) == 14:
                    return play0,game
                game.gamemode[1] = float(thishand[1])
                game=fplayadd(play0,backup,game)
                game=cleanup(game)
                game=display.redrawgamewindow(screen,game)
                return play0,game

            else:
                #2's on Aces legal
                if round(game.gamemode[1])==14 and hastwo==True:
                    game.gamemode[1]=float(play0[1])
                    game=fplayadd(play0,backup,game)
                    game=cleanup(game)
                    game=display.redrawgamewindow(screen,game)
    return play0,game

def len5check(play0,game,screen):
    #checks 5 card hands
    x=0
    backup=list(play0)
    thishand=[0,0,0]
    hastwo=False

    #checks if we have a flush, sets variable to 4 if we do
    if play0[0][-1] == play0[1][-1] == play0[2][-1] == play0[3][-1] == play0[4][-1]: thishand[2]=4
    # card conversion to number after we check for flushes
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in play0];backup3=list(play0)

    while x != len(play0):  ###redo
        play0[x] = int(play0[x][:-2]);x += 1
    play0.sort()

    #allows 2 high flushes to beat Ace high flushes
    if thishand[2] == 4:
        thishand[1] = float(backup3[-1])
        if round(float(backup3[0]))==2:
            hastwo=True

    #check for straights
    if play0[0]+1==play0[1] and play0[1]+1==play0[2] and play0[2]+1==play0[3] and play0[3]+1==play0[4]:

        #if the play is a straight and a flush we have a straight flush, thishand[1] is the card to beat in the poker hand (high card for straight/stfl)
        if thishand[2] == 4:
            thishand[2] = 7
            thishand[1]=float(backup3[-1])
        else:
            thishand[2]=3
            thishand[1]=float(backup3[-1])

    #check if hand is a through straight
    if play0 == [2, 11, 12, 13, 14] or play0 == [2, 3, 12, 13, 14] or play0 == [2, 3, 4, 13, 14] or play0 == [2, 3, 4, 5, 14]:
        if thishand[2]==4:
            thishand[2]=7
        else:
            thishand[2]=3
        x=0
        #finds the high card for the through straight
        while x<len(play0):
            if play0[x]+9 ==play0[x+1]:
                thishand[1]=float(backup3[x])
                break
            else:x += 1
    #fullhouse/4 of a kind check, we don't get a legal kicker with two pair
    x = play0.count(play0[0]);y = play0.count(play0[-1])
    #quads check
    if x==4 or y==4:
        thishand[1]=play0[2];thishand[2]=6
    #full house check
    if x==3 and y==2 or y==3 and x==2:
        thishand[1]=play0[2];thishand[2]=5
    #if we don't have a legal poker hand at this point we return
    if thishand==[0,0,0]:
        return play0,game
    #if the new hand is higher than the old one we game gamemode and move the correct cards to thier new spots
    if game.gamemode[2]<thishand[2]:
        game.gamemode[0]=3
        game.gamemode[1]=float(thishand[1])
        game.gamemode[2]=int(thishand[2])
        game=fplayadd(play0,backup,game)
        game=cleanup(game)
        game=display.redrawgamewindow(screen,game)
        return play0,game
    #if the poker hand is the same type of hand we have to check to see if the new one is higher
    if game.gamemode[2]==thishand[2]:
        if game.gamemode[1] < thishand[1]:
            #can't play 2's on Aces
            if round(game.gamemode[1])==2 and round(thishand[1])==14:
                return play0,game
            game.gamemode[1] = float(thishand[1])
            game.gamemode[2] = int(thishand[2])
            game=fplayadd(play0,backup,game)
            game=cleanup(game)
            game=display.redrawgamewindow(screen,game)
        else:
            #allows 2 high poker hands to be played on Ace high poker hands
            if round(game.gamemode[1])==14 and round(thishand[1])==2:
                game.gamemode[1] = float(thishand[1])
                game=fplayadd(play0, game)
                game=cleanup(game)
            #allows 2 high flushes to be played on Ace high flushes
            if round(game.gamemode[1])==14 and hastwo==True:
                game.gamemode[1]=float(backup3[0])
                game=fplayadd(play0,backup,game)
                game=cleanup(game)
                game=display.redrawgamewindow(screen,game)
    return play0,game

def fplayadd(play0,backup,game):
    #shows the middle area of what is played
    x=0
    game.fplay=[]
    #move Aces to the front of poker hands so they look correct
    if round(game.gamemode[1])==5 and game.gamemode[2]==7 or game.gamemode[2]==3 and round(game.gamemode[1])==5:
        game.fplay.append(backup[-1])
        backup.insert(0,game.fplay[0])
        game.fplay=[]
        backup.pop(-1)
    #adds the cards used to the log for the undo feature
    game.log.append(backup)
    game.log.append(list(game.main))
    game.log.append(list(game.gamemode))
    game.log.append(1)
    #adds used cards to fplay which shows the played cards, showthis which is a menu option to see that last played hand, and used which stores all used cards for the AI
    while x !=len(play0):  ###redo
        game.fplay.append(backup[x])
        game.showthis.append(backup[x])
        game.used.append(backup[x])
        x+=1
    return game

def cleanup(game):
    #this function takes most of the actions needFed to make the game run properly ie removing/adding cards from lists
    game.lastmouse1=[0,0]
    x=0
    #if player 1's play remove player 1's played cards, else do player 2
    if game.main[0]==1:  ###redo
        while x != len(game.fplay) :
            game.player1.remove(game.fplay[x])
            x+=1
    else:
        while x != len(game.fplay):  ###redo
            game.player2.remove(game.fplay[x])
            x+=1
    game=resetplay(game)
    #sets main to it's correct game state
    if game.main[0]==1:
        game.main=[2,2]
        return game
    if game.main[0]==2:
        game.main=[1,2]
    return game

def resetplay(game):
    #resets selected cards for undo button error prevention
    if game.main[0]==1:
        game.play=[]
    else:
        game.play2=[]
    return game