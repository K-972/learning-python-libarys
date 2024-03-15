import numpy as np



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









































board = np.empty([10, 15])


class mainmenu:
    def __init__(self):
        self.highscore = highscore

    def __str__(self):
        'loop for the main menu'

    def display(self, highscore):
        print('Welcome to thunderstruck. the best game ever')
        print(f'the current highscore is {highscore}')



class gameloop:
    def __init__(self):
        pass



    def __str__(self) -> str:
        'this will be the main game loop. tps'







if __name__ == '__main__':
    
    
    ################################################################
    playerY = 5
    playerX = 1


    