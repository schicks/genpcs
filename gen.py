import random
import re
import sys


def main():
    stats = {1: (4, 3, 2, 2), 2: (4, 3, 3, 2), 3: (4, 4, 3, 2), 4: (5, 4, 3, 2), 5: (5, 5, 3, 2), 6: (4, 4, 4, 3),
             7: (5, 4, 4, 3), 8: (5, 5, 4, 3), 9: (6, 5, 4, 3), 10: (6, 5, 5, 4)}
    traits = {1: (2, 4), 2: (1, 4), 3: (1, 6), 4: (1, 8), 5: (1, 10), 6: (2, 6), 7: (2, 8), 8: (2, 10)}
    relationships = {1: (2, 4), 2: (1, 4), 3: (1, 6), 4: (1, 8), 5: (1, 10), 6: (2, 6), 7: (2, 8), 8: (2, 10), 9: (3, 6)
        , 10: (3, 8)}
    freedice = {1: (2, 4), 2: (2, 6), 3: (4, 6), 4: (1, 8), 5: (2, 8), 6: (1, 10)}
    # dice tables for generation
    f = open(sys.argv[1], 'w')
    for char in range(6):
        f.write('Name:\n')
        f.write('Stats:\n')
        statblock = random.sample(stats[random.randint(1, 10)], 4)
        f.write('Acuity: {}\tBody: {}\tHeart: {}\tWill: {}\n'.format(*map(lambda x: writecode((x, 6)), statblock)))
        f.write('Traits:\n')
        for trait in range(4):
            f.write('TraitName\t{}\n'.format(writecode(traits[random.randint(1, 8)])))
        f.write('Relationships:\nBlood 1d6\n')
        for trait in range(2):
            f.write('RelName\t{}\n'.format(writecode(relationships[random.randint(1, 10)])))
        f.write('\n')
    f.write('Free Dice:{}\t{}\t{}'.format(*map(lambda x: writecode(freedice[random.randint(1, 6)]), range(3))))
    f.close()


def roll(diecode):  # takes a tuple in the form of (ndice, diesize, bonus) and returns a roll on that code.
    total = 0
    for die in range(diecode[0]):
        total += random.randint(1, diecode[1])
    if len(diecode) > 2:
        total += diecode[2]
    return total


def readcode(codestring):
    # takes a string and returns a tuple representing the diecode. returns null if formatted wrong.
    match = re.match(r'([0-9]+)d([0-9]+)\+([0-9]+)')
    if match:
        return match.group(1), match.group(2), match.group(3)
    return None


def writecode(diecode):
    if len(diecode) > 2:
        return '{}d{}+{}'.format(*diecode)
    return '{}d{}'.format(*diecode)


main()
