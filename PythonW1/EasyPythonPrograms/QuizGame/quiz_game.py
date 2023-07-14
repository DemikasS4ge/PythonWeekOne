print("Welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()

questions = 3
points = 0

print("Question 1:")
answer = input("what does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("correct")
    points += 1
    print(str(points)+"/3")
else:
    print("incorrect")

print("Question 2:")
answer = input("what does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("correct")
    points += 1
    print(str(points)+"/3")
else:
    print("incorrect")

print("Question 3:")
answer = input("what does RAM stand for? ")

if answer.lower() == "random access memory":
    print("correct")
    points += 1
    print(str(points)+"/3")
else:
    print("incorrect")

percentage = points / questions * 100

print("congradulations you have " + str(points) + "/3! That is "+str(percentage)+"%")