from array import *
import random

# * 088
# * Ask the user for a list of five integers. Store them in an array Sort the
# * list and display it in reverse order.
# nums = array("i", [])
# for i in range(0, 5):
#     newNum = int(input("Enter a number: "))
#     nums.append(newNum)
# nums = sorted(nums)
# nums.reverse()
# print(nums)


# * 089
# * Create an array which will store a list of integers.
# * Generate five random numbers and store them in the array. Display the
# * array (showing each item on a separate line).
# nums = array("i", [])
# for i in range(0, 5):
#     nums.append(random.randint(1, 100))
# for i in nums:
#     print(i)


# * 090
# * Ask the user to enter numbers. If they enter a number between 10 and 20,
# * save it in the array. otherwise display the message "Outside the range".
# * Once five numbers have been successfully added, display the message
# * "Thank you" and display the array with each item shown on a separate line.
# nums = array("i", [])
# while len(nums) < 5:
#     num = int(input("Enter a number: "))
#     if 9 < num < 21:
#         nums.append(num)
#     else:
#         print("Outside the range")
# print("Thank you")


# * 091
# * Create an array which contains five numbers (two of which should be
# * repeated). Display the whole array to the user. Ask the user to enter
# * one of the numbers from the array and then display a message saying how
# * many times that numbe appears in the list.
# nums = array("i", [1, 2, 4, 2, 1])
# print(nums)
# userNum = int(input("Enter a number listed above: "))
# print(f"Your number appears {nums.count(userNum)} time(s) in the array")


# * 092
# * Create two arrays (one containing three numbers that the user enters and
# * one containing a set of five random numbers). Join these two arrays
# * together into one large array.
# * Sort this large array and display it so that each number appears on a
# * separate line.
# randomNums = array("i", [])
# for i in range(0, 5):
#     randomNums.append(random.randint(0, 20))
# userNums = array("i", [])
# for i in range(0, 2):
#     num = int(input("Enter a number: "))
#     userNums.append(num)
# randomNums.extend(userNums)
# randomNums = sorted(randomNums)
# for i in randomNums:
#     print(i)


# * 094
# * Display an array of five numbers. Ask the user to select one of the numbers.
# * Once they have selected a number, display the position of that item in
# * the array. If they enter something that is not in the array, ask them to
# * try again until they select a relevant item,
# nums = array("i", [1, 54, 2, 45, 3])
# print(nums)
# choice = int(input("Choose a number from above: "))
# while not choice in nums:
#     choice = int(input("That number is not in the array, please choose again: "))
# print(f"Your chosen number is at index {nums.index(choice)}")


# * 093
# * Ask the user to enter five numbers. Sort them into order and present them
# * to the user Ask them to select one of the numbers. Remove it from the
# * original array and save it in a new array.
# nums = array("i", [])
# for i in range(0, 5):
#     num = int(input("Enter a number: "))
#     nums.append(num)
# nums = sorted(nums)
# print(f"Here are the numbers you chose: {nums}")
# num = int(input("Choose a number to remove: "))
# nums.remove(num)
# newNums = array("i", [num])
# print(nums)
# print(newNums)


# * 095
# * Create an array of five numbers between 10 and 100 which each have two
# * decimal places. Ask the user to enter a whole number between 2 and 5 if
# * they enter something outside of that range, display a suitable error
# * message and ask them to try again until they enter a valid amount.
# * Divide each of the numbers in the array by the number the user entered
# * and display the answers shown to two decimal piaces.
nums = array("f", [23.23, 15.65, 76.33, 99.99, 47.23])
choice = int(input("Enter a number between 2 and 5: "))
while not 1 < choice < 6:
    choice = int(input("Number outside of the range. Try again: "))
for i in range(0, len(nums)):
    newNum = nums[i] / choice
    print(f"{nums[i]} / {choice} = {round(newNum, 2)}")
