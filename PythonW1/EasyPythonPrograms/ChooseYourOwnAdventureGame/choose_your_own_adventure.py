name = input("type your name: ")
print("welcome", name,"to this adventure!")

answer = input("you are on a dirt road, it has come to an end, would like like to go right or left ? ").lower

if answer == "left":
    answer == input("you cme to a riverm you can walk around it or swim accross? would you like to walk or swim ? ").lower
    if answer == "walk":
        print("you walked around and found a cabin.")
    elif answer == "swim":
        print("You started to swim and the water starts to bubble what do you do ? do you stop swimming or do you swim faster? ")   
    else:
        print("not a valid answer. you lose!")
elif answer == "right":
    answer = input("you come to a bridge it looks wobble, do you want to cross it or head back ?").lower
    if answer == "cross":
        print("you walked around and found a cabin.")
    elif answer == "back":
        print("You started to swim and the water starts to bubble what do you do ? do you stop swimming or do you swim faster? ")   
    else:
        print("not a valid answer. you lose!")
else:
    print("not a valid answer. you lose!")