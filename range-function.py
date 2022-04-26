# Challenges

# Page 37
# 42 - set a variable called total to 0. Ask the user to enter 5 numbers and after each input ask them if they want that number included. If they do, then add the number to the total.
# If they don't, don't add the number to the total. After they have entered all 5 numbers, display the total.
# total = 0
# for i in range(0, 5):
#     num = int(input("Enter a number: "))
#     answer = input("Do you want to include this number? (y/n) ")
#     if answer == "y":
#         total = total + num
# print(total)


# 43 - Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number and then count from 1 to that number.
# If they select down, ask them to enter a number below 20 and then count down from 20 to that number. If they entered something other than up or down,
# display the message "I don't understand"

# count = input("Which direction do you want to count? (up/down) ")
# if count == "up":
#     topNum = int(input("Choose a top number to count to: "))
#     for i in range(1, topNum+1):
#         print(i)
# elif count == "down":
#     bottomNum = int(input("Choose a number below 20: "))
#     for i in range(20, bottomNum-1, -1):
#         print(i)
# else:
#     print("I don't understand")
    
    
# 44 - Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display
# "[name] has been invited". If they enter a numver which is 10 or higher, display the message "Too many people".
# num = int(input("How many people do you want to invite? "))
# if num < 10:
#     for i in range(0, num):
#         name = input("What's their name? ")
#         print(f"[{name}] has been invited")
# else:
#     print("Too many people")