"""
File: harvests.py
Author: Ashley Beckers
Description: Simple Python program that will tell you how many harvests it will take to reach your goal in the game
 Merge Dragons. Eventually (if I can find the time to collect the data) it will tell you how long that will take and
 possibly allow you to perfect your strategy during events. Enjoy!

Source of time information:
It is found that a dragon will 'nod' a certain, consistent number of times in a harvest. This animation does take a set
amount of time, 0.8 seconds. A nod is defined by a full cycle of down and up, ending when the dragon returns to start.
Dragons typically harvest things in some amount of half nods, or close enough to it that rounding will not be that
catastrophic.

I have counted several of these times, which are unique to each species of dragon, and stored them in harvest_times.txt.
This file is by no means complete and you are welcome to substitute your own (replace TIMES_FILE). Be sure to keep the
format the same and put your times in terms of nods (or, if in seconds, change SECONDS_PER_NOD to 1)
"""
import sys
from pprint import PrettyPrinter
import math
import file_reader
pprint = PrettyPrinter(width=1).pprint
TIMES_FILE = "harvest_times.txt"
SECONDS_PER_NOD = 0.8


def amt_each_item(goal_lvl, current_lvl, goal_amt):
    """
    Determines the amount of each orb obtained by only merging by fives
    :param goal_lvl: the level of the desired life orb
    :param current_lvl: the level of life orb being harvested
    :param goal_amt: the amount of life orbs desired
    :return: a dictionary | {level of life orb: amount of orbs at that level}
    """
    amts = dict()
    if goal_lvl != 0:
        amts[goal_lvl] = goal_amt + goal_amt%2
    else:
        amts[goal_lvl] = 5 * math.ceil(goal_amt/5)
    goal_amt = num_five_matches(goal_lvl,goal_lvl-1,goal_amt)
    for i in range(goal_lvl-1,current_lvl-1,-1):
        goal_amt = num_five_matches(i,i-1,goal_amt)
        amts[i] = goal_amt%2
    return amts


def num_five_matches(goal_lvl, current_lvl, goal_amt):
    """
    number of merges using only 5 merges to get the most profitable result
    :param goal_lvl: the level of the desired life orb
    :param current_lvl: the level of life orb being harvested
    :param goal_amt: the amount of life orbs desired
    :return: the number of harvests necessary
    """
    if goal_lvl == current_lvl or goal_lvl == 0:
        return 5 * math.ceil(goal_amt/5)
    else:
        return num_five_matches(goal_lvl-1, current_lvl, 5 * (goal_amt + goal_amt%2) // 2)


def num_five_and_three_matches(goal_lvl, current_lvl, goal_amt):
    """
    number of merges using both 5 and 3 merges to get the result as quickly as possible
    :param goal_lvl: the level of the desired life orb
    :param current_lvl: the level of life orb being harvested
    :param goal_amt: the amount of life orbs desired
    :return: the number of harvests necessary
    """
    if goal_lvl == current_lvl:
        return goal_amt
    else:
        return int(num_five_and_three_matches(goal_lvl-1, current_lvl, math.ceil(goal_amt*5/2)))


def main():
    """
    Runs the above methods to provide the user with information about harvesting life orbs from life flowers
    For ease of use, arguments for this information can either be entered in the command line or through prompt
    To use the command line, enter arguments as follows: goal_level goal_amount orb_harvesting_level
    To use prompt, enter nothing
    """
    print("Note: Life essences are level 0, life orbs are level 1, etc., so a level 9 life orb is level 9 in this program.")
    print("      This program is only optimized for harvesting life orbs from life trees.\n")

    if len(sys.argv) == 1:
        goal_lvl = int(input("What level are you aiming for? "))
        goal_amt = int(input("How many of those do you want? "))
        current_lvl = int(input("What level of things are you harvesting? "))
    else:
        if len(sys.argv) < 4:
            print("Usage: [level of goal orbs] [amount of goal orbs] [level of orbs currently harvested]",
                  file=sys.stderr)
            return
        goal_lvl = int(sys.argv[1])
        goal_amt = int(sys.argv[2])
        current_lvl = int(sys.argv[3])

    print("Harvest exactly " + str(num_five_and_three_matches(goal_lvl, current_lvl, goal_amt)) + " level " +
          str(current_lvl) + " things.")
    print("Or, to always merge five, harvest ", num_five_matches(goal_lvl, current_lvl, goal_amt), "level", current_lvl,
          "things.")
    print("If you are always merging by five, you will have (lvl:amt):")
    pprint(amt_each_item(goal_lvl, current_lvl, goal_amt))

    harvest_times = file_reader.time_file_parser(TIMES_FILE)


if __name__ == "__main__":
    main()
