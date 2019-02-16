#oxo game is project from 'python projects' by Laura Cassell and Alan Gauld


import os.path
game_file = ".oxogame.dat"


def _getPath():
    #get path, returns a valid path for data file. 
    #tries to use home folder, default to cwd
    
    try:
        game_path = os.environ['HOMEPATH'] or os.environ['HOME']
        if not os.path.exists(game_path):
            game_path = os.getcwd()
    except (KeyError, TypeError):
        game_path = os.getcwd()
    return game_path


def saveGame(game):
    # save game object to data file
    
    path = os.path.join(_getPath(), game_file)
    with open(path, 'w',) as gf:
        gamestr = ''.join(game)
        gf.write(gamestr)
        
        
def restoreGame():
    #restores game from data file, 
    #game object is a list of characters
    
    path = os.path.join(_getPath(), game_file)
    with open(path) as gf:
        gamestr = gf.read()
        return list(gamestr)
    
    
def test():
    print("Path = ", _getPath())
    saveGame(list("XO  XO XO"))
    print(restoreGame())
    
    
if __name__ == "__main__": test()

    

    