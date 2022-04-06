import random;import display as display
def getdeck(game):
    suit=['s','h','c','d'];ranks=['2','3','4','5','6','7','8','9','10','11','12','13','14']
    #create our deck
    for r in ranks:
        for s in suit:
            game.deck.append(r+s)
    random.shuffle(game.deck) ##this shuffles
    #this is for the replay game function
    game.backupdeck=list(game.deck)
    return game

def deal(game):
    #deal hands
    while len(game.player1)<=15:
        game.player1.append(game.deck[0])
        game.deck.pop(0)
    while len(game.player2)<=15:
        game.player2.append(game.deck[0])
        game.deck.pop(0)
    return game

def sort(hand):
    nhand = [];i = 0; hand = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in hand]
    #because we have varchar we convert cards to numbers and sort it that way
    while i < len(hand):
        #we seperate the length 3 (9.3), and length 4 (10.3) sort them individually and join them again after
        if len(hand[i]) == 4:
            nhand.append(hand[i])
            hand.remove(hand[i])
        else:
            i += 1
    #convert numbers back to card form
    hand.sort()
    nhand.sort()
    hand = hand + nhand
    hand = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in hand]
    return hand

def startgame(screen,game):
    game.player1.clear()
    game.player2.clear()
    game.play.clear()
    game.fplay.clear()
    game.play2.clear()
    game.main=[0,0]
    game.gamemode=[0,0,0]
    game.pile.clear()
    game.p1redraw=True
    game.p2redraw=True
    game.backupmain=[0,0]
    game.showlast.clear()
    game.showthis.clear()
    game.used.clear()
    game.log.clear()
    game.deck.clear()
    game.concede=False
    game.optionslist=[0,0,0,0,0,0]
    game.AIinfo=[False,False,False,False,False,0,[],False]
    if game.replay==True:
        game.deck=list(game.backupdeck)
        game.replay=False
    else:
        game = getdeck(game)
    game=deal(game)
    game.player1 = sort(game.player1)
    game.player2 = sort(game.player2)
    game=display.redrawgamewindow(screen,game)
    return game

def seewhogoesfirst(game):
    #function to see who has the lowest card in hand and that player goes first
    if len(game.log)==0:
        return game
    if len(game.pile)!=6:
        return game
    if game.log[-1]==-1 or game.log[-1]==-2 or game.main==[0,0]:
        x = (game.player1[0].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4'))
        y = (game.player2[0].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4'))
        if x < y:
            game.main = [1, 1]
        else:
            game.main = [2, 1]
    return game
