class TeamData:
    chosen = False
    def __init__(self, name, oddsBegin, oddsEnd):
        self.name = name
        self.oddsBegin = oddsBegin
        self.oddsEnd = oddsEnd
        self.file = self.logofile(name)

    def logofile(self, name):
        idx = name.rfind(' ') + 1
        subs = name[idx:]
        return subs

    def beenChosen(self):
        #print('insideBeenChosen')
        return self.chosen

    def didWeWin(self, lotteryball):
        if lotteryball >= self.oddsBegin and lotteryball < self.oddsEnd:
            return True
        return False

    def setChosen(self, chosen):
        self.chosen = chosen