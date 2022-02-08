import copy;import basic as basic
def remove2ak(p2copy,segp2):
    #remove 2ak from hand because we won't use them in poker hands and we don't want them to interfere
    for i in p2copy:
        if int(i[:-1])==2 or int(i[:-1])==13 or int(i[:-1])==14:
            segp2[0].append(i)
    for i in segp2[0]:p2copy.remove(i)
    return p2copy,segp2

def detectpairs(p2copy,segp2,finalseg):
    hand = list(p2copy);x=0;count=1;numberhand=[];currentnumber=0
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
    return p2copy,segp2,finalseg

def redetectpairs(hand,copyseg):
    #make sure you use copyseg as a variable; exact same code as detectpairs except this doesn't change segp2, it changes copyseg
    x=0;count=0
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
    return copyseg

def detectflush(p2copy,segp2):
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
    return segp2

def detectstr(p2copy,segp2):
    x = 0;y=0;st=[]
    #finds straights
    if not p2copy:return segp2
    while x!=len(p2copy)-1:
        if int(p2copy[x][:-1])==int(p2copy[x + 1][:-1]): st.append(p2copy[x]);x+=1;continue
        if int(p2copy[x + 1][:-1]) == int(p2copy[x][:-1])+1:st.append(p2copy[x]);y+= 1;x+=1;continue
        else:
            if y>=4:st.append(p2copy[x]);segp2[5].append(st);st=[];y=0
            else:st=[];y=0
        x+=1
    if y >= 4:st.append(p2copy[x]);segp2[5].append(st)
    return segp2

def remove(removezone,copyseg):
    #only usable for copyseg
    y=0;copy1=copy.deepcopy(removezone)
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
    copyseg[1]=[];copyseg[2]=[];copyseg[3]=[];remake=basic.sort(remake);copyseg=redetectpairs(remake,copyseg)
    return copyseg

def removeflush(removezone,copyseg):
    #only usable for copyseg
    y=0;copy1=copy.deepcopy(removezone);flush=[]
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
    copyseg[1]=[];copyseg[2]=[];copyseg[3]=[];remake=basic.sort(remake);copyseg=redetectpairs(remake,copyseg)
    flush=basic.sort(flush)
    x=0
    #replaces the flush with the properly removed flush
    for i in copyseg[6]:
        if i[0][-1]==flush[0][-1]:break
        x+=1
    copyseg[6][x] = list(flush)
    return copyseg

def removeflushwithstraight(removezone,copyseg):
    #only usable for copyseg
    y=0;copy1=copy.deepcopy(removezone);flush=[];position=0
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
    flush=basic.sort(flush);remake=list(copyseg[1]+copyseg[2]+copyseg[3])
    copyseg[1]=[];copyseg[2]=[];copyseg[3]=[];remake=basic.sort(remake);copyseg=redetectpairs(remake,copyseg)
    #replaces the flush with the properly removed flush
    if len(flush)==5:
        copyseg[6] = list(flush)
    else:
        copyseg[6].clear()
    return copyseg

def check(finalseg,copyseg):
    copysegtotal=0;finalsegtotal=0  # have to add the line for better outliers
    if len(copyseg[1])<len(finalseg[1]):finalseg=copy.deepcopy(copyseg)
    if len(copyseg[1])==len(finalseg[1]):
        for i in copyseg[1]:x=int(i[:-1]);copysegtotal=copysegtotal+x
        for i in finalseg[1]:x=int(i[:-1]);finalsegtotal=finalsegtotal+x
        if copysegtotal>finalsegtotal: finalseg=copy.deepcopy(copyseg)
    return finalseg

def twoflushesviable(segp2,copyseg,finalseg):
    copyseg=copy.deepcopy(segp2)
    #this also check for 1 flush viability, still have to do stfl
    if len(copyseg[6])==3:
        copyseg=remove(copyseg[6][0],copyseg);copyseg=remove(copyseg[6][1],copyseg);copyseg=remove(copyseg[6][2],copyseg);copyseg[5].clear();finalseg=check(finalseg,copyseg,copyseg)
    if len(copyseg[6])==2:
        #switching he flush with higher outliers in front, happens ONLY IN copyseg
        if copyseg[8][1]<copyseg[8][3]:copyseg[6].append(copyseg[6][0]);copyseg[6].pop(0);copyseg[8].append(copyseg[8][0]);copyseg[8].append(copyseg[8][1]);copyseg[8].pop(0);copyseg[8].pop(0)
        #checks if flush #2 is viable on its own
        if copyseg[8][3]>=3:
            backup=copy.deepcopy(copyseg);copyseg[6].pop(0);copyseg[8].pop(0);copyseg[8].pop(0); copyseg[5].clear();
            removeflush(copyseg[6][0],copyseg);finalseg=check(finalseg,copyseg);copyseg=copy.deepcopy(backup)
        removeflush(copyseg[6][0],copyseg);copyseg[5].clear()
        x=0 ## change the #outliers of second flush, if it's not 3< no flush
        for i in copyseg[6][1]:
            if i in copyseg[1]: x+=1
        copyseg[8][3]=int(x)
        if x<3: return finalseg
        #checks if the two flushes together are viable
        removeflush(copyseg[6][1],copyseg);finalseg=check(finalseg,copyseg)
    if len(copyseg[6])==1:
        copyseg[5].clear();removeflush(copyseg[6][0],copyseg);finalseg=check(finalseg,copyseg)  ##getting fucked after this
    return finalseg

def straightandflush(segp2,copyseg,finalseg):
    copyseg = copy.deepcopy(segp2);x=0;y=0;listofstraights=[];backupseg=[]
    #we have to find best individual straight, straight/flush combined
    usablecards=copy.deepcopy(copyseg[1]+copyseg[2]+copyseg[3]);basic.usablecards=basic.sort(usablecards)  # redetectpairs(usablecards)  this works
    #find usable straights; I have to remove all other poker hands, check then reset using 'copyseg = copy.deepcopy(segp2)'
    if len(copyseg[5])==0:
        return finalseg
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
        copyseg=remove(listofstraights[x],copyseg)
        backupseg2=copy.deepcopy(copyseg)
        #checks the first removed straight
        copyseg[5]=list(listofstraights[x]);copyseg[6].clear();copyseg[7].clear();copyseg[8].clear();finalseg=check(finalseg,copyseg);copyseg=copy.deepcopy(backupseg2)
        #checks straight+flush[0]; need to see if flush is still viable after removing straight
        if len(copyseg[6])>=1: #checks first flush
            copyseg[5]=list(listofstraights[x]);copyseg[6] = list(copyseg[6][0]);copyseg[8]=[copyseg[8][0],copyseg[8][1]];copyseg=removeflushwithstraight(copyseg[6],copyseg)
            if len (copyseg[6])==5:finalseg=check(finalseg,copyseg)
            copyseg=copy.deepcopy(backupseg2)
        if len(copyseg[6])>=2: #checks second flush
            copyseg[5]=list(listofstraights[x]);copyseg[6] = list(copyseg[6][1]);copyseg[8]=[copyseg[8][2],copyseg[8][3]];copyseg=removeflushwithstraight(copyseg[6],copyseg)
            if len (copyseg[6])==5:
                finalseg=check(finalseg,copyseg)
            copyseg=copy.deepcopy(backupseg2)
        if len(copyseg[6])==3: #checks third flush; didn't do a fourth flush might be needed later
            copyseg[5]=list(listofstraights[x]);copyseg[6] = list(copyseg[6][2]);copyseg[8]=[copyseg[8][4],copyseg[8][5]];copyseg=removeflushwithstraight(copyseg[6],copyseg)
            if len (copyseg[6])==5:
                finalseg=check(finalseg,copyseg)
            copyseg=copy.deepcopy(backupseg2)
        #this checks 2 straights
        hand=list(copyseg[1]+copyseg[2]+copyseg[3]);hand=basic.sort(hand);backuphand=copy.deepcopy(hand);position=0
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
        copyseg=redetectpairs(copyseg[1]+copyseg[2]+copyseg[3])
        copyseg[5].clear();copyseg[6].clear();copyseg[8].clear();copyseg[5].append(listofstraights[x]);copyseg[5].append(rehand3)
        copyseg=copy.deepcopy(backupseg)
        x+=1
    return finalseg

def segmenthand(player2,p2copy,segp2,copyseg,finalseg):
    segp2=[[],[],[],[],[],[],[],[],[]];copyseg=[];finalseg=[]
    p2copy=copy.deepcopy(list(player2))
    p2copy,segp2=remove2ak(p2copy,segp2)
    p2copy,segp2,finalseg=detectpairs(p2copy,segp2,finalseg)
    segp2=detectflush(p2copy,segp2)
    segp2=detectstr(p2copy,segp2)
    finalseg=twoflushesviable(segp2,copyseg,finalseg)
    finalseg=straightandflush(segp2,copyseg,finalseg)
    segp2=list(finalseg)
    print('segment phase player2 =', segp2)
    return finalseg