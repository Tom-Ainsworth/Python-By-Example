import random

# 052 Display a random integer between 1 and 100 inclusive.
# num = random.randint (1,100)
# print (num)


# # 053 Display a random fruit from a list of five fruits.
# fruit = random.choice ( ['apple','orange','grape','banana','strawberry'])
# print (fruit)


# 054 Randomly choose either heads or tails ("h" or "t"). Ask the user to make their choice. If their choice is the same
# as the randomly selected value, display the message "You win", otherwise display "Bad luck". At the end, tell the user
# if the computer selected heads or tails.
# coin = random.choice (["h", "t"])
# guess = input ("Enter (h)eads or (t)ails: ")
# if guess == coin:
#     print ("You win")
# else:
#     print ( "Bad luck")
# if coin == "h":
#     print ("It was heads")
# else:
#     print ("It was tails")


# 055 Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the
# message "Well done" otherwise tell them if they are too high or too low and ask them to pick a second number.
# If they guess correctly on their second guess, display "Correct", otherwise display "You lose"
# num = random.randint (1,5)
# guess  = int(input ("Enter a number: "))
# if guess == num:
#     print ("Well done")
# elif guess > num:
#     print ("Too high")
#     guess = int(input ("Guess again: "))
#     if guess == num:
#         print ("Correct")
#     else:
#         print ("You lose")
# elif guess < num:
#     print ("Too low")
#     guess = int(input("Guess again: "))
#     if guess == num:
#         print ("Correct")
#     else:
#         print ("You lose")


# 056 Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until
# they enter the number that was randomly picked.
# num = random.randint (1, 10)
# correct = False
# while correct == False:
#     guess = int(input("Enter a number: "))
#     if guess == num:
#         correct = True


# 057 Update program 056 so that it tells the user if they are too high or too low before they pick again.
# num = random.randint(1,10)
# correct = False
# while correct == False:
#     guess = int(input("Enter a number:"))
#     if guess == num:
#         correct = True
#     elif guess > num:
#         print ("Too high")
#     else:
#         print ("Too low")

# 058 Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question
# (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At
# the end of the quiz, tell them how many they got correct out of five.
score = 0
for i in range(1, 6):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = num1 + num2
    print(num1, "+". num2)
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score = score + 1
print("You scored", score, "out of 5")

# 059 Display five colours and ask the user to pick one. If they pick the same as the program has chosen, sav "Well
# done", otherwise display a witty answer which involves the correct colour, e.g. "I bet you are GREEN with envy'
# or "You are probably feeling BLUE right now". Ask them to quess again; if they have still not got it right,
# keep giving them the same clue and ask the user to enter a colour until they guess it correctly.
colour = random. choice (["red", "blue", "green", "white","pink"])
print("Select from red, blue, green, white or pink")
tryagain = True
while tryagain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()
    if colour == theirchoice:
        print ("Well done")
        tryagain = False
    else:
        if colour == "red":
            print ("I bet you are seeing RED right now! ")
        elif colour == "blue":
            print ("Don't feel BLUE.")
        elif colour == "green":
            print ("I bet you are GREEN with envy right now.")
        elif colour == "white":
            print ("Are you WHITE as a sheet, as you didn't guess correctly?")
        elif colour == "pink":
            print ("Shame you are not feeling in the PINK, as you got it wrong!")