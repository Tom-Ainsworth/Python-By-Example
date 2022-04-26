# 45 - Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and
# print the message "The total is... [total]". Stop the loop when the total is over 50
# total = 0
# while total <= 50:
#     num = int(input("Enter a number: "))
#     total = total + num
#     print("The total is...", total)


# 46 - Ask the user to enter a number. Keep asking until they enter a value over 5 and then display the message "The last number you entered
# was a [number]" and stop the program
# num = 0
# while num <= 5:
#     num = int(input("Enter a number: "))
# print("The last number you entered was a", num)


# 47 Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number
# If they answer "y", ask them to enter another number and keep adding numbers until they do not answer "y". Once the loop has stopped, display the total.
# num1 = int(input("Enter a number: "))
# total = num1
# print(total)
# addAgain = input("Add another number? (y/n)")
# while addAgain == "y":
#     num = int(input("Enter a number: "))
#     total = total + num
#     addAgain = input("Add another number? (y/n)")
# print("The final total is", total)


# 48 - Ask for the name of somebody the user wants to invite to a party. After this, display the message "[name] has now been invited"
# and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to
# the party and then display how many people they have coming to the party.
# count = 0
# name = input("Enter a name: ")
# print(name, "has now been invited")
# count += 1
# another = input("Invite someone else? (y/n)")
# while another == "y":
#     input("Enter a name: ")
#     count += 1
#     another = input("Invite someone else? (y/n)")
# print(count)

# 49 - Create a variable called compnum and set the value to 50. Ask the user to enter a number.
# While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them
# to have another guess. If they enter the same value as compnum, display the message "Well done, you took [count] attempts"
# count = 1
# compnum = 50
# guess = int(input("Enter a number: "))
# while guess != compnum:
#     if guess > compnum:
#         print("Guess too high")
#     else:
#         print("Guess too low")
#     count += 1
#     guess = int(input("Guess again: "))
# print("Well done, you took", count, "attempts")


# 50 - Ask the user to enter a number between 10 and 20. If they enter a value under 10, displau the message "Too low" and ask them
# to try again. If they enter a value above 20, display the message "Too high" and ask them to try again. Keep repeating this until
# they enter a value that is between 10 and 20 and then display the message "Thank you".
# num = int(input("Enter a number between 10 and 20 "))
# while num < 10 or num > 20:
#     if num < 10:
#         print("Too low")
#     else:
#         print("Too high")
#     num = int(input("Enter a number between 10 and 20 "))
# print("Thank you")
    

# 51 - Using the song "10 green bottles", display the lines "There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall,
# and if 1 green bottle should accidentally fall". Then ask the question "how many green bottles will be hanging on the wall?" If the user answers correctly,
# display the message "There will be [num] green bottles hanging on the wall". If they answer incorrectly, display the message "No, try again" until they get
# it right. When the number of green bottles gets down to 0, display the message "There are no more green bottles hanging on the wall".
num = 10
while num > 0:
    print("There are", num, "green bottles hanging on the wall,", num, "green bottles hanging on the wall, and if 1 green bottle should accidentally fall")
    guess = int(input("How many green bottles will be hanging on the wall? "))
    if guess == num-1:
        num -= 1
        print("There will be", num, "green bottles hanging on the wall")
    else:
        print("No, try again")
print("There are no more green bottles hanging on the wall")