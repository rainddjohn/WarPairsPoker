import mulligan as mull
class gamerinfo():
    player1=[ '13s']
    player2=['3d', '3h', '4h', '5h', '6d', '7s', '9d', '9s', '11c', '13d', '13c', '13h']
    play=[]
    play2=[]
    fplay=[]
    pile=[]
    main=[0,0]
    gamemode=[]
    deck=[]
    backupmain=[0]
    showthis=[]
    showlast=[]
    optionslist=[0,0,0,0,0,0]
    used=[]
    log=[]
    backupdeck = []
    automull = True
    concede=False
    altreveal=False
    replay=False
    AI=False
    p1redraw = True
    p2redraw = True
    n2akout = []
    hardmull = []
    mullnotes = []
    outliers = []
    quads = []
    mull = []
    segp2 = [[], [], [], [], [], [], [], [], []]
    copyseg = []
    finalseg = []
    p2copy = []
    lastmouse1 = [0, 0]
    AIinfo = [False, False, False, False, False, 0, [], False]
    background_color = (84, 119, 44)
    hand = []




tis=gamerinfo()
tis=mull.mulligan(tis)
print(tis.play2)

