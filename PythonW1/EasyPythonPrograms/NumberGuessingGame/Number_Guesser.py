import random

num_of_guess = input("choose how many guesses you want: ")
top_of_range = input ("choose a number: ")
guess_counter = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Plese type a number larger than 0 bext time.")
        quit()
else:
    print("please type in a number next time.")
    quit()

random_num = random.randrange(0, top_of_range)

while True:
    guess_counter += 1
    num_of_guess = int(num_of_guess) - 1
    user_guess = input("Make a guess: ")

    if num_of_guess == 0:
        break
    else:

        if user_guess.isdigit():
            user_guess = int(user_guess)

        else:
            print("please type in a number next time.")
            continue

        if user_guess == random_num:
            print("You got it!")
            break
        elif user_guess > random_num:
            print("you were above the number!")
        else:
            print("you were below the number!")
if user_guess == random_num:
    print("You got it in", guess_counter,"guesses")
else:
    print("you failed to guess the number in", guess_counter)