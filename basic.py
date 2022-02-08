import random;import display as display
def getdeck(deck,backupdeck):
    suit=['s','h','c','d'];ranks=['2','3','4','5','6','7','8','9','10','11','12','13','14']    ##for spades cut 13 from this and add 14-16 to spades after
    #create our deck
    for r in ranks:
        for s in suit:
            deck.append(r+s)
    random.shuffle(deck) ##this shuffles
    #this is for the replay game function
    backupdeck=list(deck)
    return deck,backupdeck

def deal(player1,player2,deck):
    #deal hands
    while len(player1)<=15:
        player1.append(deck[0]); deck.pop(0)
    while len(player2)<=15:
        player2.append(deck[0]); deck.pop(0)
    return player1,player2,deck

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

def startgame(player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,showthis,used,log,concede
              ,optionslist,AIinfo,play,play2,fplay,pile,altreveal, screen,background_color,lastmouse1,AI,backupmain):
    player1.clear();player2.clear();play.clear();fplay.clear();play2.clear();main=[0,0]; gamemode=[0,0,0];pile.clear();p1redraw=True;p2redraw=True;backupmain=[0,0]
    showlast.clear();showthis.clear();used.clear();log.clear();deck.clear();concede=False;optionslist=[0,0,0,0,0,0];AIinfo=[False,False,False,False,False,0,[],False]
    deck, backupdeck = getdeck(deck, backupdeck)
    player1, player2, deck = deal(player1, player2, deck)
    player1 = sort(player1);player2 = sort(player2)
    player1, player2,main=display.redrawgamewindow(player1, player2,main, altreveal, screen, play,play2,fplay,background_color,lastmouse1,pile, p1redraw,p2redraw,AI,concede,backupmain)
    return player1,player2,deck,backupdeck,main,gamemode,p1redraw,p2redraw,showlast,showthis,used,log,concede,optionslist\
        ,AIinfo,play,play2,fplay,pile,altreveal, screen,background_color,lastmouse1,AI,backupmain

def seewhogoesfirst(main,log,pile,player1,player2):
    #function to see who has the lowest card in hand and that player goes first
    if len(log)==0: return main,log,pile
    if len(pile)!=6:return main,log,pile
    if log[-1]==-1 or log[-1]==-2 or main==[0,0]:
        x = (player1[0].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4'));y = (player2[0].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4'))
        if x < y:
            main = [1, 1]
        else:
            main = [2, 1]
    return main,log,pile
