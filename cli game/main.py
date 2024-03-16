import keyboard
import time
import numpy as np
import sys







################################################################

### deal with highscore values and file ###


def get_highscore():
    # exampple call is highscore = get_highscore()
    with open('cli game/highscore.txt', 'r', encoding='utf-8') as f:
        highscore = f.read()
    return highscore

def write_highscore(new_highscore):
    with open('cli game/highscore.txt', 'w', encoding='utf-8') as f:
        f.write(new_highscore)

# will implement potenial users so this will need to be rewriten


################################################################


### generate enimies ###
        
def generate_enemy():
    random_num = np.random.randint(1, 5)
    if random_num == 1:
        tl = 0 # top left
        tm = 1 # top middle
        tr = 1 # to right
        ml = 0 # mid left
        mm = 1 # mid mid
        mr = 1 # mid right
        bl = 0 # botton left
        bm = 0 # bottom middle
        br = 0 # bottom right
    elif random_num == 2:
        tl = 0 # top left
        tm = 1 # top middle
        tr = 0 # to right
        ml = 1 # mid left
        mm = 1 # mid mid
        mr = 1 # mid right
        bl = 0 # botton left
        bm = 1 # bottom middle
        br = 0 # bottom right
    elif random_num == 3:
        tl = 1 # top left
        tm = 1 # top middle
        tr = 1 # to right
        ml = 1 # mid left
        mm = 1 # mid mid
        mr = 1 # mid right
        bl = 0 # botton left
        bm = 0 # bottom middle
        br = 0 # bottom right
    elif random_num == 4:
        tl = 0 # top left
        tm = 1 # top middle
        tr = 1 # to right
        ml = 1 # mid left
        mm = 1 # mid mid
        mr = 1 # mid right
        bl = 0 # botton left
        bm = 1 # bottom middle
        br = 1 # bottom right
    else:
        tl = 0 # top left
        tm = 0 # top middle
        tr = 1 # to right
        ml = 0 # mid left
        mm = 1 # mid mid
        mr = 1 # mid right
        bl = 0 # botton left
        bm = 0 # bottom middle
        br = 1 # bottom right
    return tl, tm, tr, ml, mm, mr, bl, br, bm

def place_enemy():
    tl, tm, tr, ml, mm, mr, bl, br, bm = generate_enemy()

    # middle middle always has to be true
     







































class mainmenu:
    def __init__(self):
        self.highscore = get_highscore()

    def __str__(self):
        'loop for the main menu'

    def display(self, highscore):
        print('Welcome to thunderstruck. the best game ever')
        print(f'the current highscore is {highscore}')
        print('press p to play')
        print('a to see analytics')
        print('Press q to quit')
        menu_input = input('enter your choice >> ')
        if menu_input.lower() == 'p':
            #game_intro() # this will include call to main class
            pass
        elif menu_input.lower() == 'a':
            pass
            # this will have a section to show data i have collected
        elif menu_input.lower() == 'q':
            sys.exit()
        else:
            mainmenu.display(self, highscore)




class gameloop: # every second it runs until 10 score hit then 0.7 at 20 it is 0.3. 
    def __init__(self):
        pass



    def __str__(self) -> str:
        'this will be the main game loop. tps'







if __name__ == '__main__':
    
    
    ################################################################
    board = np.empty([10, 25])
    playerY = 5
    playerX = 1
    enemies = []


    ################################################################


    while gamestate == True:
        time.sleep(0.5)
        # here i will run the case called gameloop.