def numPplForQuest(roundNum, np):
    def getPlayersFromString(s, roundNum):
        return int(s[roundNum])


    if np == 5:
        return getPlayersFromString('23233', roundNum)
    elif np == 6:
        return getPlayersFromString('23434', roundNum)
    elif np == 7:
        return getPlayersFromString('23344', roundNum)
    elif np == 8:
        return getPlayersFromString('34455', roundNum)
    elif np == 9:
        return getPlayersFromString('34455', roundNum)
    elif np == 10:
        return getPlayersFromString('34455', roundNum)

for roundNum in range(5):
    # print 2 + (roundNum) / 2,
    print numPplForQuest(roundNum, 9),

import random

def probability(percent):
    x = random.random()
    return x >= percent

# print probability(.99)
