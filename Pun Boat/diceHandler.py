import random
import math
import statistics


def diceHandle(dice: str):
    """The diceHandler class. Understands standard roll cobinations, and outputs standard results from these functions."""
    rolled = dice.split('d')
    limit = int(rolled[1])
    if dice[0] == "d":
        rolls = int(1)
    else:
        rolls = int(rolled[0])
    dice = []
    for r in range(0, rolls, 1):
        roll = random.randint(1,int(limit))
        dice.append(roll)
    diceaverage = 0
    dicelowest = 0
    dicehighest = 0
    dicetotal = 0
    dicemedian = 0
    dicemode = 0

    diceresults = {
        "rolls": "0",
        "average": 0,
        "lowest": 0,
        "highest": 0,
        "total": 0,
        "median": 0,
        "mode": 0
        }
    for test in range(0,limit):
        diceresults["amount"+str(test)] = 0
    for r in dice:
        for test in range(0,limit):
            if r == test:
               diceresults["amount"+str(r)] = diceresults["amount"+str(r)] + 1
                    
    diceaverage = statistics.mean(dice)
    dicelowest = min(dice)
    dicehighest = max(dice)
    dicetotal = sum(dice)
    dicemedian = statistics.median(dice)
    dicemode = max(set(dice), key=dice.count)
   

    diceresults["rolls"] = dice
    diceresults["average"] = diceaverage
    diceresults["lowest"] = dicelowest
    diceresults["highest"] = dicehighest
    diceresults["total"] = dicetotal
    diceresults["median"] = dicemedian
    diceresults["mode"] = dicemode

    return diceresults