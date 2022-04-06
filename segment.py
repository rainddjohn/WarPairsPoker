import copy;import basic as basic
def remove2ak(game):
    #remove 2ak from hand because we won't use them in poker hands and we don't want them to interfere
    for i in game.p2copy:
        if int(i[:-1])==2 or int(i[:-1])==13 or int(i[:-1])==14:
            game.segp2[0].append(i)
    for i in game.segp2[0]:
        game.p2copy.remove(i)
    return game

def detectpairs(game):
    game.hand = list(game.p2copy)
    x=0
    count=1
    numberhand=[]
    currentnumber=0
    #move pairs to segp2[2], trips to segp2[3], and quads to segp2[4]
    for i in game.p2copy:
        numberhand.append(int(i[:-1]))

    for i in numberhand:
        if i == currentnumber:
            continue
        if not currentnumber:
            currentnumber = i
        move = numberhand.count(i)

        if move == 1:
            for j in game.p2copy:
                if str(i) == j[:-1]:
                    game.segp2[1].append(j)

        if move == 2:
            for j in game.p2copy:
                if str(i) == j[:-1] and j not in game.segp2[2]:
                    game.segp2[2].append(j)

        if move == 3:
            for j in game.p2copy:
                if str(i) == j[:-1] and j not in game.segp2[3]:
                    game.segp2[3].append(j)

        if move == 4:
            for j in game.p2copy:
                if str(i) == j[:-1] and j not in game.segp2[4]:
                    game.segp2[4].append(j)

        if i != currentnumber: currentnumer = i
    game.finalseg=copy.deepcopy(game.segp2)
    return game

def redetectpairs(hand,game):
    #make sure you use copyseg as a variable; exact same code as detectpairs except this doesn't change segp2, it changes copyseg
    x=0
    count=0
    organizer=[[],[],[],[],[]]

    while x!=len(hand):
        if len(hand)==1:
            organizer[1].append(hand[x])
            break
        if hand[x][:-1]==hand[x+1][:-1]:
            count+=1;x+=1
            if x!=len(hand)-1:
                continue
        if count==0:
            organizer[1].append(hand[x])
        if count==1:
            organizer[2].append(hand[x-1])
            organizer[2].append(hand[x])
        if count==2:
            organizer[3].append(hand[x-2])
            organizer[3].append(hand[x-1])
            organizer[3].append(hand[x])
        if count == 3:
            organizer[4].append(hand[x - 3])
            organizer[4].append(hand[x - 2])
            organizer[4].append(hand[x-1])
            organizer[4].append(hand[x])
        count = 0
        x += 1
        #gets the last card in the sequence if it isn't a pair
        if x==len(hand)-1:
            organizer[1].append(hand[x])
            break
    game.copyseg[1]=list(organizer[1])
    game.copyseg[2]=list(organizer[2])
    game.copyseg[3]=list(organizer[3])
    game.copyseg[4]=list(organizer[4])
    return game

def detectflush(game):
    x=0
    suits=[[],[],[],[]]
    y=0
    #finds flushes
    while x!=len(game.p2copy):
        if game.p2copy[x][-1:] == 'd':
            suits[0].append(game.p2copy[x])
        if game.p2copy[x][-1:] == 'c':
            suits[1].append(game.p2copy[x])
        if game.p2copy[x][-1:] == 'h':
            suits[2].append(game.p2copy[x])
        if game.p2copy[x][-1:] == 's':
            suits[3].append(game.p2copy[x])
        x+=1
    x=0
    #if 2 outliers aren't in the flush then it most likely can't be used
    while x!=len(suits):
        if len(suits[x]) >=5:
            for i in suits[x]:
                if i in game.segp2[1]:
                    y+=1
            game.segp2[6].append(suits[x])
            if x==0:
                game.segp2[8].append('d')
            if x == 1:
                game.segp2[8].append('c')
            if x == 2:
                game.segp2[8].append('h')
            if x == 3:
                game.segp2[8].append('s')
            game.segp2[8].append(int(y))
            y=0
        x+=1
    return game

def detectstr(game):
    x = 0
    y=0
    st=[]
    #finds straights
    if not game.p2copy:
        return game
    while x!=len(game.p2copy)-1:
        if int(game.p2copy[x][:-1])==int(game.p2copy[x + 1][:-1]):
            st.append(game.p2copy[x])
            x+=1
            continue
        if int(game.p2copy[x + 1][:-1]) == int(game.p2copy[x][:-1])+1:
            st.append(game.p2copy[x])
            y+= 1
            x+=1
            continue

        else:
            if y>=4:
                st.append(game.p2copy[x])
                game.segp2[5].append(st)
                st=[]
                y=0
            else:st=[]
            y=0
        x+=1
    if y >= 4:
        st.append(game.p2copy[x])
        game.segp2[5].append(st)
    return game

def remove(removezone,game):
    #only usable for copyseg
    y=0
    copy1=copy.deepcopy(removezone)

    for i in removezone:
        if i in game.copyseg[1]:
            game.copyseg[1].remove(i)
            copy1.remove(i);y+=1
            if y == 5: break

    removezone=list(copy1)
    for i in removezone:
        if i in game.copyseg[3]:
            game.copyseg[3].remove(i)
            copy1.remove(i)
            y+=1
            if y == 5:
                break

    removezone = list(copy1)
    for i in removezone:
        if i in game.copyseg[2]:
            game.copyseg[2].remove(i)
            y+=1
            if y==5:
                break
    remake=list(game.copyseg[1]+game.copyseg[2]+game.copyseg[3])
    game.copyseg[1]=[]
    game.copyseg[2]=[]
    game.copyseg[3]=[]
    remake=basic.sort(remake)
    game=redetectpairs(remake,game)
    return game

def removeflush(removezone,game):
    #only usable for copyseg
    y=0
    copy1=copy.deepcopy(removezone)
    flush=[]
    for i in removezone:
        if y == 5: break
        if i in game.copyseg[1]:
            game.copyseg[1].remove(i)
            copy1.remove(i)
            flush.append(i)
            y+=1
            if y == 5:
                break
        if y == 5:
            break
    removezone=list(copy1)

    for i in removezone:
        if y == 5: break
        if i in game.copyseg[3]:
            game.copyseg[3].remove(i)
            copy1.remove(i)
            flush.append(i)
            y+=1
            if y == 5:
                break
        if y == 5:
            break
    removezone = list(copy1)

    for i in removezone:
        if y == 5:
            break
        if i in game.copyseg[2]:
            game.copyseg[2].remove(i)
            flush.append(i)
            y+=1
            if y==5:
                break
        if y == 5:
            break
    remake=list(game.copyseg[1]+game.copyseg[2]+game.copyseg[3])

    game.copyseg[1]=[]
    game.copyseg[2]=[]
    game.copyseg[3]=[]
    remake=basic.sort(remake)
    game=redetectpairs(remake,game)
    flush=basic.sort(flush)
    x=0
    #replaces the flush with the properly removed flush
    for i in game.copyseg[6]:
        if i[0][-1]==flush[0][-1]:
            break
        x+=1
    game.copyseg[6][x] = list(flush)
    return game

def removeflushwithstraight(removezone,game):
    #only usable for copyseg
    y=0
    copy1=copy.deepcopy(removezone)
    flush=[]
    position=0
    for i in removezone:
        if i in game.copyseg[1]:
            game.copyseg[1].remove(i)
            copy1.remove(i)
            flush.append(i)
            if len(flush) == 5:
                break
        else:   #this else statement in the next 3 parts finds if we have a straight that uses a flush piece but the straight has a card it can use instead
                # the straight will use the other piece and the flush will take it's card it has to use
            for k in game.copyseg[1]:
                if i[:-1] in k:
                    for j in game.copyseg[5]:
                        if i[:-1] in j:
                            flush.append(i)
                            game.copyseg[5][position] = k
                            game.copyseg[1].remove(k)
                            copy1.remove(i)
                            if len(flush) == 5:
                                break
                        position += 1
                        if len(flush) == 5:
                            break
                    position = 0
                    if len(flush) == 5:
                        break
                if len(flush) == 5:
                    break

    removezone=list(copy1)
    for i in removezone:
        if i in game.copyseg[3]:
            game.copyseg[3].remove(i)
            copy1.remove(i)
            flush.append(i)
            if len(flush) == 5:
                break
        else:
            for k in game.copyseg[1]:
                if i[:-1] in k:
                    for j in game.copyseg[5]:
                        if i[:-1] in j:
                            flush.append(i)
                            game.copyseg[5][position] = k
                            game.copyseg[1].remove(k)
                            copy1.remove(i)
                            if len(flush) == 5:
                                break
                        position += 1
                        if len(flush) == 5:
                            break
                    position = 0
                    if len(flush) == 5:
                        break
                if len(flush) == 5:
                    break

    removezone = list(copy1)
    for i in removezone:
        if i in game.copyseg[2]:
            game.copyseg[2].remove(i)
            flush.append(i)
            y+=1
            if len(flush)==5:break
        else:
            for k in game.copyseg[1]:
                if i[:-1] in k:
                    for j in game.copyseg[5]:
                        if i[:-1] in j:
                            flush.append(i)
                            game.copyseg[5][position] = k
                            game.copyseg[1].remove(k)
                            copy1.remove(i)
                            if len(flush) == 5:
                                break
                        position += 1
                        if len(flush) == 5:
                            break
                    position = 0
                    if len(flush) == 5:
                        break
                if len(flush) == 5:
                    break

    flush=basic.sort(flush)
    remake=list(game.copyseg[1]+game.copyseg[2]+game.copyseg[3])

    game.copyseg[1]=[]
    game.copyseg[2]=[]
    game.copyseg[3]=[]
    remake=basic.sort(remake)
    game=redetectpairs(remake,game)
    #replaces the flush with the properly removed flush
    if len(flush)==5:
        game.copyseg[6] = list(flush)
    else:
        game.copyseg[6].clear()
    return game

def check(game):
    copysegtotal=0
    finalsegtotal=0  # have to add the line for better outliers
    if len(game.copyseg[1])<len(game.finalseg[1]):
        game.finalseg=copy.deepcopy(game.copyseg)
    if len(game.copyseg[1])==len(game.finalseg[1]):
        for i in game.copyseg[1]:
            x=int(i[:-1])
            copysegtotal=copysegtotal+x
        for i in game.finalseg[1]:
            x=int(i[:-1])
            finalsegtotal=finalsegtotal+x
        if copysegtotal>finalsegtotal:
            game.finalseg=copy.deepcopy(game.copyseg)
    return game

def twoflushesviable(game):
    game.copyseg=copy.deepcopy(game.segp2)
    #this also check for 1 flush viability, still have to do stfl
    if len(game.copyseg[6])==3:
        game.copyseg=remove(game.copyseg[6][0],game.copyseg)
        game.copyseg=remove(game.copyseg[6][1],game.copyseg)
        game.copyseg=remove(game.copyseg[6][2],game.copyseg)
        game.copyseg[5].clear()
        game=check(game)
    if len(game.copyseg[6])==2:
        #switching he flush with higher outliers in front, happens ONLY IN copyseg
        if game.copyseg[8][1]<game.copyseg[8][3]:
            game.copyseg[6].append(game.copyseg[6][0])
            game.copyseg[6].pop(0)
            game.copyseg[8].append(game.copyseg[8][0])
            game.copyseg[8].append(game.copyseg[8][1])
            game.copyseg[8].pop(0)
            game.copyseg[8].pop(0)
        #checks if flush #2 is viable on its own
        if game.copyseg[8][3]>=3:
            backup=copy.deepcopy(game.copyseg)
            game.copyseg[6].pop(0)
            game.copyseg[8].pop(0)
            game.copyseg[8].pop(0)
            game.copyseg[5].clear()
            removeflush(game.copyseg[6][0],game)
            game=check(game)
            game.copyseg=copy.deepcopy(backup)
        removeflush(game.copyseg[6][0],game)
        game.copyseg[5].clear()
        x=0 ## change the #outliers of second flush, if it's not 3< no flush
        for i in game.copyseg[6][1]:
            if i in game.copyseg[1]:
                x+=1
        game.copyseg[8][3]=int(x)
        if x<3:
            return game
        #checks if the two flushes together are viable
        removeflush(copyseg[6][1],game)
        game=check(game)
    if len(game.copyseg[6])==1:
        game.copyseg[5].clear()
        removeflush(game.copyseg[6][0],game)
        game=check(game)
    return game

def straightandflush(game):
    copyseg = copy.deepcopy(game.segp2)
    x=0
    y=0
    listofstraights=[]
    backupseg=[]
    #we have to find best individual straight, straight/flush combined
    usablecards=copy.deepcopy(game.copyseg[1]+game.copyseg[2]+game.copyseg[3])
    basic.usablecards=basic.sort(usablecards)  # redetectpairs(usablecards)  this works
    #find usable straights; I have to remove all other poker hands, check then reset using 'copyseg = copy.deepcopy(segp2)'
    if len(game.copyseg[5])==0:
        return game
    convertedseg=list(game.copyseg[5][0])
    while x!= len(convertedseg):
        convertedseg[x]=int(convertedseg[x][:-1])
        x+=1
    x=0
    while x!=len(convertedseg):
        if len(listofstraights)>=1 and convertedseg[x]==listofstraights[-1][0]:
            x+=1
            continue

        if convertedseg[x]+4 in convertedseg:
            slist=[convertedseg[x],convertedseg[x]+1,convertedseg[x]+2,convertedseg[x]+3,convertedseg[x]+4]
            for i in slist:
                if convertedseg.count(i)!=1:
                    y+=1
            if y<=4:
                listofstraights.append(slist)
            y=0
        x+=1
    x=0;y=0

    #turn list of straights into actual cards
    while x!=len(listofstraights):
        while y!=len(listofstraights[x]):
            for i in game.copyseg[5][0]:
                if int(i[:-1])==listofstraights[x][y]:
                    listofstraights[x][y]=str(i)
                    break
            y+=1
        x+=1;y=0

    ##add straight flush here, go through flushes, see if straight flushes are viable then add them to listofstraights
    x=0 ## we hit vanilla straight, straight/flush (including second/third if we have it), 2 straights
    while x !=len(listofstraights):
        #you need 2 backup segs, the first to have all the card in to make decisions and backupseg2 it what we base decisions off of
        backupseg = copy.deepcopy(game.copyseg)
        game=remove(listofstraights[x],game)
        backupseg2=copy.deepcopy(game.copyseg)
        #checks the first removed straight
        game.copyseg[5]=list(listofstraights[x])
        game.copyseg[6].clear()
        game.copyseg[7].clear()
        game.copyseg[8].clear()
        game=check(game)
        game.copyseg=copy.deepcopy(backupseg2)

        #checks straight+flush[0]; need to see if flush is still viable after removing straight
        if len(game.copyseg[6])>=1: #checks first flush
            game.copyseg[5]=list(listofstraights[x])
            game.copyseg[6] = list(game.copyseg[6][0])
            game.copyseg[8]=[game.copyseg[8][0],game.copyseg[8][1]]
            game.copyseg=removeflushwithstraight(copyseg[6],game)
            if len (game.copyseg[6])==5:
                game=check(game)
            game.copyseg=copy.deepcopy(backupseg2)

        if len(game.copyseg[6])>=2: #checks second flush
            game.copyseg[5]=list(listofstraights[x])
            game.copyseg[6] = list(game.copyseg[6][1])
            game.copyseg[8]=[game.copyseg[8][2],game.copyseg[8][3]]
            game.copyseg=removeflushwithstraight(copyseg[6],game)

            if len (game.copyseg[6])==5:
                game=check(game)
            game.copyseg=copy.deepcopy(backupseg2)

        if len(game.copyseg[6])==3: #checks third flush; didn't do a fourth flush might be needed later
            game.copyseg[5]=list(listofstraights[x])
            game.copyseg[6] = list(game.copyseg[6][2])
            game.copyseg[8]=[game.copyseg[8][4],game.copyseg[8][5]]
            game.copyseg=removeflushwithstraight(copyseg[6],game)

            if len (game.copyseg[6])==5:
                game=check(game)
            game.copyseg=copy.deepcopy(backupseg2)

        #this checks 2 straights
        game.hand=list(game.copyseg[1]+game.copyseg[2]+game.copyseg[3])
        game.hand=basic.sort(game.hand)
        backuphand=copy.deepcopy(game.hand)
        position=0
        for i in game.hand:
            game.hand[position]=int(i[:-1])
            position+=1

        position=0
        rehand2=[]
        game.outliers = []
        rehand=list(game.hand)
        game.hand.sort()
        for i in game.hand:
            if i+1 in game.hand and i+2 in game.hand and i+3 in game.hand and i+4 in game.hand:
                game.outliers.append(i)
                game.outliers.append(i+1)
                game.outliers.append(i+2)
                game.outliers.append(i+3)
                game.outliers.append(i+4)
        #this break means second straight not viable
        #outliers is a dummy list will return if there is no hand, rehand2 is the correct hand
        if len(game.outliers)==0:
            x+=1
            game.copyseg=copy.deepcopy(backupseg)
            continue

        for i in game.outliers:
            if i not in rehand2:
                rehand2.append(i)
        game.outliers=[]
        for i in rehand2:
            game.hand.remove(i)
        for i in game.hand:
            game.outliers.append(i)
        rehand3=[]
        game.used=[]
        for i in backuphand:
            if int(i[:-1]) in rehand2 and int(i[:-1]) not in game.used:
                rehand3.append(i)
                game.used.append(int(i[:-1]))
        for i in rehand3:
            if i in game.copyseg[1]:
                game.copyseg[1].remove(i)
            if i in game.copyseg[2]:
                game.copyseg[2].remove(i)
            if i in game.copyseg[3]:
                game.copyseg[3].remove(i)
        game.copyseg=redetectpairs(game.copyseg[1]+game.copyseg[2]+game.copyseg[3],game)
        game.copyseg[5].clear()
        game.copyseg[6].clear()
        game.copyseg[8].clear()
        game.copyseg[5].append(listofstraights[x])
        game.copyseg[5].append(rehand3)
        game.copyseg=copy.deepcopy(backupseg)
        x+=1
    return game

def segmenthand(game):
    game.segp2=[[],[],[],[],[],[],[],[],[]]
    game.copyseg=[]
    game.finalseg=[]
    game.p2copy=copy.deepcopy(list(game.player2))
    game=remove2ak(game)
    game=detectpairs(game)
    game=detectflush(game)
    game=detectstr(game)
    game=twoflushesviable(game)
    game=straightandflush(game)
    game.segp2=list(game.finalseg)
    print('segment phase player2 =', game.segp2)
    return game