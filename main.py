import urllib.request
import json
import random
import team
import GUI

_NHLrecords = None
_NHLteamdata = None
winners = ['default','default','default']

def nhlapi(): # Fetch NHL API and returns team records
    nhl = urllib.request.urlopen("https://statsapi.web.nhl.com/api/v1/standings/byLeague")
    data = json.load(nhl)
    records = data['records'][0]['teamRecords']
    return records

def nhlodds(): # Fetch NHL Lottery odds from local txt file
    NHLodds = open('NHLodds.txt')
    odds = NHLodds.readlines()
    NHLodds.close()
    return odds

def teamname(curRank):
    return str(_NHLrecords[curRank]['team']['name'])

def isValid(curRank):
    wildcardrank = int(_NHLrecords[curRank]['wildCardRank'])
    if wildcardrank > 2: return True
    return False

def fetchNHLinfo():
    global _NHLrecords
    teams = []
    odds = nhlodds()  # sets varibale 'odds' to our accurate NHL odds
    curRank = 30  # Index of the LAST PLACE TEAM
    oddsIndex = 0  # Index of our odds array
    beginningodds = 0
    endingodds = 0

    for record in _NHLrecords:
        if isValid(curRank): # if the team is a lottery team...
            name = teamname(curRank) # fetch data
            currentodds = float(odds[oddsIndex]) # fetch odds
            endingodds += currentodds # endingodds
            currentTeam = team.TeamData(name, beginningodds, endingodds)
            teams.append(currentTeam)

            beginningodds = endingodds
            oddsIndex+=1
        curRank -= 1
    return teams



#class lottery:
def rollthedice():
    return round(random.uniform(0.0, 99.9), 1)

def NHLlottery():
    global winners
    for i in range(3):
        lotteryball = rollthedice()
        for team in _NHLteamdata:
            if team.didWeWin(lotteryball) and team.beenChosen():
                if winners[2] != "default": break
                NHLlottery()
                break

            if team.didWeWin(lotteryball) and not team.beenChosen():
                if winners[0] == "default":
                    winners[0] = team.file
                elif winners[1] == "default":
                    winners[1] = team.file
                elif winners[2] == "default":
                    winners[2] = team.file
                # else:
                #     print("team name error, debug me")
                team.chosen = True
                break

def getWinners():
    return winners

def setupAPI():
    global _NHLrecords
    global _NHLteamdata
    _NHLrecords = nhlapi()  # sets global variable '_NHLrecords' to our NHL API
    _NHLteamdata = fetchNHLinfo()  # returns array of NHLTeams and their odds

def reset(records):
    global _NHLrecords
    global _NHLteamdata
    _NHLrecords = records  # sets global variable '_NHLrecords' to our NHL API
    _NHLteamdata = fetchNHLinfo()  # returns array of NHLTeams and their odds

    for i in range(3):
        winners[i] = 'default'
    _NHLteamdata = fetchNHLinfo()  # RESETS OUR TEAM DATA ARRAY SO BEEN CHOSEN BOOLEAN IS FALSE
    NHLlottery()
    GUI._winners = winners

    #_NHLteamdata = fetchNHLinfo()  # RESETS OUR TEAM DATA ARRAY SO BEEN CHOSEN BOOLEAN IS FALSE


# main method
if __name__ == '__main__':
    setupAPI()

    NHLlottery()

    GUI.vp_start_gui(winners, _NHLrecords)





    #
    # while True:
    #   i = input('Press "n" to play the lottery')
    #   if i == 'n':
    #       p = 0
    #       while True:
    #         if p > 2:
    #             _NHLteamdata = fetchNHLinfo() #RESETS OUR TEAM DATA ARRAY SO BEEN CHOSEN BOOLEAN IS FALSE
    #             break
    #         NHLlottery()
    #         print()
    #         p+=1
    #
    #   if i == 'x': break
