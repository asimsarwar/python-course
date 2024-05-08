class Remote():
    def isLeftPressed(self):
        return True

class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        print('Yahooo!')

    def moveTop(self):
        pass

remote1 = Remote()
player1 = Player()

if(remote1.isLeftPressed()):
    player1.moveLeft()