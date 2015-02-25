import random

class Villager:
    def __init__(self):
        self.isBad = False
        self.isMerlin = False
        self.isPercival = False

class Minion(Villager):
    def __init__(self):
        Villager.__init__(self)
        self.isBad = True

class Merlin(Villager):
    def __init__(self):
        Villager.__init__(self)
        self.isMerlin = True

class Percival(Villager):
    def __init__(self):
        Villager.__init__(self)
        self.isPercival = True

def shuffle(arr):
    for i in range(len(arr)):
        swapPos = random.randint(i, len(arr)-1)
        arr[i], arr[swapPos] = arr[swapPos], arr[i]

def probability(percent):
    x = random.random()
    return x < percent


class Game:
    numRoundsToWin = 3
    def __init__(self, numGood, numBad):
        self.goodWins = 0
        self.badWins = 0
        self.numPlayers = numGood+numBad
        self.numBadPlayers = numBad
        self.numGoodPlayers = numGood
        self.players = list()
        self.players.append(Merlin())
        self.players.append(Percival())
        for i in range(numGood-2):
            self.players.append(Villager())
        for i in range(numBad):
            self.players.append(Minion())

        shuffle(self.players)

    def getPlayersThatArentInSet(self, ret, s, numNeeded):
        while len(ret) < numNeeded:
            p = random.choice(self.players)
            if p not in s and p not in ret:
                ret.add(p)

        return ret


    def numPplForQuest(self,roundNum):
        def getPlayersFromString(s, roundNum):
            return int(s[roundNum])

        np = self.numPlayers
        if np == 5:
            return getPlayersFromString('23233', roundNum) #avalon
        elif np == 6:
            # return getPlayersFromString('23434', roundNum)
            return getPlayersFromString('23434', roundNum) #avalon
        elif np == 7:
            return getPlayersFromString('23344', roundNum) #avalon
        elif np == 8:
            return getPlayersFromString('34455', roundNum) #avalon
        elif np == 9:
            return getPlayersFromString('34455', roundNum) #avalon
        elif np == 10:
            return getPlayersFromString('34455', roundNum) #avalon

    def failsRequiredForQuest(self,roundNum):
        # if roundNum == 1:
        #     return 2
        # if roundNum == 2:
        #     return 2
        # if roundNum == 3:
        #     return 2
        if roundNum == 3 and self.numPlayers >= 7:
            return 2
        return 1


    def playGame(self):
        currLeaderNum = -1
        while self.badWins < self.numRoundsToWin and self.goodWins < self.numRoundsToWin:
            currLeaderNum = (currLeaderNum + 1) % self.numPlayers
            p = self.players[currLeaderNum]
            if p.isBad:
                if probability(.80):
                    self.badWins += 1
                continue #else someone new proposes the quest

            if p.isMerlin and probability(.6):
                self.goodWins += 1
                continue
            if p.isPercival and probability(.225):
                self.goodWins += 1
                continue

            # p is good
            questPlayers = set([p])
            self.getPlayersThatArentInSet(questPlayers, set([p]), self.numPplForQuest(self.badWins + self.goodWins))
            numBads = 0

            for qp in questPlayers:
                if qp.isBad:
                    numBads += 1

            if numBads >= self.failsRequiredForQuest(self.badWins + self.goodWins):
                self.badWins += 1
            else:
                self.goodWins += 1

        if self.goodWins > self.badWins:
            if probability(1/(self.numGoodPlayers-.65)*1):
                return False # merlin was assassinated
        return self.goodWins > self.badWins



wins = 0
totalGames = 20000
for i in range(totalGames):
    g = Game(4, 2)
    wins += g.playGame()


print wins, 'wins /', totalGames, '=', str(float(wins)/totalGames*100) +"%"
