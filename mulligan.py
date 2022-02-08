import basic as basic
def n2aksetup(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand):
    x=0;this=[];temp=[];hand=list(player2)
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
    if len(this) < 3:
        hardmull = []
        outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand=hardermull(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand)
        hardmull.sort();this = list(hardmull)
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
    return outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand

def finalstraight(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand):
    must=[]; straightmull=[];testmust=[[],[],0];must1=0;hand0=[];handbackup=list(hand)
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
    if not must:hand=list(handbackup);return outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand
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
    if len(straightmull)<3:
        hardmull=[]
        outliers, n2akout, quads, hardmull, player2, mullnotes, mull, hand = hardermull(outliers, n2akout, quads,
                                                                                        hardmull, player2, mullnotes,
                                                                                        mull, hand)
        hardmull.sort();straightmull=list(hardmull)
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
    return outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand

def finalflush(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand):
    pokerremove=[];must=[];w=0;x = 0;y=0;possflush=[];flushmull=[];firsttwo=[];flushnotes=[];oldhand=list(hand);oldoutliers=list(outliers);temp=[];hand0=[]
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
    if not possflush:return outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand
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
        if len(flushmull) <3:hardmull=[]
        outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand=hardermull(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand)
        hardmull.sort();flushmull=list(hardmull)
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
    return outliers, n2akout, quads, hardmull, player2, mullnotes, mull, hand

def hardermull(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand):
    n2akline=['13d', '14d', '13c', '14c', '2d', '2c', '2h', '13h', '14h', '2s', '13s', '14s'];n2akoutliers=[0, 0, 0];c2=0;c3=0;c22=0;c33=0;c333=0
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
    return outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand

def mullselect(mullnotes,mull,play2):
    x=0;y=0;final=[10,0,0];finalmull=[]
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
    return mullnotes,mull,play2

def mulligan(main,gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast):
    if main!=[0,0]:
        return main,gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast
    if len(player2)==13:
        return main,gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast
    n2akout.clear();hardmull.clear();mullnotes.clear();outliers.clear();quads.clear();mull.clear()
    player2 = basic.sort(player2)
    outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand=n2aksetup(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand)
    outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand=finalflush(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand)
    outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand=finalstraight(outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand)
    mullnotes,mull,play2=mullselect(mullnotes,mull,play2)
    return main,gamemode,outliers,n2akout,quads,hardmull,player2,mullnotes,mull,hand,play2,pile,showthis,showlast