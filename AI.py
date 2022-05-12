import basic as basic;import copy;import display as display

def coveragefinder(game):
    game.player2=basic.sort(game.player2);
    game.p2copy2=copy.deepcopy(game.player2)
    #this functions find if you just want to win the game in singles
    rangecards = ['11d', '11c', '11h', '11s', '12d', '12c', '12h', '12s', '13d', '13c', '13h', '13s', '14d', '14c','14h', '14s']
    coverage = 0
    twocount = 0
    rangecap=0
    AKcount=0
    badcardscount=0
    Acecount=0
    for i in game.p2copy2:
        if int(i[:-1])==2:
            twocount+=1
        if 2<int(i[:-1])<11:
            badcardscount+=1
        if int(i[:-1])>=11:
            rangecap=str(i)
            break
    twocountbackup = int(twocount)

    for i in reversed(rangecards):
        if i in game.p2copy2:
            coverage+=1
            if i[:-1] == '13':
                AKcount += 1
            if i[:-1] == '14':
                AKcount += 1
                Acecount+=1
        else:
            if i[:-1]=='14' and twocount>0:
                twocount-=1
            else:
                coverage-=1
                if coverage==-5:
                    game.AIinfo[4]=0
                    return game
                    ### if we have a huge hole in coverage we don't go on
        if i==rangecap:
            break
    twocount=int(twocountbackup)
    leftover2s= Acecount+twocount-4
    if leftover2s>0:
        badcardscount=badcardscount+ leftover2s
        game.AIinfo[1]=True          ### if we have too many twos they are effectively worthless, the 2s is the exception
    twocount=twocount/2

    if game.gamemode[0] != 0:
        badcardscount += 1
    if '2s' in game.p2copy2:
        twocount+=.5
    if AKcount+twocount/2>badcardscount+1:
        game.AIinfo[0]=True     ##if we have enough AK2 to cover enough cards we play singles
    game.AIinfo[4]=int(coverage)
    return game

def AIflushstraight(game):
    #functions plays straights and flushes if we have them
    # straight first
    if not game.AIinfo[6] and game.finalseg[5] and game.gamemode[0] == 3 or not game.AIinfo[6] and game.finalseg[5] and game.gamemode[0] == 0:
        print('do we have doublestraight, finalseg[5] is', game.finalseg[5])
        if game.gamemode[2] < 3:
            game.AIinfo[6] = list(game.finalseg[5][0])
            game.AIinfo[5] = 1
        if game.gamemode[2] == 3:
            str = game.finalseg[5][-1].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')
            if game.gamemode[1] < float(str):
                if round(game.gamemode[1]) != 2 and round(float(str)) != 14:
                    game.AIinfo[6] = list(game.finalseg[5])
                    game.AIinfo[5] = 1
            else:
                if round(float(str)) == 2 and round(game.gamemode[1]) == 14:
                    game.AIinfo[6] = list(game.finalseg[5]) #works as game.finalseg[5][0] for some reason, not sure about double straights yet, will error if theres 2 I guess
                    game.AIinfo[5] = 1
    if len(game.AIinfo[6])!=5 and game.AIinfo[6]:
        game.AIinfo[6]=game.finalseg[5]
    # flush
    if not game.AIinfo[6] and game.finalseg[6] and game.gamemode[0] == 3 or not game.AIinfo[6] and game.finalseg[6] and game.gamemode[0] == 0:
        if game.gamemode[2] < 4:
            game.AIinfo[6] = list(game.finalseg[6])
            game.AIinfo[5] = 2
        if game.gamemode[2] == 4:
            print('finalseg[6] is',game.finalseg[6])
            str = game.finalseg[6][-1][-1].replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4')
            print('str is',str)
            if game.gamemode[1] < float(str):
                if round(game.gamemode[1]) != 2 and round(float(str)) != 14:
                    game.AIinfo[6] = list(game.finalseg[6])
                    game.AIinfo[5] = 2
            else:
                if round(float(str)) == 2 and round(game.gamemode[1]) == 14:
                    game.AIinfo[6] = list(game.finalseg[6])
                    game.AIinfo[5] = 2
    return game

def AIFullhHouseQuadsTwoPair(game):
    counter=0
    valueseg=[]
    TAK=[0,0,0]
    pairstotest=[]
    dummy=[]
    for i in game.finalseg:
        if counter==5:break
        x = game.finalseg[counter]
        x = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in x]
        x = [float(a) for a in x]
        if len(x)>1:
            if x[1]<1:
                x[0]=x[0]+x[1]
                x.pop(-1)
        valueseg.append(x)
        counter += 1
    doiwinseg =copy.deepcopy(valueseg)

    ##doiwinseg put everything into outliers/pairs/trips
    for i in doiwinseg[0]:
        if round(i)==2:
            TAK[0]+=1
        if round(i) == 13:
            TAK[1] += 1
        if round(i) == 14:
            TAK[2] += 1

    #assembles pairs to test to see if we can play them and win, and also moves them into doiwinseg
    for i in TAK:
        if i==1:
            doiwinseg[1].append(doiwinseg[0][0])
            doiwinseg[0].pop(0)
        if i == 2:
            pairstotest.append([doiwinseg[0][0],doiwinseg[0][1]])
            doiwinseg[2].append(doiwinseg[0][0]);doiwinseg[0].pop(0)
            doiwinseg[2].append(doiwinseg[0][0]);doiwinseg[0].pop(0)
        if i==3:
            pairstotest.append([doiwinseg[0][0],doiwinseg[0][1]])
            doiwinseg[3].append(doiwinseg[0][0])
            doiwinseg[0].pop(0);doiwinseg[3].append(doiwinseg[0][0])
            doiwinseg[0].pop(0);doiwinseg[3].append(doiwinseg[0][0])
            doiwinseg[0].pop(0)

    for i in doiwinseg[4]:
        dummy.append(round(i))
        doiwinseg[4].pop(0);doiwinseg[4].pop(0)
        doiwinseg[4].pop(0)
    doiwinseg[4]=list(dummy)
    #odd straights and flushes
    if len(game.player2)==5 and len(doiwinseg[1])==5: #not calculating gamemode only do this if we win
        if game.gamemode[0]==0 or game.gamemode[0]==3:
            weirdstraight=copy.deepcopy(doiwinseg[1])
            weirdstraight.sort()
            weirdstraight=[round(i) for i in weirdstraight]
            if weirdstraight==[2,3,4,13,14] or weirdstraight==[2,3,4,5,14] or weirdstraight==[2,3,12,13,14] or weirdstraight==[2,11,12,13,14] or weirdstraight==[10,11,12,13,14] or weirdstraight==[9,10,11,12,13]:
                game.AIinfo[6] = list(doiwinseg[1])
                game.AIinfo[5] = 1
            if doiwinseg[1][0]*10%10==doiwinseg[1][1]*10%10==doiwinseg[1][2]*10%10==doiwinseg[1][3]*10%10==doiwinseg[1][4]*10%10:
                game.AIinfo[6] = list(doiwinseg[1])
                game.AIinfo[5] = 2
            game.AIinfo[6]=basic.sort(game.AIinfo[6])
            if game.AIinfo[6]:
                game.AIinfo[6] = [str(a) for a in game.AIinfo[6]]
                game.AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in game.AIinfo[6]]
            game.AIinfo[6]=basic.sort(game.AIinfo[6])
    counter=0
    #trips and extra trips
    if game.gamemode[0]==3 and game.gamemode[2]<=2 or game.gamemode[0]==0:
        if not game.AIinfo[6]:
            if len(game.finalseg[2]) <= 2 and len(game.finalseg[3]) >= 6 or len(game.finalseg[3])==9 or len(game.finalseg[3]) >= 3 and len(game.finalseg[2])==0:
                for i in valueseg[3]:
                     if i>game.gamemode[1] or game.gamemode[2]<2:
                        game.AIinfo[6] = list(game.finalseg[3][0+counter:3+counter])
                        game.AIinfo[5]=3
                        break
                     counter+=1
                counter=0
            #win condition
            if len(doiwinseg[3]) == 3 and len(game.player2) == 3:
                game.AIinfo[6] = list(game.finalseg[0])
                game.AIinfo[5] = 3
            ###have to add a rule for trip 2's
    #twopair before boat gamemode[2]=1
    if game.gamemode[0] == 3 and game.gamemode[2] <= 1 or game.gamemode[0] == 0:
        if not game.AIinfo[6]:
            if len(game.finalseg[2]) >= 6 and len(game.finalseg[3]) >= 3:
                for i in valueseg[2]:
                    if i > game.gamemode[1] or game.gamemode[2]<1:
                        game.AIinfo[6]=list(game.finalseg[2][0:2]+game.finalseg[2][0+counter:2+counter])
                        game.AIinfo[5]=4
                        if game.AIinfo[6][0]==game.AIinfo[6][2]:
                            game.AIinfo[6]=game.AIinfo[6]=list(game.finalseg[2][0:4])
                            game.AIinfo[5]=4
                        break
                    counter += 1
                counter = 0
            if len(game.player2)==4 and len(doiwinseg[2])==4:
                game.AIinfo[6]=list(game.player2)
    #exactly two boats gamemode[2]=5
    if game.gamemode[0] == 3 and game.gamemode[2] <= 5 or game.gamemode[0] == 0:
        if not game.AIinfo[6]:
            if len(game.finalseg[2]) >= 2 and len(game.finalseg[3]) >= 3:
                for i in valueseg[3]:
                    if i > game.gamemode[1] or game.gamemode[2]<5:
                        game.AIinfo[6]=list(game.finalseg[2][0:2]+game.finalseg[3][0+counter:3+counter])
                        game.AIinfo[5]=5;break
                    counter += 1
                counter = 0
            ## breaks a trip to play a boat
            if not game.AIinfo[6] and not game.finalseg[2] and len(game.finalseg[3])>=6:
                game.AIinfo[6] = list(game.finalseg[3][0:5])
                game.AIinfo[5]=5
            #win condition set
            if not game.AIinfo[6] and len(game.player2)==5 and len(doiwinseg[2])==2 and len(doiwinseg[3])==3:
                game.AIinfo[6].append(list(game.player2))
                game.AIinfo[5]=5
    #quads
    if game.gamemode[0] == 3 and game.gamemode[2] <= 6 or game.gamemode[0] == 0:
        if len(game.player2)<=11 or len(game.player1)<=7: ##not sure about this number but I don't want to be jamming quads
            if not game.AIinfo[6]:
                if len(game.finalseg[4]) >=4:
                    for i in valueseg[4]:
                        if i > game.gamemode[1] or game.gamemode[2]<6:
                            kicker=0
                            if len(game.finalseg[1])!=0:
                                kicker=str(game.finalseg[1][0])
                            game.AIinfo[6]=list(game.finalseg[4][0:4])
                            if kicker:
                                game.AIinfo[6].append(kicker)
                                game.AIinfo[5]=6
                            break
                        counter += 1
                    counter = 0
                ## chooses a kicker, taking doiwin[0] isn't 100% correct
                if len(game.AIinfo[6])==4:
                    if doiwinseg[1]:
                        kicker=[doiwinseg[1][0]]
                        kicker = [str(a) for a in kicker];kicker= [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in kicker]
                        kicker.append(game.AIinfo[6])
                if len(game.AIinfo[6])==4 and len(game.player2)==5:
                    game.AIinfo[6]=list(game.player2)
    #straightflush
    if game.gamemode[0] == 3 and game.gamemode[2] <= 7 or game.gamemode[0] == 0:
        if not game.AIinfo[6]:
            if len(game.finalseg[7]) >=5:
                for i in valueseg[7]:
                    if i > game.gamemode[1] or game.gamemode[2]<7:
                        game.AIinfo[6]=list(game.finalseg[4][0:5])
                        game.AIinfo[5]=9
                        break
                    counter += 1
            counter = 0

    #normal pairs
    if game.gamemode[0] == 2 or game.gamemode[0] == 0:
        if not game.AIinfo[6] or not game.AIinfo[6] and not game.AIinfo[0] and game.gamemode[0]==0:
            if round(game.gamemode[1])==14:
                twocount=0
                Acount=0
                for i in valueseg[0]:
                    if round(i)==2:
                        twocount+=1
                    if round(i)==14:
                        Acount+=1
                if twocount>=2 and Acount<2:
                    game.AIinfo[6]=[game.finalseg[0][0],game.finalseg[0][1]]
                    game.AIinfo[5]=7
                if len(game.player1)<=3 and Acount>=2 and 14.4 in valueseg[0]:
                    game.AIinfo[6]=[game.finalseg[0][-2],game.finalseg[0][-1]]
                    game.AIinfo[5]=7
            if len(game.finalseg[2]) >= 2 and not game.AIinfo[6]:
                for i in valueseg[2]:
                    if i > game.gamemode[1]:
                        if counter%2==0:
                            game.AIinfo[6]=list(game.finalseg[2][counter:2+counter])
                            game.AIinfo[5]=7
                            break
                        else:
                            game.AIinfo[6] = list(game.finalseg[2][counter-1:+counter+1])
                            game.AIinfo[5]=7
                            break
                    counter += 1
                counter = 0
            if TAK[0]==2 and TAK[2]==2 and len(doiwinseg[2])==6 and len(game.player2)==6:
                game.AIinfo[6].clear()
                game.AIinfo[6].append(doiwinseg[2][2])
                game.AIinfo[6].append(doiwinseg[2][3])
            #covers all playable pairs including 2AK
            if not game.AIinfo[6] and len(game.finalseg[2])!=0:
                game.AIinfo[5]=7
                game=doiwin(doiwinseg,game)

            #playing a high pair to not lose the game
            if game.AIinfo[3] and not game.AIinfo[6]:
                thepair=0
                for i in doiwinseg[2]:
                    if i>game.gamemode[1]:
                        thepair=round(i);
                        break
                for i in doiwinseg[2]:
                    if round(i) == thepair:
                        game.AIinfo[6].append(i)
                if doiwinseg[3]:
                    thepair = 0
                    for i in doiwinseg[3]:
                        if round(i)>game.gamemode[1]:
                            game.AIinfo[6].append(i)
                            if len(game.AIinfo[6])==2:
                                print('test we broke trips')
                                break
                if game.gamemode==[0,0,0]:
                    # we can play whatever we want it isn't worth playing a pair of good cards here
                    print('we choose not to play pair here to not lose')
                    game.AIinfo[6].clear()

            if game.AIinfo[6]:
                game.AIinfo[6] = [str(a) for a in game.AIinfo[6]]
                game.AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in game.AIinfo[6]]
            else:
                game.AIinfo[5]=0
            if game.gamemode[0]==0 and len(game.player2)==2 and doiwinseg[2]:
                game.AIinfo[6]=list(game.player2)
    #singles
    if game.gamemode[0]==1 or game.gamemode[0]==0:
        #standard singles play section
        if not game.AIinfo[6]:
            if len(game.player1)>=len(game.player2) or game.gamemode[0]==0:
                for i in valueseg[1]:
                    if i > game.gamemode[1]:
                        game.AIinfo[6].append(game.finalseg[1][counter])
                        game.AIinfo[5]=8
                        break
                    counter += 1
            else:
                counter=len(valueseg[1])
                for i in reversed (valueseg[1]):
                    counter -= 1
                    if i > game.gamemode[1]:
                        game.AIinfo[6].append(game.finalseg[1][counter])
                        game.AIinfo[5]=8
                        break
                    counter -= 1
            counter=0
            pairstrips=list(valueseg[2])+list(valueseg[3])
            pairstrips.sort()
            ##if we are just jamming singles we don't care about our pairs trips and play singles for gamemode[0]=0
            if game.gamemode[0]==0 and pairstrips and not game.AIinfo[6]:
                game.AIinfo[6].append(pairstrips[0])
                game.AIinfo[5]=8
            if game.gamemode[0]==1 and pairstrips and not game.AIinfo[6]:
                if game.gamemode[1]<pairstrips[-1]:
                    game.AIinfo[6].append(pairstrips[-1])
                    game.AIinfo[5]=8

            if round(game.gamemode[1])==14:
                #we're in trouble and need to play hard to not lose
                if game.AIinfo[3]==True or len(game.player2)>=len(game.player1):
                    for i in valueseg[0]:
                        if i > game.gamemode[1]:
                            game.AIinfo[6].append(i)
                            game.AIinfo[5]=8
                            break
                    if not game.AIinfo[6]:
                        for i in reversed(valueseg[0]):
                            if round(i)==2:
                                game.AIinfo[6].append(i)
                                game.AIinfo[5]=8
                                break

                ## here we're not in trouble and can make the value play
                else:
                    for i in valueseg[0]:
                        if round(i)==2:
                            game.AIinfo[6].append(i)
                            game.AIinfo[5]=8
                            break
                    if not game.AIinfo[6]:
                        for i in valueseg[0]:
                            if i > game.gamemode[1]:
                                game.AIinfo[6].append(i)
                                game.AIinfo[5]=8
                                break

            ## uses 2's in singles if 2's are useless
            if TAK[1]==0 and len(pairstrips)==0 and valueseg[1]==1 and TAK[0] !=0 and TAK[2]!=0 and game.AIinfo[6]:
                if TAK[0]>=2 and TAK[2] >=2:
                    game.AIinfo[6].clear()
                    game.AIinfo[6].append(valueseg[0])

            #deletes play if we can't make a standard play so that we can go harder to not lose
            acestwos=0
            playablesingles=list(valueseg[1])+list(valueseg[2])+list(valueseg[3])
            playablesingles.sort()
            if TAK[0]+TAK[2]>4:
                acestwos=4
            else:
                acestwos=int(TAK[0])+int(TAK[2])
            #gear switch AI will only play high cards
            if playablesingles:
                if acestwos+TAK[1]<len(game.player1) and playablesingles[-1] > game.gamemode[1] and game.gamemode[0] !=0:
                    game.AIinfo[6].clear()
                    game.AIinfo[6].append(playablesingles[-1])
            if game.AIinfo[3] and game.gamemode[0]!=0:
                if TAK[2]:
                    if round(game.gamemode[1])!=2:
                        game.AIinfo[6].clear()
                if TAK[1]:
                    game.AIinfo[6].clear()

            #make a function to get rid of excess 2's maybe at 5 cards or len(valueseg[0])==4/[1] ==1
            if len(game.player2) == 3 and '2s' in game.player2 and game.gamemode[0]==0:
                for i in game.player2:
                    if i != '2s':
                        game.AIinfo[6].clear()
                        game.AIinfo[6].append(i)
                        break

            if len(game.player2) == 3 and 'As' in game.player2 and game.gamemode[0]==0:
                game.AIinfo[6].clear()
                game.AIinfo[6].append(game.player2[0])

            #converter
            if not type(game.AIinfo[6])== str and game.AIinfo[6]:
                game.AIinfo[6][0] = str(game.AIinfo[6][0])
                game.AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in game.AIinfo[6]]
            if not game.AIinfo[6] and game.finalseg[0]:
                #adds quad 2ak into the cards playable in singles
                if valueseg[4]:
                    for i in valueseg[4]: ###have to add quad 2ak here just don't know how I should do it
                        if round(i)==14 or round(i)==13 or round(i)==2:
                            valueseg[0].append(i)
                # this is if no outliers and all we have is 2ak and we lead
                if game.gamemode[0]==0:
                    if TAK[0]>=TAK[1] and TAK[0]>=TAK[2]:
                        game.AIinfo[6].append(game.finalseg[0][0])
                        game.AIinfo[5]=8
                    if TAK[1]>TAK[0] and TAK[1]>=TAK[2] and not game.AIinfo[6]:
                        for i in game.finalseg[0]:
                            if i[:-1]=='13':
                                game.AIinfo[6].append(game.finalseg[0][counter])
                                game.AIinfo[5]=8
                                break
                            counter+=1
                    if TAK[2]>TAK[0] and TAK[2]>TAK[1] and not game.AIinfo[6]:
                        for i in game.finalseg[0]:
                            if i[:-1]=='14':
                                game.AIinfo[6].append(game.finalseg[0][counter])
                                game.AIinfo[5]=8
                                break
                            counter+=1
                #this is no outliers and we don't lead
                if game.gamemode[0]==1:
                    if round(game.gamemode[1])==14 and TAK[0]>=1:
                        if TAK[0]>=2 and len (game.player1)<=3:
                            game.AIinfo[6].append(game.finalseg[0][TAK[0]-1])
                            game.AIinfo[5] = 8
                        else:
                            game.AIinfo[6].append(game.finalseg[0][0])
                            game.AIinfo[5]=8


                    if not game.AIinfo[6]:
                        print('we should play 2ak here')
                        Ks=False
                        if len (game.player1) <=2 and len(game.player2)>len(game.player1):
                            print('scared mode')
                            for i in reversed(valueseg[0]):
                                if game.gamemode[1] < i:
                                    if i==13.4:
                                        Ks=True
                                        continue
                                    if round(game.gamemode[1])==2 and round(i)==14:
                                        continue

                                    else:
                                        game.AIinfo[6].append(i)
                                        game.AIinfo[5]=8
                                        break
                        else:
                            print('value mode')
                            for i in valueseg[0]:
                                if game.gamemode[1] < i:
                                    if i==13.4:
                                        Ks=True
                                        print('skip Ks2')
                                        continue
                                    if round(game.gamemode[1])==2 and round(i)==14:
                                        break
                                    else:
                                        game.AIinfo[6].append(i)
                                        game.AIinfo[5]=8
                                        break

                        #play Ks over As
                        if Ks and game.AIinfo[6]:
                            if game.AIinfo[6]==14.4:
                                if game.gamemode[1]<13.4:
                                    game.AIinfo[6]=[13.4]

                        #play Ks if we have nothing
                        if Ks and not game.AIinfo[6] and game.gamemode[1]<13.4:
                            game.AIinfo[6]=[13.4]

                        #play Ks when they have 2 or less cards
                        if Ks and game.AIinfo[6] and len(game.player1)<=2:
                            if game.AIinfo[6][0]!=14.4:
                                game.AIinfo[6]=[13.4]

                        ##add 3 card win cons here
                        #adjust if they have 3 or less, and adjust to be able play A on A
                        game.AIinfo[6] = [str(a) for a in game.AIinfo[6]]
                        game.AIinfo[6] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's')for word in game.AIinfo[6]]
    if game.AIinfo[6]:
        if type(game.AIinfo[6][0])==list:
            game.AIinfo[6]=game.AIinfo[6][0]
    game.AIinfo[6]=basic.sort(game.AIinfo[6])
    return game

def doiwin(doiwinseg,game):
    #you get basically 4 free poker hands if they have less than 4 cards
    counter=0
    pairstotest=[]
    pair=[]
    strongpokerhand=False
    for i in doiwinseg[3]:
        if i>11 and doiwinseg[2] or i>11 and len(doiwinseg[3])>3:
            game.AIinfo[7]=True
    for i in doiwinseg[2]:
        if 13<i<14.5:
            pair.append(i)
            if len(pair)==2:
                pairstotest.append(pair)
                pair=[]
    #if we have a trips we aren't afraid of having an extra pair
    if game.AIinfo[2]==True or strongpokerhand==True:
        for i in pairstotest:
            backupcopy = copy.deepcopy(doiwinseg)
            for k in pairstotest[counter]:
                if k in doiwinseg[2]:doiwinseg[2].remove(k)
                if k in doiwinseg[1]:doiwinseg[1].remove(k)
                if k in doiwinseg[3]:doiwinseg[3].remove(k)
            if doiwinseg[3]:
                doiwinseg[2].clear()
            therest=doiwinseg[1]+doiwinseg[2]
            if 14.4 in therest and len(therest)<=4+len(doiwinseg[4]):
                if 14.3 or 14.2 in therest:
                    if 2.4 in therest:
                        game.AIinfo[5]=9
                        game.AIinfo[6]=pairstotest[counter]
                        return game
                    badtwos=0
                    for j in therest:
                        if j==2.1 or j==2.2 or j==2.3:badtwos+=1
                    badtwos=badtwos-len(doiwinseg[4])
                    if badtwos<=1:
                        game.AIinfo[5]=9
                        game.AIinfo[6]=pairstotest[counter]
                        return game
            if 14.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                badtwos=0
                for j in therest:
                    if j == 2.1 or j == 2.2 or j == 2.3:
                        badtwos += 1
                badtwos = badtwos - len(doiwinseg[4])
                if 14.1 or 14.2 or 14.3 in therest:
                    badtwos+=1
                if badtwos <= 1:
                    game.AIinfo[5]=9
                    game.AIinfo[6]=pairstotest[counter]
                    return game
            if 13.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                for i in therest:
                    if round(i)==2:
                        game.AIinfo[5]=9
                        game.AIinfo[6]=pairstotest[counter]
                        return game
            if 2.4 in therest and len(therest)<=3+len(doiwinseg[4]):
                for i in therest:
                    if round(i)==14:
                        game.AIinfo[5]=9
                        game.AIinfo[6]=pairstotest[counter]
                        return game
            if game.AIinfo[4] >=2:
                game.AIinfo[5]=9
                game.AIinfo[6]=pairstotest[counter]
                return game
            counter+=1
            doiwinseg = copy.deepcopy(backupcopy)
    return game

def AIdraw(game):
    plainnumseg=[[],[],[]]
    draws=[];newgamemode=[]
    #for pile maybe above an 8 outlier draw it
    #pile draw if they have =<4 cards and you have 2 outliers pile draw one of them if possible
    #draw pair less then 6 cards keep it
    #less then 5 cards draw 1
    #drawing a 2 good if #A+#2 < 3
    if game.AIinfo[6]:
        game.fplay=list(game.AIinfo[6])  #after this is old spot for log add
        # add to log for undo
        game.log.append(list(game.AIinfo[6]))
        game.log.append(list(game.main))
        game.log.append(list(game.gamemode))
        game.log.append(7)
        newgamemode.append(game.AIinfo[6][-1])
        newgamemode = [word.replace('d', '.1').replace('c', '.2').replace('h', '.3').replace('s', '.4') for word in newgamemode]
        newgamemode= [float(a) for a in newgamemode]
        if len(game.AIinfo[6])==1:
            game.gamemode[0]=1
        if len(game.AIinfo[6]) == 2:
            game.gamemode[0] = 2
        if len(game.AIinfo[6]) >=3:
            game.gamemode[0] = 3

            #this part uses the number found from AIinfo[5] to determine what poker hand it is and then set the new gamemode to that
            if game.AIinfo[5]==9:
                game.gamemode[2]=7
            if game.AIinfo[5] == 6:
                game.gamemode[2] = 6
            if game.AIinfo[5] == 5:
                game.gamemode[2] = 5
            if game.AIinfo[5] == 4:
                game.gamemode[2] = 1
            if game.AIinfo[5] == 3:
                game.gamemode[2] = 2
            if game.AIinfo[5] == 1:
                game.gamemode[2] = 3
            if game.AIinfo[5] == 2:
                game.gamemode[2] = 4
        game.main=[1,2]
        if game.AIinfo[5]==5: #should do 2 high flush/straight eventually
            game.gamemode[1]=float(game.AIinfo[6][2][:-1])
        elif game.AIinfo[5]==6:
            game.gamemode[1]=float(game.AIinfo[6][3][:-1])
        else:
            game.gamemode[1]=float(newgamemode[-1])
        if len(game.AIinfo[6])!=0:
            for i in game.AIinfo[6]:
                game.player2.remove(i)
                game.used.append(i)

        #hotfix for making straight flush work
        if game.gamemode[2]==4:
            if int(game.AIinfo[6][0][:-1])+1==int(game.AIinfo[6][1][:-1]) and int(game.AIinfo[6][1][:-1])+1==int(game.AIinfo[6][2][:-1]) and \
                    int(game.AIinfo[6][2][:-1])+1==int(game.AIinfo[6][3][:-1]) and int(game.AIinfo[6][3][:-1])+1==int(game.AIinfo[6][4][:-1]):
                game.gamemode[2]=7
        game.AIinfo[5] = 0


        return game
    game.showlast=[]
    game.showlast=list(game.showthis)
    game.showthis=[]
    game.play.clear()
    game.play2.clear()
    game.fplay.clear()
    game.AIinfo[5]=0
    for i in game.finalseg[1]:
        plainnumseg[0].append(i[:-1])
    plainnumseg[0] = [int(a) for a in plainnumseg[0]]
    for i in game.finalseg[2]:
        plainnumseg[1].append(i[:-1])
    plainnumseg[1] = [int(a) for a in plainnumseg[1]]
    for i in game.finalseg[3]:
        plainnumseg[2].append(i[:-1])
    plainnumseg[2] = [int(a) for a in plainnumseg[2]]
    for i in game.pile:
        pass #do this later
    draw=[]
    if int(game.deck[0][:-1]) in plainnumseg[0] or int(game.deck[0][:-1]) in plainnumseg[2] or game.deck[0][:-1]=='13' or game.deck[0][:-1]=='14'or len(game.player2)<=4:
        #AI 7 play 8 AI draw 9 AI pile
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.log.append(list(draw))
        game.log.append(list(game.main))
        game.log.append(list(game.gamemode))
        game.log.append(8)
        game.main=[1,1]
        game.gamemode=[0,0,0]
        return game

    if int(game.deck[0][:-1]) in plainnumseg[0] or int(game.deck[0][:-1]) in plainnumseg[2] or game.deck[1][:-1] == '13' or game.deck[1][:-1] == '14' or game.deck[1][:-1]==game.deck[0][:-1]:
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.log.append(list(draw))
        game.log.append(list(game.main))
        game.log.append(list(game.gamemode))
        game.log.append(8)
        game.main=[1,1]
        game.gamemode=[0,0,0]
        return game

    if game.p2redraw:
        game.pile.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.pile.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.log.append(list(draw))
        game.log.append(list(game.main))
        game.log.append(list(game.gamemode))
        game.log.append(8)
        game.main=[1,1]
        game.gamemode=[0,0,0]
        game.p2redraw=False
        return game
    if len(game.player2)>=4:
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.log.append(list(draw))
        game.log.append(list(game.main))
        game.log.append(list(game.gamemode))
        game.log.append(8)
        game.main=[1,1]
        game.gamemode=[0,0,0]
        return game
    else:
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.player2.append(game.deck[0])
        draw.append(game.deck[0])
        game.deck.pop(0)
        game.log.append(list(draw))
        game.log.append(list(game.main))
        game.log.append(list(game.gamemode))
        log.append(8)
        game.main=[1,1]
        game.gamemode=[0,0,0]
        return game
    return game

def AImove(screen,game):
    if game.main[0] == 1:
        return
    if len(game.player1)<=2:
        game.AIinfo[3]=True
    else:
        game.AIinfo[3]=False
    if len(game.player1)<=4:
        game.AIinfo[2]=True
    if len(game.player1)>=9 and game.AIinfo[2]==True:
        game.AIinfo[2]=False
    if game.finalseg[4]:
        game.AIinfo[7]=True
    if game.finalseg[7]:
        game.AIinfo[7]=True
    game=coveragefinder(game)
    game=AIflushstraight(game)
    game=AIFullhHouseQuadsTwoPair(game)
    #AIdraw
    game=AIdraw(game)
    game.AIinfo[6].clear()
    game.player2=basic.sort(game.player2)
    game.play2.clear()
    game=display.redrawgamewindow(screen,game)
    return game
###AIinfo= [[0]coverage jam singles,[1]extra 2's,[2]opponent had less than 4 cards,[3]opponent had 2 cards, [4]coverage#,[5]what poker hand we added,[6]the play,[7]strongpokerhand]