from pprint import PrettyPrinter
import math

pprint = PrettyPrinter(width=1).pprint

def amt_each_item(goal_lvl,current_lvl,goal_amt):
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

def num_five_matches(goal_lvl,current_lvl,goal_amt):
    if goal_lvl == current_lvl or goal_lvl == 0:
        return 5* math.ceil(goal_amt/5)
    else:
        return num_five_matches(goal_lvl-1, current_lvl, 5*(goal_amt + goal_amt%2) // 2)

def num_five_and_three_matches(goal_lvl,current_lvl, goal_amt):
    if goal_lvl == current_lvl:
        return goal_amt
    else:
        return int(num_five_and_three_matches(goal_lvl-1, current_lvl, math.ceil(goal_amt*5/2)))

def main():
    print("Note: Life essences are level 0, life orbs are level 1, etc., so a level 9 life orb is level 9 in this program.")
    print("\t  This program is only optimized for harvesting items that behave like life orbs from items that behave like life trees.\n")
    goal_lvl = int(input("What level are you aiming for? "))
    goal_amt = int(input("How many of those do you want? "))
    current_lvl = int(input("What level of things are you harvesting? "))
    print("Harvest exactly " + str(num_five_and_three_matches(goal_lvl, current_lvl, goal_amt)) + " level " + str(current_lvl) + " things.")
    print("Or, to always merge five, harvest ", num_five_matches(goal_lvl, current_lvl, goal_amt),"level",current_lvl,"things.")
    print("If you are always merging by five, you will have (lvl:amt):")
    pprint(amt_each_item(goal_lvl, current_lvl, goal_amt))

main()
