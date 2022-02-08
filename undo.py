import basic as basic;import display as display

def undo(log, main, pile, player1, player2, showthis, showlast, p1redraw, p2redraw, fplay, gamemode, backupmain,deck,play,play2,used,background_color,altreveal, screen,lastmouse1, AI, concede):
    x=0
    #every event is added here as [cards used,main,gamemode,type of action]; types of action: -1,-2 mulligans, 1 play, 2 draw, 3 redraw, 4 is pass turn, 5 is pile, 6 is change of turn
    #AI 7 play 8 AI draw 9 AI pile
    if len(log)==0:
        main=list(backupmain)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
        return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    play.clear();play2.clear()
    if log[-1]==-1:
        main=log[-3]
        while x < len(log[-4]):
            player1.append(log[-4][x]);pile.remove(log[-4][x]);x += 1
        main=list(log[-3]);fplay=updatefplay(log,main,fplay);player1=basic.sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=[0,0,0]
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
        return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==-2:
        main=log[-3]
        while x < len(log[-4]):
            player2.append(log[-4][x]);pile.remove(log[-4][x]);x += 1
        main=list(log[-3]);fplay=updatefplay(log,main,fplay);player2=basic.sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=[0,0,0]
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
        return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==1:
        while x < len(log[-4]):
            log[-4][x] = str(log[-4][x]);x += 1
        log[-4] = [word.replace('.1', 'd').replace('.2', 'c').replace('.3', 'h').replace('.4', 's') for word in log[-4]]
        if log[-3][0]==1:
            x=0
            while x<len(log[-4]):
                player1.append(log[-4][x]);used.remove(log[-4][x])
                if log[-4][x] in showthis:
                    showthis.remove(log[-4][x])
                x+=1
            main=log[-3];fplay=updatefplay(log,main,fplay);player1 = basic.sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
            if main[1]==1:gamemode=list([0,0,0])
            else: gamemode=list(log[-2])
            main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                     lastmouse1, pile,
                                     p1redraw, p2redraw, AI, concede, backupmain)
            return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
        if log[-3][0]==2:
            x=0
            while x < len(log[-4]):
                player2.append(log[-4][x]);used.remove(log[-4][x])
                if log[-4][x] in showthis:
                    showthis.remove(log[-4][x])
                x+=1
            main=log[-3];fplay=updatefplay(log,main,fplay);player2 = basic.sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
            if main[1]==1:gamemode=list([0,0,0])
            else: gamemode=list(log[-2])
            main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                     lastmouse1, pile,
                                     p1redraw, p2redraw, AI, concede, backupmain)
            return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==2:
        if log[-3][0] == 1:
            main=log[-3];fplay=updatefplay(log,main,fplay);player1.remove(log[-4]);deck.insert(0,log[-4]);player1 = basic.sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=list(log[-2])
            main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                     lastmouse1, pile,
                                     p1redraw, p2redraw, AI, concede, backupmain)
            return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
        if log[-3][0] == 2:
            main=log[-3];fplay=updatefplay(log,main,fplay);player2.remove(log[-4]);deck.insert(0,log[-4]);player2 = basic.sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1);gamemode=list(log[-2])
            main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
            player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                     lastmouse1, pile,
                                     p1redraw, p2redraw, AI, concede, backupmain)
            return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==3:
        if log[-3][0] == 1:
            if log[-3][1] == 3:
                p1redraw = True;player1.remove(log[-4][1]);player1.append(log[-4][0]);pile.remove(log[-4][0])
                main = log[-3];fplay=updatefplay(log,main,fplay);player1 = basic.sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
                main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile,
                                         p1redraw, p2redraw, AI, concede, backupmain)
                return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
            if log[-3][1]==4:
                p1redraw=True
                player1.remove(log[-4][2]);player1.remove(log[-4][3]);player1.append(log[-4][0]);player1.append(log[-4][1]);pile.remove(log[-4][0]);pile.remove(log[-4][1])
                main=log[-3];fplay=updatefplay(log,main,fplay);player1 = basic.sort(player1);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
                main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile,
                                         p1redraw, p2redraw, AI, concede, backupmain)
                return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
        if log[-3][0] == 2:
            if log[-3][1] == 3:
                p2redraw = True;player2.remove(log[-4][1]);player2.append(log[-4][0]);pile.remove(log[-4][0])
                main = log[-3];fplay=updatefplay(log,main,fplay);player2 = basic.sort(player2);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
                main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile,
                                         p1redraw, p2redraw, AI, concede, backupmain)
                return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
            if log[-3][1] == 4:
                p2redraw = True
                player2.remove(log[-4][2]);player2.remove(log[-4][3]);player2.append(log[-4][0]);player2.append(log[-4][1]);pile.remove(log[-4][0]);pile.remove(log[-4][1])
                main=log[-3];fplay=updatefplay(log,main,fplay);player2 = basic.sort(player2);log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1)
                main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
                player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay,
                                         background_color,
                                         lastmouse1, pile,
                                         p1redraw, p2redraw, AI, concede, backupmain)
                return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==4:
        main=log[-3];fplay=updatefplay(log,main,fplay);log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1)
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
        return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==5:
        if log[-3][0]==1:
            player1.remove(log[-4]);pile.append(log[-4])
        if log[-3][0]==2:
            player2.remove(log[-4]);pile.append(log[-4])
        main = log[-3];fplay=updatefplay(log,main,fplay);log.pop(-1);log.pop(-1);log.pop(-1);log.pop(-1)
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
        return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==6:
        gamemode=list(log[-2]);main=log[-3];fplay=updatefplay(log,main,fplay);log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1)
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
        if log[-1]==5:
            main, gamemode, log, pile, deck, fplay, showthis, showlast, used, p1redraw, p2redraw, player1, player2= \
                undo(log, main, pile, player1, player2, showthis, showlast, p1redraw, p2redraw, fplay, gamemode,
                     backupmain,deck,play,play2,used,background_color,altreveal, screen,lastmouse1, AI, concede)
        return main, gamemode, log,pile, deck,fplay,showthis,showlast,used,p1redraw,p2redraw,player1,player2
    if log[-1]==7:
        if type(log[-4])==str:player2.append(i)
        else:
            for i in log[-4]:
                player2.append(i)
                if i in used:
                    used.remove(i)
                if i in showthis:
                    showthis.remove(i) ##show this/used remove(i)
        fplay=list(log[-4]);player2=basic.sort(player2);gamemode=list(log[-2]);main=log[-3];fplay=updatefplay(log,main,fplay);log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1)
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
    if log[-1]==8:
        if len(log[-4])<3:
            for i in reversed(log[-4]): deck.insert(0,i);player2.remove(i)
        if len(log[-4])==4:
            counter=0
            for i in reversed(log[-4]):
                deck.insert(0,i)
                if counter<=1:player2.remove(i)
                if counter>=2:pile.remove(i)
                counter+=1
        p2redraw=True;player2 = basic.sort(player2); gamemode = list(log[-2]);main=log[-3];fplay=updatefplay(log,main,fplay);log.pop(-1);log.pop(-1); log.pop(-1);log.pop(-1)
        main,log,pile=basic.seewhogoesfirst(main,log,pile,player1,player2)
        player1, player2,main=display.redrawgamewindow(player1, player2, main, altreveal, screen, play, play2, fplay, background_color,
                                 lastmouse1, pile,
                                 p1redraw, p2redraw, AI, concede, backupmain)
    return main, gamemode, log,pile, deck, fplay, showthis, showlast, used, p1redraw, p2redraw, player1, player2
        
def updatefplay(log,main,fplay):
    x = 1
    #updates fplay when the undo button is used, needs to be fixed
    if main[1]==1: fplay=[];return fplay
    while len(log)>1+(x*4):   ### not sure about this one
        if log[-1+(x*-4)]==1:
            if log[-3][1]==2: fplay=list(log[-4+(x*-4)]);return fplay
            else: return fplay
        else:x += 1
    fplay=[]
    return fplay