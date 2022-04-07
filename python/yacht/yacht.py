
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum([x == 1 for x in dice]) * 1
TWOS = lambda dice: sum([x == 2 for x in dice]) * 2
THREES = lambda dice: sum([x == 3 for x in dice]) * 3
FOURS = lambda dice: sum([x == 4 for x in dice]) * 4
FIVES = lambda dice: sum([x == 5 for x in dice]) * 5
SIXES = lambda dice: sum([x == 6 for x in dice]) * 6
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and any(dice.count(x) == 3 for x in set(dice)) else 0
FOUR_OF_A_KIND = lambda dice: sum(x * 4 for x in set(dice) if dice.count(x) > 3) 
LITTLE_STRAIGHT = lambda dice: 30 if set(dice) == {1, 2, 3, 4, 5} else 0
BIG_STRAIGHT = lambda dice: 30 if set(dice) == {2, 3, 4, 5, 6} else 0
CHOICE = lambda dice: sum(dice)


def score(dice, category):
    return category(dice)
