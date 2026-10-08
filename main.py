## dnd test  envrioment

import random

def dieType(sides):
    return random.randint(1, sides)


def diceRoll():
    dice = dieType(20)

    advDis = input("Do you have advantage or disadvantage? y/n: ")

    if advDis == "y":
        prompt2 = input("(a)dv or (d)isadv: ")

        if prompt2 == "a":
            adv = dieType(20)
            dice = max(dice, adv)

        elif prompt2 == "d":
            dis = dieType(20)
            dice = min(dice, dis)

    print(dice)

    if dice == 1:
        print("critical miss")
    elif dice == 20:
        print("critical hit")
    else:
        print("is what you rolled")

    return dice

def ac():
    armorClass = 10
    attackRoll = diceRoll()
    damage = dieType(8)

    if attackRoll == 20:
        damage = damage * 2
        print(f"critical hit! You did {damage} damage")  
    elif armorClass <= attackRoll:
        print("you hit")
        print(f"you did {damage} damage")
    else:
        print("you missed")

def savethrow():
    # roll a d20 and beat 10 to save
    safe = diceRoll()
    spellDc = 10
    damage = dieType(10)

    if spellDc <= safe:
        damage = damage // 2
        print(f"You rolled {safe}")
        print(f"You saved! You only take {damage} damage")
    else:
        print(f"You rolled {safe}")
        print(f"You failed the save and take {damage} damage")
 #test
ac()
savethrow()

