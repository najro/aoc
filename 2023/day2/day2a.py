lines = open("C:\\dev\\repos\\aoc\\2023\\day2\\day2a.txt", "r").readlines()


for line in lines:
    print(line)
    game = line.split(':')

    gameNumber = int(game[0].split()[1].strip())

    gameSetInfo = game[1]


    print("Gamenumber:", gameNumber)
    print("gameSetInfo:", gameSetInfo)

