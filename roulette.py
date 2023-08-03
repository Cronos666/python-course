import random
class FairRoulette(object):
    def __init__(self):
        self.pockets = []
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets) -1
    def spin(self):
        self.ball = random.choice(self.pockets)
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: return -amt
    def betColor(self, color, amt):
        if str(self.ball%2) == str(color):
            return amt*1.5
        else: return -amt
    def __str__(self):
        return 'Fair Roulette'

def play(game, gtype, spins, pocket, bet, output):
    totPocket = 0
    for i in range(spins):
        game.spin()
        if gtype == 0:
            totPocket += game.betPocket(pocket, bet)
        if gtype == 1:
            totPocket += game.betColor(pocket, bet)
    if output:
        print(spins, 'spins of', game)
        print('Expected return betting', pocket, '=', str(100*totPocket/spins)+'%\n')
    return (totPocket/spins)

game = FairRoulette()

for i in range(6):
    play(game, 0, 10000000, 6, 1, True) 
