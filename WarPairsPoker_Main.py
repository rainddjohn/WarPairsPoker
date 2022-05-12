import basic as basic
import display as display
import buttons as buttons
import pygame

#variables needed for pygame
pygame.init()
(width,height)=(1033,750)
background_color= (84,119,44)
screen=pygame.display.set_mode((width,height))
screen.fill(background_color)
pygame.display.set_caption('WarPairsPoker v3')
pygame.display.update()

class gameinfo():
    player1=[]
    player2=[]
    play=[]
    play2=[]
    fplay=[]
    pile=[]
    main=[0,0]
    gamemode=[0,0,0]
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
    AI=True
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
    showtop= True

game=gameinfo()
game=basic.startgame(screen,game)
game=display.redrawgamewindow(screen,game)
pygame.display.flip()

running= True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            game=buttons.buttons(mouse,screen,game)

        ####hotkey code
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                mouse = [120, 323]
                if game.main == [-3, 0]:
                    mouse = [450, 90]
                if game.main == [-2, 0]:
                    mouse = [450, 520]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_q:
                if game.main[0] == 1: mouse = [55, 645]
                if game.main[0] == 2: mouse = [55, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_w:
                if game.main[0] == 1: mouse = [130, 645]
                if game.main[0] == 2: mouse = [130, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_e:
                if game.main[0] == 1: mouse = [205, 645]
                if game.main[0] == 2: mouse = [205, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_r:
                if game.main[0] == 1: mouse = [280, 645]
                if game.main[0] == 2: mouse = [280, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_t:
                if game.main[0] == 1: mouse = [355, 645]
                if game.main[0] == 2: mouse = [355, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_y:
                if game.main[0] == 1: mouse = [430, 645]
                if game.main[0] == 2: mouse = [430, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_u:
                if game.main[0] == 1: mouse = [505, 645]
                if game.main[0] == 2: mouse = [505, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_i:
                if game.main[0] == 1: mouse = [580, 645]
                if game.main[0] == 2: mouse = [580, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_o:
                if game.main[0] == 1: mouse = [655, 645]
                if game.main[0] == 2: mouse = [655, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_p:
                if game.main[0] == 1: mouse = [730, 645]
                if game.main[0] == 2: mouse = [730, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_LEFTBRACKET:
                if game.main[0] == 1: mouse = [805, 645]
                if game.main[0] == 2: mouse = [805, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_RIGHTBRACKET:
                if game.main[0] == 1: mouse = [880, 645]
                if game.main[0] == 2: mouse = [880, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_BACKSLASH:
                if game.main[0] == 1: mouse = [955, 645]
                if game.main[0] == 2: mouse = [955, 188]
                mouse = list(mouse)
                game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_1:
                if game.main[0] == 1:
                    mouse = [55, 490]
                if game.main[0] == 2:
                    mouse = [55, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 30]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_2:
                if game.main[0] == 1:
                    mouse = [135, 490]
                if game.main[0] == 2:
                    mouse = [135, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 90]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_3:
                if game.main[0] == 1:
                    mouse = [205, 490]
                if game.main[0] == 2:
                    mouse = [205, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 150]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_4:
                if game.main[0] == 1:
                    mouse = [280, 490]
                if game.main[0] == 2:
                    mouse = [280, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 210]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_5:
                if game.main[0] == 1:
                    mouse = [355, 490]
                if game.main[0] == 2:
                    mouse = [355, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 270]
                mouse = list(mouse)

                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_6:
                if game.main[0] == 1:
                    mouse = [430, 490]
                if game.main[0] == 2:
                    mouse = [430, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 330]
                mouse = list(mouse)

                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_7:
                if game.main[0] == 1:
                    mouse = [505, 490]
                if game.main[0] == 2:
                    mouse = [505, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 390]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_8:
                if game.main[0] == 1:
                    mouse = [580, 490]
                if game.main[0] == 2:
                    mouse = [580, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 450]
                mouse = list(mouse)

                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_9:
                if game.main[0] == 1:
                    mouse = [655, 490]
                if game.main[0] == 2:
                    mouse = [655, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 510]
                mouse = list(mouse)

                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_0:
                if game.main[0] == 1:
                    mouse = [730, 490]
                if game.main[0] == 2:
                    mouse = [730, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 570]
                mouse = list(mouse)

                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_MINUS:
                if game.main[0] == 1:
                    mouse = [805, 490]
                if game.main[0] == 2:
                    mouse = [805, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 630]
                mouse = list(mouse)

                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_EQUALS:
                if game.main[0] == 1:
                    mouse = [880, 490]
                if game.main[0] == 2:
                    mouse = [880, 60]
                if game.main == [-3, -3]:
                    mouse = [20, 690]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_BACKSPACE:
                if game.main[0] == 1:
                    mouse = [955, 490]
                if game.main[0] == 2:
                    mouse = [955, 60]
                mouse = list(mouse)
                if game.main != [-3, -3]:
                    game.lastmouse1 = list(mouse)
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_SPACE:
                mouse = [650, 350]
                game=buttons.buttons(mouse,screen,game)
            if event.key == pygame.K_RALT:
                mouse = [650, 300]
                game=buttons.buttons(mouse,screen,game)
            if event.key == pygame.K_TAB:
                mouse = [20, 350]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_LEFT:
                if game.main[0] == 1:
                    backupplay = len(game.play)
                    backup = list(game.lastmouse1)
                    game.lastmouse1[0] = game.lastmouse1[0] - 75
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)

                    if backupplay > len(game.play):
                        game=buttons.buttons(mouse,screen,game)
                    backupplay = len(game.play)
                    mouse = list(backup)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay < len(game.play):
                        game=buttons.buttons(mouse,screen,game)

                if game.main[0] == 2:
                    backupplay = len(game.play2)
                    backup = list(game.lastmouse1)
                    game.lastmouse1[0] = game.lastmouse1[0] - 75
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)

                    if backupplay > len(game.play2):
                        game=buttons.buttons(mouse,screen,game)
                    backupplay = len(game.play2)
                    mouse = list(backup)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay < len(game.game.play2):
                        game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_RIGHT:
                if game.main[0] == 1:
                    backupplay = len(game.play)
                    backup = list(game.lastmouse1)
                    game.lastmouse1[0] = game.lastmouse1[0] + 75
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)

                    if backupplay > len(game.play):
                        game=buttons.buttons(mouse,screen,game)
                    backupplay = len(game.play)
                    mouse = list(backup)
                    game=buttons.buttons(mouse,screen,game)

                    if backupplay < len(game.play):
                        game=buttons.buttons(mouse,screen,game)
                if game.main[0] == 2:
                    backupplay = len(game.play2)
                    backup = list(game.lastmouse1)
                    game.lastmouse1[0] = game.lastmouse1[0] + 75
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)

                    if backupplay > len(game.play2):
                        game=buttons.buttons(mouse,screen,game)
                    backupplay = len(game.play2)
                    mouse = list(backup)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay < len(game.game.play2):
                        game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F1:
                mouse = [751, 280]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F2:
                mouse = [788, 280]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F3:
                mouse = [825, 280]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F4:
                mouse = [865, 280]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F5:
                mouse = [910, 280]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F6:
                mouse = [950, 280]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F7:
                mouse = [751, 310]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F8:
                mouse = [788, 310]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F9:
                mouse = [825, 310]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F10:
                mouse = [865, 310]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F11:
                mouse = [910, 310]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_F12:
                mouse = [950, 310]
                game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_UP:
                if game.main[0] == 1:
                    backupplay = len(game.play)
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay > len(game.play):
                        game=buttons.buttons(mouse,screen,game)

                if game.main[0] == 2:
                    backupplay = len(game.play2)
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay > len(game.game.play2):
                        game=buttons.buttons(mouse,screen,game)

            if event.key == pygame.K_DOWN:
                if game.main[0] == 1:
                    backupplay = len(game.play)
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay < len(game.play):
                        game=buttons.buttons(mouse,screen,game)
                if game.main[0] == 2:
                    backupplay = len(game.play2)
                    mouse = list(game.lastmouse1)
                    game=buttons.buttons(mouse,screen,game)
                    if backupplay < len(game.play2):
                        game=buttons.buttons(mouse,screen,game)

        mouse = pygame.mouse.get_pos()