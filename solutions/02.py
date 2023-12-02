import os
import re

script_dir = os.path.dirname(__file__)
rel_path = '../inputs/02.txt'

file = open(os.path.join(script_dir, rel_path), 'r', encoding='utf-8')

MAX = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def getGame(gameString):
    parts = gameString.strip().split(':')
    gameNum = parts[0].split(' ')[1]

    games = [a.strip().split(' ') for a in re.split(r'[\;,]\s', parts[1])]

    return gameNum, games

def main():
    sum1 = 0

    for line in file:
        gameNum, games = getGame(line)

        gameMatchesCriteria = True
        for game in games:
            if MAX[game[1]] < int(game[0]):

                gameMatchesCriteria = False
                break

        if gameMatchesCriteria:
            sum1 += int(gameNum)

    print('Part 1:', sum1)

    file.seek(0)
    sum2 = 0

    for line in file:
        gameNum, games = getGame(line)

        highest = {
            'red': 1,
            'blue': 1,
            'green': 1
        }

        for game in games:

            num = int(game[0])

            if highest[game[1]] < num:
                highest[game[1]] = num

        sum2 += highest['red'] * highest['green'] * highest['blue']

    print('Part 2:', sum2)


main()
