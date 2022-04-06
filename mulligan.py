import basic as basic
def n2aksetup(game):
    x=0
    this=[]
    temp=[]
    game.hand=list(game.player2)
    #remove 2ak and add to its own list
    while x != len(game.hand):
        if int(game.hand[x][:-1]) == 2 or int(game.hand[x][:-1]) == 13 or int(game.hand[x][:-1]) == 14:  ##terrible code but 14 literally didnt work
            game.n2akout.append(game.hand[x])
            game.hand.pop(x);x -= 1
        x += 1

    #change hand into int
    game.hand = [x[:-1] for x in game.hand]
    game.hand = list(map(int, game.hand))
    x = 0
    y = 0
    #move the outliers to its list
    while x != len(game.hand):
        if game.hand[x] == game.hand[x + 1]:
            x += 1
            y += 1
            if x==len(game.hand)-1:
                break
            else:
                continue
        else:
            if y == 0:
                game.outliers.append(game.hand[x])
        x += 1
        y = 0

        if x == len(game.hand) - 1:
            break

    if y == 0:
        game.outliers.append(game.hand[x])
    x=0
    #sets quads, then removes it from hand
    for i in game.hand:
        if game.hand.count(i)==4 and i not in game.quads:
            game.quads.append(i)
    for i in game.quads:
        game.hand.remove(i)
        game.hand.remove(i)
        game.hand.remove(i)
        game.hand.remove(i)

    #change 2ak to numbers
    while x!=len(game.n2akout):
        game.n2akout[x]=int(game.n2akout[x][:-1])
        x+=1

    #check for quads in 2ak
    for i in game.n2akout:
        k=game.n2akout.count(i)
        for j in range(k):
            if k==4 and i not in game.quads:
                game.quads.append(i)
                game.n2akout.remove(i)

    #add outliers to the mulligan
    for i in game.outliers:
        this.append(i)
        if len(this)==3: break

    #if we don't have enough outliers we figure out what gets mulliganed, 'this'  variable is the list of mulligned cards and temp is the variables turned into cards
    if len(this) < 3:
        game.hardmull = []
        game=hardermull(game)
        game.hardmull.sort()
        this = list(game.hardmull)

    #readjust hand and outliers to remove the mulligan and also adds the correct outliers to outliers
    outliersonlythis=list(game.outliers);handbackup=list(game.hand)
    for i in this:
        if i in game.hand:
            game.hand.remove(i)
        if i in outliersonlythis:
            outliersonlythis.remove (i)
    for i in game.hand:
        if game.hand.count(i)==1 and i not in game.outliers:
            outliersonlythis.append(i)
    mulltiebreaker=sum(outliersonlythis)

    x=0
    y=0

    #find cards in the hand and add it to the mulligan possibilities
    while x!=3:
        while y!=len(game.player2):
            if this[x]==int(game.player2[y][:-1]) and game.player2[y] not in temp:
                temp.append(game.player2[y])
                break
            y+=1
        x+=1;y=0
    if len(outliersonlythis)>0:
        game.mullnotes.append(len(outliersonlythis))
    else:
        game.mullnotes.append(0)
    game.mullnotes.append(mulltiebreaker)
    game.mullnotes.append('b')
    game.mull.append(temp)
    game.hand=list(handbackup)
    return game

def finalstraight(game):
    must=[]
    straightmull=[]
    testmust=[[],[],0]
    must1=0
    hand0=[]
    handbackup=list(game.hand)

    #find possible straights, and finish them into variable must
    for i in game.outliers:
        for j in game.outliers:
            if 4 >= j - i >= 0:
                testmust[0].append(j)
        if len(testmust[0]) < 3:
            testmust[0].clear()
            continue
        else:
            #this fills in the middle
            for k in range (testmust[0][-1]-testmust[0][0]):
                if testmust[0][0]+k in game.hand:
                    if testmust[0][0]+k not in testmust[0]:
                        testmust[1].append(testmust[0][0]+k)
                else:
                    testmust[0].clear()
                    testmust[1].clear()
                    break

            testmust[2] = int(len(testmust[0]));testmust[0] = testmust[0] + list(testmust[1])
            testmust[0].sort()
            testmust[1].clear()
            if len(testmust[0]) == 0:
                continue

            #this fills in the ends, because the loop only loops ythrough outliers we need the before straight part
            if len(testmust[0]) != 5:
                if testmust[0][0] - 1 in game.hand and len(testmust[0]) != 5:
                    testmust[0].append(testmust[0][0] - 1)
                    testmust[0].sort()

                if testmust[0][0] - 1 in game.hand and testmust[0][0] - 1 in game.hand and len(testmust[0]) != 5:
                    testmust[0].append(testmust[0][0] - 1)
                    testmust[0].sort()

                if testmust[0][-1] + 1 in game.hand and len(testmust[0]) != 5:
                    testmust[0].append(testmust[0][-1] + 1)
                    testmust[0].sort()

                if testmust[0][-1] + 1 in game.hand and testmust[0][-1] + 2 in game.hand and len(testmust[0]) != 5:
                    testmust[0].append(testmust[0][-1] + 1)
                    testmust[0].sort()

            if len(testmust[0]) != 5:
                testmust[0].clear()
                testmust[1].clear()
                testmust[2] = 0

            if testmust[2] > must1: must = list(testmust[0]);must1 = int(testmust[2])
            testmust[0].clear()
            testmust[1].clear()
            testmust[2] = 0

    #continue if we have a straight, return if we have no possible straights
    if not must:
        game.hand=list(handbackup)
        return game

    #remove straight from hand
    #straight adjustment x2 we mull the low cards instead of the top end of the straight
    if must[-1]+1 in game.outliers:
        game.hand.sort()
        must.pop(0)
        game.outliers.remove(must[-1]+1)
        must.append(must[-1]+1)

    if must[-1]+1 in game.outliers:
        game.hand.sort()
        must.pop(0)
        game.outliers.remove(must[-1] + 1)
        must.append(must[-1] + 1)

    for i in must:
        game.hand.remove(i)
        if i in game.outliers:
            game.outliers.remove(i)

    #adjust the rest of the cards that need adjusting from removing the straight from the hand
    for i in game.hand:
        if game.hand.count(i)==1 and i not in game.outliers:
            game.outliers.append(i)
    game.outliers.sort()
    for i in game.outliers:
        straightmull.append(i)
        if len(straightmull)==3:
            break
    #if we have less then 3 outliers we have to figure out what gets mulliganed using hardermull
    if len(straightmull)<3:
        game.hardmull=[]
        game = hardermull(game)
        game.hardmull.sort()
        straightmull=list(game.hardmull)

    #remove the correct cards from the hand and add it to the list of mulligan possibilities
    for i in straightmull:
        if i in game.hand:
            game.hand.remove(i)
    for i in game.hand:
        if game.hand.count(i)==1:
            hand0.append(i)
    game.outliers=list(hand0)
    x = 0
    y = 0
    mulltiebreaker=sum(game.outliers)

    #turn the numbers in the mulligan into cards
    while y!=3:
        if int(game.player2[x][:-1])==straightmull[y]:
            straightmull[y]=str(game.player2[x])
            y+=1
        x+=1

    #append the cards mulliganed and the number of outliers removed to the list mull/mullnotes
    if len(game.outliers)<0:
        game.mullnotes.append(0)
    else:
        game.mullnotes.append(int(len(game.outliers)))
    game.mull.append(straightmull)
    game.mullnotes.append(mulltiebreaker)
    game.mullnotes.append('t')
    game.hand=list(handbackup)
    return game

def finalflush(game):
    pokerremove=[]
    must=[]
    w=0
    x=0
    y=0
    possflush=[]
    flushmull=[]
    firsttwo=[]
    flushnotes=[]
    oldhand=list(game.hand)
    oldoutliers=list(game.outliers)
    temp=[]
    hand0=[]
    suits = [[], [], [], []]

    #seperate hand into suits, skip 2ak
    while x != len(game.player2):
        if int(game.player2[x][:-1])==2 or int(game.player2[x][:-1])==13 or int(game.player2[x][:-1])==14:
            x+=1
            continue
        if int(game.player2[x][:-1]) in game.quads:
            x += 1
            continue
        if game.player2[x][-1:] == 'd':
            suits[0].append(int(game.player2[x][:-1]))
        if game.player2[x][-1:] == 'c':
            suits[1].append(int(game.player2[x][:-1]))
        if game.player2[x][-1:] == 'h':
            suits[2].append(int(game.player2[x][:-1]))
        if game.player2[x][-1:] == 's':
            suits[3].append(int(game.player2[x][:-1]))
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
    if not possflush:
        return game
    x=0
    y=0
    z=1
    a=0

    #check if we have a viable straightflush
    while x != (len(possflush)):  ### stfl test, pretty sure this is correct, y should only be 0 if its 5 card stfl and max 1 if it's 6 cards, needs to be redone
        while y <= len(possflush[x]) - 4: #not 100% about this sign
            if possflush[x][y]+z in possflush[x] and z>4:
                z+=1
                continue
            else:
                if z>=4:
                    for i in range (z):
                        temp.append(possflush[x][y]+a)
                        a+=1
                a=0;z=0;y+=1
                if temp: break
        if temp:
            possflush.append(temp)
            flushnotes.append(flushnotes[x]+'stfl')
            temp=[]
        x+=1
    x=0
    temp=[]

    #loop through all available flushes
    while w!=len(possflush):
        while x!=len(possflush[w]):
            #check if we have enough cards to have a viable flush
            if int(possflush[w][x]) in game.outliers:
                must.append(possflush[w][x])
            else:
                if len(firsttwo)<2:
                    firsttwo.append(possflush[w][x])
            x+=1
        #we don't have enough for a flush, continue
        if len(must)<3:
            must=[]
            w+=1
            x=0
            flushnotes.pop(0)
            continue

        #we have 3 outliers for a flush so we use them and the lowest 2 usable in suit to make our flush
        if len(must)==3:
            pokerremove=list(must)
            pokerremove.append(firsttwo[0])
            pokerremove.append(firsttwo[1])
            pokerremove.sort()
            game.outliers.append(firsttwo[0])
            game.outliers.append(firsttwo[1])
            game.outliers.sort()
        #we have 4 outliers for a flush and we use the lowest available in suit to make our flush
        if len(must)==4:
            pokerremove=list(must)
            pokerremove.append(firsttwo[0])
            pokerremove.sort()
            game.outliers.append(firsttwo[0])
            game.outliers.sort()
        #if we have more than 5 usable cads of a suit we use the lowest 5
        if len(must)>5:
            for i in must:
                must.pop(0)
                if len(must)==5:
                    break

        #remove the cards from where they need to go and add them to thier new lists, pokerremove/must is our flush
        for i in pokerremove:
            game.hand.remove(i)
        game.outliers=[]
        for i in game.hand:
            if game.hand.count(i) == 1:
                game.outliers.append(i)

        #add new outliers to our mulligan
        for i in game.outliers:
            if len(flushmull)<3:
                flushmull.append(i)

        #if we don't have enough outliers for our mulligan we figure out what cards to mulligan
        if len(flushmull) <3:
            game.hardmull=[]
        game=hardermull(game)
        game.hardmull.sort()
        flushmull=list(game.hardmull)

        #remove excess pairs from outliers, I don't remember why we need to do this
        for i in flushmull:
            if i in game.hand: game.hand.remove(i)
        for i in game.hand:
            if game.hand.count(i) == 1:
                hand0.append(i)

        game.outliers = list(hand0)
        mulltiebreaker=sum(game.outliers)
        x=0
        y=0

        # remove the correct cards from hand and add it to the list of possibilities to mulligan
        for i in flushmull:
            for j in game.player2:
                if i==int(j[:-1]) and j[-1]!=flushnotes[0]:  # stops mulligan from mulliganing the flush
                    if j in temp:
                        continue
                    else:
                        temp.append(j)
                        break
                if len(temp)==3:
                    break
            if len(temp) == 3:
                break
        game.mull.append(temp)
        if len(game.outliers) <0:
            game.mullnotes.append(0)
        else:
            game.mullnotes.append(len(game.outliers))
        game.mullnotes.append(mulltiebreaker)
        game.mullnotes.append(flushnotes[0])
        flushnotes.pop(0)
        w+=1
        x=0
        game.hand=list(oldhand)
        firsttwo=[]
        game.outliers=list(oldoutliers)
        flushmull=[]
        must=[]
        temp=[]
    return game

def hardermull(game):
    n2akline=['13d', '14d', '13c', '14c', '2d', '2c', '2h', '13h', '14h', '2s', '13s', '14s']
    n2akoutliers=[0, 0, 0]
    c2=0 #lowest pair
    c3=0 #lowest trip
    c22=0 #second lowest pair
    c33=0 #second lowest trip
    c333=0 #third lowest trip
    for i in game.hand:
        #figures out low pair and low trips, c22 is second lowest pair
        if game.hand.count(i)==2 and c2==0:
            c2=i
        if game.hand.count(i) == 3 and c3==0:
            c3=i
        if game.hand.count(i) == 2 and c22==0 and i!=c2:
            c22 = i
        if game.hand.count(i)==3 and c33==0 and i!=c3:
            c33=i
        if game.hand.count(i)==3 and c333==0 and c33!=0 and i!=c3 and i!=c33:
            c333=i

    #no quads hardermull
    #check1 1 outlier + bottom pair
    if len(game.outliers)==1 and c2 !=0:
        game.hardmull=[c2,c2,game.outliers[0]]

    #check2 1 outlier + lowest trip and second lowest trip
    if len(game.outliers)==1 and len(game.hardmull)!=3 and c33 !=0:
        game.hardmull = [game.outliers[0],c3,c33]

    #check3 1 outlier + 2 of low trip
    if len(game.outliers)==1 and len(game.hardmull)!=3 and c33 ==0:
        #take 2 trip + outlier if it's lower than the outlier
        if game.outliers[0]>c3:
            game.hardmull = [game.outliers[0],c3, c3]

        #take all of low trip if it's lower than outlier
        else:
            game.hardmull = [c3,c3, c3]

    if len(game.outliers)==2 and c3==0:
        if c2>game.outliers[1]:
            #with 2 outliers take both if c2 > outlier1
            game.hardmull = [c2, game.outliers[0], game.outliers[1]]
        else:
            # if c2<2nd lowest outlier take it instead
            game.hardmull = [game.outliers[0], c2,c2]
    if len(game.outliers)==2 and c3!=0:
        #take 1 in trip and pair
        game.hardmull = [c3, game.outliers[0], game.outliers[1]]
    if len(game.outliers)==0 and c3!=0:
        #take low trip
        game.hardmull = [c3, c3,c3]
    if len(game.outliers)==0 and c3==0:
        #take 2 low pair
        game.hardmull = [c2, c2, c22]
    game.hardmull.sort()
    if game.hardmull:
        return game

    #quads hardermull
    #outliers are in base numbers, we already removed poker hands at this point
    #while y !=len(n2akout):n2akout[y]=int(n2akout[y][:-1]);y+=1 commented out 7/28
    n2akoutliers[0]=game.n2akout.count(2)
    n2akoutliers[1]=game.n2akout.count(13)
    n2akoutliers[2]=game.n2akout.count(14)
    y=0
    if len(game.outliers)==1:
        #the 1 outlier is always in
        game.hardmull.append(game.outliers[0])
        if n2akoutliers==[1,1,1]:
            for i in n2akline:
                if i in game.player2:
                    #add the cards in n2ak line, this variable is aguide on what to mulligan next
                    game.hardmull.append(int(i[:-1]))
                    y+=1
                if y==2:
                    break

        if c33 !=0 and len(game.hardmull)!=3:
            #trim 2 trips
            game.hardmull=[game.outliers[0],c3,c33]
        if c3 !=0 and 3 in n2akoutliers and len(game.hardmull)!=3:
            if n2akoutliers[0]==3:
                #we have to take a good card here so we take a 2 the outlier and trim trip so we don't have to take more good cards
                game.hardmull = [game.outliers[0], c3, 2]
            if n2akoutliers[1] == 3:
                # we have to take a good card here so we take a King
                game.hardmull = [game.outliers[0], c3, 13]
            if n2akoutliers[2] == 3:
                # we have to take a good card here so we take an Ace
                game.hardmull = [game.outliers[0], c3, 14]

        if c2 !=0 and len(game.hardmull)!=3:
            #taking outlier + low pair is ideal
            game.hardmull = [game.outliers[0], c2,c2]

        if len(game.quads)>=2 and len(game.hardmull)!=3:
            game.quads.sort()
            #if we have to we break lowest quads for mulligan
            game.hardmull = [game.outliers[0], game.quads[0],game.quads[0]]

        if c3!=0 and len(game.hardmull)!=3:
            if game.hardmull[0]<c3:
                #we're basically mulliganing the full trip but keep 1 of the trip if the outlier is lower
                game.hardmull = [game.outliers[0], c3,c3]
            else:
                #mulligan low trip
                game.hardmull.clear()
                game.hardmull = [c3, c3, c3]

        #at very worst case we have to take 2 from our good cards (2,K,A)
        if len(game.hardmull)!=3:
            for i in n2akline:
                if i in game.player2:
                    game.hardmull.append(int(i[:-1]))
                    if len(game.hardmull)==3:
                        break
    if len(game.outliers)==2:
        game.hardmull.append(game.outliers[0])
        game.hardmull.append(game.outliers[1])

        #1 outlier in n2ak, take one of them
        if 1 in n2akoutliers and len(game.hardmull)!=3:
            mulloneofthese=[]
            if n2akoutliers[0]==1:
                mulloneofthese.append(2)
            if n2akoutliers[1]==1:
                mulloneofthese.append(13)
            if n2akoutliers[2]==1:
                mulloneofthese.append(14)

            #this makes it so that we follow the 2akline with this block of code
            for i in n2akline:
                if i in game.hand and int(i[:-1]) in mulloneofthese:
                    game.hardmull.append(i)
        #2 outliers in n2ak, take according to n2akline
        if n2akoutliers.count(1)==2 and len(game.hardmull)!=3:
            for i in n2akline:
                if i in game.hand:
                    game.hardmull.append(i)
        #the rest of the possibilities
        if c3 !=0 and len(game.hardmull)!=3:
            game.hardmull.append(c3)
        if c2!=0 and len(game.hardmull)!=3:
            game.hardmull.append(c2)
        if len(game.hardmull)==2:
            for i in n2akline:
                if i in game.player2:
                    game.hardmull.append(int(i[:-1]))
                    break

    # 0 outliers in hand
    if len(game.outliers)==0:

        #very difficult mulligan territory, this is based heavily off how many 2 A K you have
        if n2akoutliers.count(1)==0 and len(game.hardmull)!=3:


            if c2!=0 and c3!=0 and c22!=0 and c2<c3:
                game.hardmull=[c2,c2,c22]
            if c2!=0 and c3!=0 and c2>c3:
                game.hardmull = [c3, c3, c3]
            if c3==0 and c2!=0 and c22!=0:
                game.hardmull = [c2, c2, c22]
        if n2akoutliers.count(1) == 1 and len(game.hardmull)!=3:
            #break low trips(c3) if we have 3 trips at this stage including 2ak
            if c333!=0:
                game.hardmull = [c3, c3, c3]
            if c33!=0 and 3 in n2akoutliers and len(game.hardmull)!=3:
                game.hardmull = [c3, c3, c3]
            if c3!=0 and n2akoutliers.count(3)==2 and len(game.hardmull)!=3:
                game.hardmull = [c3, c3, c3]

            #if we have a 4 pair+trip hand we mull bottom pair (c2) +2ak
            if c2 != 0 and len(game.hardmull) != 3:
                game.hardmull=[c2,c2]
                mulloneofthese = []
                if n2akoutliers[0] == 1 and len(game.hardmull) != 3:
                    mulloneofthese.append(2)
                if n2akoutliers[1] == 1 and len(game.hardmull) != 3:
                    mulloneofthese.append(13)
                if n2akoutliers[2] == 1 and len(game.hardmull) != 3:
                    mulloneofthese.append(14)
                for i in n2akline:
                    if i in game.hand and int(i[:-1]) in mulloneofthese:
                        game.hardmull.append(i)
            if len(game.hardmull) != 3:  #idk if this is needed
                for i in n2akline:
                    if i in game.player2:
                        game.hardmull.append(int(i[:-1]))
                        if len(game.hardmull) == 3:
                            break

        if n2akoutliers.count(1) == 2 and len(game.hardmull)!=3:
            #first add a n2ak outlier, if we have a low pair break it, otherwise break low quads, note: not sure if there are any more cases beyond this but it is extremely low %
            if c3!=0:
                game.hardmull = [c3, c3, c3]
            if c2 !=0 and c22!=0 and len(game.hardmull)!=3:
                game.hardmull = [c2, c2, c22]

            #add the 2ak card here then break low quads
            for i in n2akline:
                if i in game.player2:
                    if len(game.hardmull)!=3:
                        game.hardmull.append(int(i[:-1]))
                    else: break
            if len(game.quads)==2 and len(game.hardmull)!=3:
                game.hardmull.append(game.quads[0])
                game.hardmull.append(game.quads[0])
        if n2akoutliers.count(1) == 3 and len(game.hardmull)!=3:
            if c3!=0:
                game.hardmull = [c3, c3, c3]
            if c2 !=0 and c22!=0 and len(game.hardmull)!=3:
                game.hardmull = [c2, c2, c22]
            if len(game.hardmull)!=3:
                game.hardmull = [game.n2akout[0],game.n2akout[1], game.n2akout[2]]
    game.hardmull.sort()
    return game

def mullselect(game):
    final=[10,0,0]
    finalmull=[]
    mullguide=['b','t','d','c','h','s','dstfl','cstfl','hstfl','sstfl']
    game.play2=[]

    while len(game.mull) !=0:
        if final[0]>game.mullnotes[0]:
            final=[game.mullnotes[0],game.mullnotes[1],game.mullnotes[2]]
            finalmull=list(game.mull[0])
            game.mull.pop(0)
            game.mullnotes.pop(0)
            game.mullnotes.pop(0)
            game.mullnotes.pop(0)
            continue

        if final[0]==game.mullnotes[0] and final[1]<game.mullnotes[1]:
            final=list([game.mullnotes[0],game.mullnotes[1],game.mullnotes[2]])
            finalmull=game.mull[0]
            game.mull.pop(0)
            game.mullnotes.pop(0)
            game.mullnotes.pop(0)
            game.mullnotes.pop(0)
            continue

        if final[0]==game.mullnotes[0] and final[1]==game.mullnotes[1]:
            for i in mullguide:
                if final[0]==i:
                    final=list([game.mullnotes[0],game.mullnotes[1],game.mullnotes[2]])
                    finalmull=list(game.mull[0])
                    game.mull.pop(0)
                    game.mullnotes.pop(0)
                    game.mullnotes.pop(0)
                    game.mullnotes.pop(0)
                    continue

                if game.mullnotes[0]==i:
                    game.mull.pop(0)
                    game.mullnotes.pop(0)
                    game.mullnotes.pop(0)
                    game.mullnotes.pop(0)
                    continue

        game.mull.pop(0)
        game.mullnotes.pop(0)
        game.mullnotes.pop(0)
        game.mullnotes.pop(0)
    game.play2=list(finalmull)
    return game

def mulligan(game):
    if game.main!=[0,0]:
        return game
    if len(game.player2)==13:
        return game
    game.n2akout.clear()
    game.hardmull.clear()
    game.mullnotes.clear()
    game.outliers.clear()
    game.quads.clear()
    game.mull.clear()
    game.player2 = basic.sort(game.player2)
    game=n2aksetup(game)
    game=finalflush(game)
    game=finalstraight(game)
    game=mullselect(game)
    return game
