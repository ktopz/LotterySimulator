# class lottery:
#     def rollthedice():
#         return round(random.uniform(0.0, 99.9), 1)
#
#     def NHLlottery():
#         lotteryball = rollthedice()
#         for team in _NHLteamdata:
#             if team.didWeWin(lotteryball) and team.beenChosen():
#                 NHLlottery()
#                 break
#
#             if team.didWeWin(lotteryball) and not team.beenChosen():
#                 global _FirstPlace
#                 global _SecondPlace
#                 global _ThirdPlace
#                 if _FirstPlace == "":
#                     _FirstPlace = team.file
#                 if _SecondPlace == "":
#                     _SecondPlace = team.file
#                 if _ThirdPlace == "":
#                     _ThirdPlace = team.file
#                 else:
#                     print("team name error")
#                 team.chosen = True
#                 break
#
#     def reset():
#         global _NHLteamdata
#         _NHLteamdata = fetchNHLinfo()  # RESETS OUR TEAM DATA ARRAY SO BEEN CHOSEN BOOLEAN IS FALSE
#
#         global _FirstPlace
#         global _SecondPlace
#         global _ThirdPlace
#         _FirstPlace = ""
#         _SecondPlace = ""
#         _ThirdPlace = ""
#
#     def getTeam(num):
#         if num == 1:
#             getFirst()
#         elif num == 2:
#             getSecond()
#         elif num == 3:
#             getThird()
#         else:
#             "error getting team"
#
#     def getFirst():
#         global _FirstPlace
#         return _FirstPlace
#
#     def getSecond():
#         global _SecondPlace
#         return _SecondPlace
#
#     def getThird():
#         global _ThirdPlace
#         return _ThirdPlace