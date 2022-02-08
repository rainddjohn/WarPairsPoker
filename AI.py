import basic as basic;import copy;import display as display

def coveragefinder(player2,AIinfo,gamemode):
    player2=basic.sort(player2);p2copy2=copy.deepcopy(player2)
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
                if coverage==-5:
                    AIinfo[4]=0;return AIinfo
                    ### if we have a huge hole in coverage we don't go on
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
    return AIinfo

def AIflushstraight(gamemode,finalseg,AIinfo):
    #functions plays straights and flushes if we have them
    print('AIinfo[6]')
    # straight first
    if not AIinfo[6] and finalseg[5] and gamemode[0] == 3 or not AIinfo[6] and finalseg[5] and gamemode[0] == 0:
        if gamemode[2] < 3:
            AIinfo[6] = list(finalseg[5][0])
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
            AIinfo[6] = list(finalseg[6])
            AIinfo[5] = 2
        if gamemode[2] == 4:
            for i in finalseg[6]:
                str = i[-1].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')
                if gamemode[1] < float(str):
                    if round(gamemode[1]) != 2 and round(float(str)) != 14: AIinfo[6] = list(i);AIinfo[5] = 2
                else:
                    if round(float(str)) == 2 and round(gamemode[1]) == 14: AIinfo[6] = list(i);AIinfo[5] = 2
    return AIinfo
def AIFullhHouseQuadsTwoPair(gamemode,finalseg,AIinfo,player1,player2):
    counter=0;valueseg=[]
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
    print('93doiwinseg/TAK/valueseg is',doiwinseg,TAK,valueseg)
    print('94 AIinfo is',AIinfo)
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
            AIinfo[6]=basic.sort(AIinfo[6])
            if AIinfo[6]:AIinfo[6] = [str(a) for a in AIinfo[6]];AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in AIinfo[6]]
            AIinfo[6]=basic.sort(AIinfo[6])
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
            if not AIinfo[6] and len(finalseg[2])!=0:AIinfo[5]=7; AIinfo=doiwin(doiwinseg,AIinfo)
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
            if 'As' in player2:print('As in player2')
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
    AIinfo[6]=basic.sort(AIinfo[6])
    return AIinfo

def doiwin(doiwinseg,AIinfo):
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
                    if 2.4 in therest:
                        AIinfo[5]=9;AIinfo[6]=pairstotest[counter];
                        return AIinfo
                    badtwos=0
                    for j in therest:
                        if j==2.1 or j==2.2 or j==2.3:badtwos+=1
                    badtwos=badtwos-len(doiwinseg[4])
                    if badtwos<=1:
                        AIinfo[5]=9;AIinfo[6]=pairstotest[counter]
                        return AIinfo
            if 14.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                badtwos=0
                for j in therest:
                    if j == 2.1 or j == 2.2 or j == 2.3: badtwos += 1
                badtwos = badtwos - len(doiwinseg[4])
                if 14.1 or 14.2 or 14.3 in therest:badtwos+=1
                if badtwos <= 1:
                    AIinfo[5]=9;AIinfo[6]=pairstotest[counter]
                    return AIinfo
            if 13.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                for i in therest:
                    if round(i)==2:
                        AIinfo[5]=9;AIinfo[6]=pairstotest[counter]
                        return AIinfo
            if 2.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                for i in therest:
                    if round(i)==14:
                        AIinfo[5]=9;AIinfo[6]=pairstotest[counter]
                        return AIinfo
            if AIinfo[4] >=2:
                AIinfo[5]=9;AIinfo[6]=pairstotest[counter]
                return AIinfo
            counter+=1
            doiwinseg = copy.deepcopy(backupcopy)
    return  AIinfo

def AIdraw(AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2):
    plainnumseg=[[],[],[]]
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
        return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2
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
        return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2
    if int(deck[0][:-1]) in plainnumseg[0] or int(deck[0][:-1]) in plainnumseg[2] or deck[1][:-1] == '13' or deck[1][:-1] == '14' or deck[1][:-1]==deck[0][:-1]:
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);
        log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0]
        print('draw2 done')
        return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2
    if p2redraw:
        pile.append(deck[0]);draw.append(deck[0]);deck.pop(0);pile.append(deck[0]);draw.append(deck[0]);deck.pop(0)
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8)
        main=[1,1];gamemode=[0,0,0];p2redraw=False
        print('redraw')
        return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2
    if len(player2)>=4:
        print('draw1#2 done')
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0]
        return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2
    else:
        player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);player2.append(deck[0]);draw.append(deck[0]);deck.pop(0);
        log.append(list(draw));log.append(list(main));log.append(list(gamemode));log.append(8);main=[1,1];gamemode=[0,0,0]
        print('draw2#2 done')
        return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2
    return AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2

def AImove(AIinfo,main,gamemode,player2,log,player1,play2,altreveal, screen, background_color,lastmouse1, p1redraw,
           p2redraw, AI, concede, backupmain,fplay,deck,finalseg,play,pile,showthis,showlast):
    if main[0] == 1: return
    if len(player1)<=2:AIinfo[3]=True
    else: AIinfo[3]=False
    if len(player1)<=4:AIinfo[2]=True
    if len(player1)>=9 and AIinfo[2]==True:AIinfo[2]=False
    if finalseg[4]:AIinfo[7]=True
    if finalseg[7]:AIinfo[7]=True
    AIinfo=coveragefinder(player2,AIinfo,gamemode)
    AIinfo=AIflushstraight(gamemode,finalseg,AIinfo)
    AIinfo=AIFullhHouseQuadsTwoPair(gamemode,finalseg,AIinfo,player1,player2)
    #AIdraw
    AIinfo,finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2=AIdraw(AIinfo,
        finalseg,p2redraw,deck,pile,log,main,gamemode,fplay,showthis,showlast,play,play2,player2)
    AIinfo[6].clear();player2=basic.sort(player2);play2.clear()
    player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                             lastmouse1, pile,
                             p1redraw, p2redraw, AI, concede, backupmain)
    return AIinfo,main,gamemode,player2,log,play2,lastmouse1, p2redraw, fplay,deck,finalseg,pile
###AIinfo= [[0]coverage jam singles,[1]extra 2's,[2]opponent had less than 4 cards,[3]opponent had 2 cards, [4]coverage#,[5]what poker hand we added,[6]the play,[7]strongpokerhand]