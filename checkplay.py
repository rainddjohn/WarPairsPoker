import basic as basic;import display as display;import segment as segment;import AI as AIm

def playfct(mouse,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,
            p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode,p2copy,segp2,copyseg,finalseg,AIinfo,deck):
    #play is the variable where the players hand input if placed, all cards in play are also in the players hands. Checkplay determines if the play is legal
    if main ==[1,0] or main ==[1,1] or main==[1,2]:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            play0=list(play)
            fplay,player1,player2,main,play,play2,gamemode,lastmouse1=checkplay(play0,player1, player2,main, altreveal,
                screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
    elif main==[2,0] or main ==[2,1] or main==[2,2]:
        if 120 <= mouse[0] <= 200 and 323 <= mouse[1] <= 383:
            play0=list(play2)
            fplay,player1,player2,main,play,play2,gamemode,lastmouse1=checkplay(play0,player1, player2,main, altreveal,
                screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
            if AI and main==[2,0] or AI and main==[2,1] or AI and main==[2,2]:
                finalseg=segment.segmenthand(player2,p2copy,segp2,copyseg,finalseg)
                #AImove
                AIinfo,main,gamemode,player2,log,play2,lastmouse1, p2redraw, fplay,deck,finalseg,pile=AIm.AImove(AIinfo,
                    main,gamemode,player2,log,player1,play2,altreveal, screen, background_color,lastmouse1, p1redraw,
                    p2redraw, AI, concede, backupmain,fplay,deck,finalseg,play,pile,showthis,showlast)
                AIinfo[6].clear()
    return fplay,player1,player2,main,play,play2,gamemode,lastmouse1,finalseg,AIinfo,deck,p2redraw,log,pile

def checkplay(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile,
              p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode):
    #takes you to the correct check function to see if your play is legal
    #added this function long after global play if hand 1 selected cards, play2 is hand 2 selected cards
    if main[0]==0:return fplay,player1,player2,main,play,play2,gamemode,lastmouse1
    play0=basic.sort(play0)
    if len(play0)==1:
        if gamemode[0]==1 or gamemode[0]==0:
            play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1=len1check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
    if len(play0)==2:
        if gamemode[0]==2 or gamemode[0]==0:
            play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1=len2check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
    if gamemode[0]==3 or gamemode[0]==0:
        if len(play0)==3:
            play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1=len3check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
        if len(play0)==4:
            play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1=len4check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
        if len(play0)==5:
            play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1=len5check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode)
    #this feature selects your whole hand if you click on the play button, useful for if your last cards are a poker hand
    if main[0]==1:
        if play0==[]:play=list(player1)
        else: play.clear()
    elif main[0] == 2:
        if play0==[]:play2=list(player2)
        else:play2.clear()
    player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return fplay,player1,player2,main,play,play2,gamemode,lastmouse1

def len1check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode):
    backup = list(play0)
    #card conversion to number
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in play0]
    #check if my card is higher/legal to play on your card
    if gamemode[1] < float(play0[-1]):
        play0[-1]=float(play0[-1])
        if round(gamemode[1]) == 2 and round(play0[-1]) == 14:
            return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
        #sets gamemode to singles, gamemode[0]=1
        if gamemode[0]==0:gamemode[0]=1
        gamemode[1] = float(play0[-1])
        fplay, used,showthis,log=fplayadd(play0,backup,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,showthis,showlast,used,log,gamemode)
        fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay,player1,player2,main,lastmouse1,play,play2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
    else:
        play0[-1]=float(play0[-1])
        #check if it's a 2 that is played on an Ace which is legal
        if int(round(gamemode[1]))==14 and round(play0[-1])==2:
                gamemode[1] = float(play0[-1])
                fplay, used,showthis,log=fplayadd(play0,backup,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,showthis,showlast,used,log,gamemode)
                fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay,player1,player2,main,lastmouse1,play,play2)
                player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1

def len2check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode):
    backup = list(play0)
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play0]
    #card conversion to number, checks to see if we have a legal pair
    if round(float(play0[0])) == round(float(play0[1])) and float(play0[1])> float(gamemode[1]):
        play0[-1] = float(play0[-1])
        #can't play Aces on 2's
        if round(gamemode[1]) == 2 and round(play0[-1]) == 14:
            return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
        #sets gamemode to pairs, gamemode[0]=2
        if  gamemode[0]==0:gamemode[0]=2
        gamemode[1] = float(play0[-1])
        fplay, used,showthis,log=fplayadd(play0,backup,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,showthis,showlast,used,log,gamemode)
        fplay, player1, player2, main, play, play2,lastmouse1 = cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
    else:
        play0[-1] = float(play0[-1])
        #2's playable on Aces
        if int(round(gamemode[1])) == 14 and round(play0[-1]) == 2:
            gamemode[1] = float(play0[-1])
            fplay, used,showthis,log=fplayadd(play0,backup,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,showthis,showlast,used,log,gamemode)
            fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay,player1,player2,main,lastmouse1,play,play2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
    return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1

def len3check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode):
    backup = list(play0)
    # card conversion to number
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play0]
    #checks for three of a kind
    if round(float(play0[0])) == round(float(play0[1]))== round(float(play0[2])) and gamemode[2]<=2:
        if float(play0[1]) > float(gamemode[1]) and gamemode[2]<=2 or gamemode[2]<2:
            play0[-1] = float(play0[-1])
            #no Aces on 2's
            ##  this line gets around a bug that disallows us to declare as int and round 9/1
            x=float(gamemode[1]);x=round(x);y=float(play0[1]);y=round(y)
            if x==2 and y==14:
                return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
            #sets gamemode to poker, gamemode[0]=3
            if gamemode[0]==0:gamemode[0]=3
            gamemode[1] = float(play0[-1]);gamemode[2]=2
            fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
            fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay,player1,player2,main,lastmouse1,play,play2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
        else:
            play0[-1] = float(play0[-1])
            #2's legal on Aces
            if int(round(gamemode[1])) == 14 and int(round(play0[-1])) == 2:
                gamemode[1] = float(play0[-1])
                fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                         lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
                fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay,player1,player2,main,lastmouse1,play,play2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
    return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1

def len4check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode):
    backup = list(play0);thishand=[0,0,0];hastwo=False
    # card conversion to number
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')for word in play0]
    #check if legal twopair/quads
    if round(float(play0[0])) == round(float(play0[1])) and round(float(play0[2]))==round(float(play0[3])):
        #hastwo variable used for twopair of twos beating twopair of aces
        if round(float(play0[0])) == 2:hastwo = True
        #set gamemode to poker, gamemode[0]=3
        if gamemode[0]==0: gamemode[0]=3
        #if both pairs are equal we have quads, thishand[2]=6/gamemode[2]=6, otherwise thishand[2]=1/gamemode[2]=1
        if round(float(play0[1]))==round(float(play0[2])):thishand[2]=6
        else: thishand[2]=1
        thishand[1]=float(play0[-1])
        #changes game state to play the new hand
        if thishand[2]>gamemode[2]:
            gamemode[1]=float(thishand[1]);gamemode[2]=int(thishand[2])
            fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
            fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                     background_color,
                                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
            return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
        #checks if the new poker hand is hgiher than the old one
        if thishand[2]==gamemode[2]:
            if gamemode[1]<thishand[1]:
                #can't play Aces on 2's
                if round(gamemode[1]) == 2 and round(thishand[1]) == 14:
                    return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
                gamemode[1] = float(thishand[1])
                fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                         lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
                fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
                return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
            else:
                #2's on Aces legal
                if round(gamemode[1])==14 and hastwo==True:
                    gamemode[1]=float(play0[1])
                    fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay,
                             background_color,
                             lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used,log,gamemode)
                    fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
                    player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                             background_color,
                                             lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
    return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1

def len5check(play0,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,log,showthis,showlast,used,gamemode):
    x=0;backup=list(play0);thishand=[0,0,0];hastwo=False
    #checks if we have a flush, sets variable to 4 if we do
    if play0[0][-1] == play0[1][-1] == play0[2][-1] == play0[3][-1] == play0[4][-1]: thishand[2]=4
    # card conversion to number after we check for flushes
    play0 = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in play0];backup3=list(play0)
    while x != len(play0):
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
        if thishand[2] == 4: thishand[2] = 7;thishand[1]=float(backup3[-1])
        else:thishand[2]=3;thishand[1]=float(backup3[-1])
    #check if hand is a through straight
    if play0 == [2, 11, 12, 13, 14] or play0 == [2, 3, 12, 13, 14] or play0 == [2, 3, 4, 13, 14] or play0 == [2, 3, 4, 5, 14]:
        if thishand[2]==4:thishand[2]=7
        else:thishand[2]=3
        x=0
        #finds the high card for the through straight
        while x<len(play0):
            if play0[x]+9 ==play0[x+1]:
                thishand[1]=float(backup3[x]);break
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
        return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
    #if the new hand is higher than the old one we game gamemode and move the correct cards to thier new spots
    if gamemode[2]<thishand[2]:
        gamemode[0]=3;gamemode[1]=float(thishand[1]);gamemode[2]=int(thishand[2])
        fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay,
                 background_color,
                 lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
        fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                 background_color,
                                 lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
        return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
    #if the poker hand is the same type of hand we have to check to see if the new one is higher
    if gamemode[2]==thishand[2]:
        if gamemode[1] < thishand[1]:
            #can't play 2's on Aces
            if round(gamemode[1])==2 and round(thishand[1])==14:
                return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1
            gamemode[1] = float(thishand[1]);gamemode[2] = int(thishand[2])
            fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay,
                     background_color,
                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
            fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                     background_color,
                                     lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
        else:
            #allows 2 high poker hands to be played on Ace high poker hands
            if round(gamemode[1])==14 and round(thishand[1])==2:
                gamemode[1] = float(thishand[1])
                fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay,
                         background_color,
                         lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used, log,gamemode)
                fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
            #allows 2 high flushes to be played on Ace high flushes
            if round(gamemode[1])==14 and hastwo==True:
                gamemode[1]=float(backup3[0])
                fplay, used,showthis,log=fplayadd(play0, backup, player1, player2, main, altreveal, screen, play, play2, fplay,background_color,
                             lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain, showthis, showlast, used,log,gamemode)
                fplay,player1,player2,main,play,play2,lastmouse1=cleanup(fplay, player1, player2, main, lastmouse1, play, play2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,background_color,
                                             lastmouse1, pile, p1redraw, p2redraw, AI, concede, backupmain)
    return play0,fplay,player1,player2,main,play,play2,gamemode,lastmouse1

def fplayadd(play0,backup,player1, player2,main, altreveal, screen, play,play2,fplay,background_color,
                                lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain,showthis,showlast,used,log,gamemode):
    x=0;fplay=[]
    #move Aces to the front of poker hands so they look correct
    if round(gamemode[1])==5 and gamemode[2]==7 or gamemode[2]==3 and round(gamemode[1])==5:fplay.append(backup[-1]);backup.insert(0,fplay[0]);fplay=[];backup.pop(-1)
    #adds the cards used to the log for the undo feature
    log.append(backup);log.append(list(main));log.append(list(gamemode)); log.append(1)
    #adds used cards to fplay which shows the played cards, showthis which is a menu option to see that last played hand, and used which stores all used cards for the AI
    while x !=len(play0):
        fplay.append(backup[x]);showthis.append(backup[x]);used.append(backup[x])
        x+=1
    return fplay, used,showthis,log

def cleanup(fplay,player1,player2,main,lastmouse1,play,play2):
    #resets lastmouse1
    lastmouse1=[0,0];x=0
    #if player 1's play remove player 1's played cards, else do player 2
    if main[0]==1:
        while x != len(fplay) :
            player1.remove(fplay[x]);x+=1
    else:
        while x != len(fplay) :
            player2.remove(fplay[x]);x+=1
    play,play2=resetplay(play,play2,main)
    #sets main to it's correct game state
    if main[0]==1:main=[2,2];return fplay,player1,player2,main,play,play2,lastmouse1
    if main[0]==2:main=[1,2]
    return fplay,player1,player2,main,play,play2,lastmouse1

def resetplay(play,play2,main):
    #resets selected cards for undo button error prevention
    if main[0]==1:play=[]
    else:play2=[]
    return play,play2