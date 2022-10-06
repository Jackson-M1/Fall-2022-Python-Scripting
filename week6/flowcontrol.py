#!/usr/bin/env python3
'''
Author: Jackson Mckenney
Description: Week 6, Assignment 2, in this script I am learning flow control and testing decision logic
'''

print("""There's a zombie outbreak. A hoarde of zombies is chasing you, you find yourself
in front of 3 different bunkers. Do you enter bunker 1, 2, or 3?""")

bunker = input("-> ")

if bunker == "1":

    print("There's a large selection of weapons everywhere you look")
    print("A huge mutant zombie barges in behind you, you rush to grab a weapon,")
    print("what weapon do you choose to defend yourself?\n")

    print("1 - Rocket launcher")
    print("2 - Spear\n")

    weapon = input("-> ")

    if weapon == "1":
        print("You fire the rocket launcher only for it to jam and explode in your face, you're dead!")
    elif weapon == "2":
        print("You chuck the spear at the zombie, it goes clean through the zombies brain")
        print("Good job! You get to live for 10 more minutes!")
    else:
        print("You fail to make a decision in time")
        print("The zombie picks you up and eats you, you're dead!")

elif bunker == "2":
    print("There are zombies ravenously feasting on humans everywhere you look")
    print("What will you do?\n")
    
    print("1 - Turn around and run")
    print("2 - Play dead")
    print("3 - Try to fight through the zombies\n")

    death = input("-> ")

    if death == "1" or death == "3":
        print("Dude...come on...")
        print("The zombies overwhelm you in seconds, you're dead!")
    elif death == "2":
        print("You quickly get on the ground and smear the blood of nearby bodies all over yourself")
        print("The sound of zombies around you never ceases, you lay there until you die of starvation")
        print("You're dead!")
    else:
        print(f"{death} isn't viable, consider yourself brains a la mode, you're dead!")

elif bunker == "3":
    print("You got lucky! In front of you is a military squadron with their guns drawn")
    print("One of them signals for you to come to them and says 'quickly!'")
    print("What is your next action?\n")

    print("1 - Follow instructions and rush to the military men")
    print("2 - Question them, you suspect they may be highly intelligent zombies\n")

    savior = input("-> ")

    if savior == "1":
        print("You rush towards them with zombies on your tail")
        print("As you get behind them they open fire on the zombies chasing you")
        print("You are safe! For now...")
    elif savior == "2":
        print("Dude...come on...")
        print("The zombies rush in behind you, with some of them attacking you")
        print("You are suddenly hit with a barrage of bullets, you're dead!")
    else:
        print(f"You have found the secret option of {savior}...")
        print("You are teleported to the astral plane, Santa Claus greets you")
        print("He says 'everything will be ok', you are now immortal, you win!")

else:
    print("You didn't select a bunker??? Lame :(")


