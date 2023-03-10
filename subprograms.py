import random
import csv

# * 118
# * Define a subprogram that will ask the user to enter a number and save it as the variable "num". Define another subprogram that will use "num" and count from 1 to that number.
# def set_num_from_user():
#     num = int(input("Enter a number: "))
#     return num


# def count_from_one_to_num(number):
#     for i in range(1, number + 1):
#         print(i)


# def main():
#     num = set_num_from_user()
#     count_from_one_to_num(num)


# main()

# * 119
# * Define a subprogram that will ask the user to pick a low and a high number, and then generate a random number between those two values and store it in a variable called comp_num.
# * Define another subprogram that will give the instruction "I am thinking of a number..." and then ask the user to guess the number they are thinking of.
# * Define a third subprogram that will check to see if the comp_num is the same as the user's guess. If it is, it should display the message "Correct, you win", otherwise it should keep looping, telling the user if they are too low or too high and asking them to guess again until they guess correctly.


# def generate_random_number():
#     """Asks for 2 integers as a lower and upper range a random integer between that range.

#     Returns:
#         int: A random integer between the given range
#     """
#     low_num = int(input("Choose a number to range FROM: "))
#     high_num = int(input("Choose a number to range TO: "))
#     comp_num = random.randint(low_num + 1, high_num - 1)
#     return comp_num


# def get_user_number_guess():
#     """Asks user for an integer and returns that value.

#     Returns:
#         int: user inputted integer to be passed elsewhere
#     """
#     print("I am thinking of a number...")
#     num = int(input("Guess the number I'm thinking of: "))
#     return num


# def compare_two_nums(comp_num, user_num):
#     """Recursivley compares two numbers until they are equal.

#     Args:
#         comp_num: A static integer to be compared with.
#         user_num: Another integer to compare with comp_num. If it's not equal to comp_num, the function will ask for a new number and recursively compare that to comp_num.
#     """
#     if user_num < comp_num:
#         new_guess = int(input("Too low, try a higher number: "))
#         return compare_two_nums(comp_num, new_guess)
#     elif user_num > comp_num:
#         new_guess = int(input("Too high, try a lower number: "))
#         return compare_two_nums(comp_num, new_guess)
#     else:
#         print("Correct, you win!")


# def main():
#     compare_two_nums(generate_random_number(), get_user_number_guess())


# main()

# * 120
# * Display the following menu to the user:
# * 1.    Addition
# * 2.    Subtraction
# * Enter 1 or 2:
# * If they enter a 1, it should run a subprogram that will generate two random numbers between 5 and 20, and ask the user to add them together. Work out the correct answer and return both the user's answer and the correct answer.
# * If they entered 2 as their selection on the menu, it should run a subprogram that will generate one number between 25 and 50 and another number between 1 and 25 and ask them to work out num1 minus num2. This way they will not have to worry about negative answers.
# * Return both the user's answer and the correct answer.
# * Create another subprogram that will check if the user's answer matches the actual answer. If it does, display
# * "Correct", otherwise display a message that will say
# * "Incorrect, the answer is" and display the real answer.
# * If they do not select a relevant option on the first menu you should display a suitable message.
# def add_two_nums():
#     """Generates two numbers to add together

#     Returns:
#         tuple: The user's answer and the correct answer"""

#     num1 = random.randint(5, 20)
#     num2 = random.randint(5, 20)
#     guess = int(input(f"What is {num1} + {num2}? "))
#     return (guess, num1 + num2)


# def subtract_two_nums():
#     """Generates two numbers to subtract from one another

#     Returns:
#         tuple: The user's answer and the correct answer"""

#     num1 = random.randint(25, 50)
#     num2 = random.randint(1, 25)
#     guess = int(input(f"What is {num1} - {num2}? "))
#     return (guess, num1 - num2)


# def calc_result(num1, num2):
#     """
#     Checks whether two integers are equal to each other.

#     Args:
#         num1: first value to compare
#         num2: second value to compare
#     """
#     if num1 == num2:
#         print("Correct")
#     else:
#         print("Incorrect")


# menu_choice = int(input("Selection option 1 or 2: "))


# def main():
#     print("1. Addition")
#     print("2. Subtraction")
#     while menu_choice < 1 or menu_choice > 2:
#         menu_choice = int(input("That isn't an option. Select 1 or 2: "))
#     if menu_choice == 1:
#         user_guess, correct_answer = add_two_nums()
#         calc_result(user_guess, correct_answer)
#     else:
#         user_guess, correct_answer = subtract_two_nums()
#         calc_result(user_guess, correct_answer)


# * 121
# * Create a program that will allow the user to easily manage a list of names. You should display a menu that will allow them to add a name to the list, change a name in the list, delete a name from the list or view all the names in the list. There should also be a menu option to allow the user to end the program. If they select an option that is not relevant, then it should display a suitable message. After they have made a selection to either add a name, change a name, delete a name or view all the names, they should see the menu again without having to restart the program. The program should be made as easy to use as possible.
# names_list = ["Tom", "Dick", "Harry"]


# def display_list():
#     """Display a list of names"""
#     print("\n")
#     for idx, name in enumerate(names_list):
#         print(f"{idx}: {name}")


# def show_menu():
#     print("\n")
#     print("1. Add a name to the list")
#     print("2. Delete a name from the list")
#     print("3. View all names in the list")
#     print("4. End the program")
#     menu_choice = int(input("Choose a menu option number from 1-4: "))

#     return menu_choice


# def add_name():
#     """Takes a user inputted name and adds it to names_list"""

#     new_name = input("Enter a new name: ").title()
#     names_list.append(new_name)


# def delete_name():
#     """Asks the user for a name, then deletes it from names_list"""
#     try_again = True
#     while try_again == True:
#         name = int(input("Enter the number of the name you want to delete: "))
#         if 0 <= name < len(names_list):
#             print(f"Deleting record {name}, {names_list[name]}")
#             del names_list[name]
#             try_again = False
#         else:
#             print("That name isn't in the list")
#             display_list()


# def check_menu_choice(menu_choice):

#     while menu_choice < 1 or menu_choice > 4:
#         menu_choice = int(input("That isn't an option. Select a number from 1-4: "))
#     if menu_choice == 1:
#         add_name()
#         check_menu_choice(show_menu())
#     elif menu_choice == 2:
#         display_list()
#         delete_name()
#         check_menu_choice(show_menu())
#     elif menu_choice == 3:
#         display_list()
#         check_menu_choice(show_menu())
#     else:
#         print("Ending program, thank you for using the list!")


# def main():
#     display_list()
#     check_menu_choice(show_menu())


# main()

# * 122
# * Create the following menu;
# * 1.    Add to file
# * 2.    View all records
# * 3.    Quit program
# * Enter the number of your selection:
# * if the user selects 1, allow them to add to a file called Salaries.csv which will store their name and salary. If they select 2 it should display all records in the Salaries.csv file. If they select 3 it should stop the program. If they select an incorrect option they should see an error message. They should keep returning to the menu until they select option 3.
# def show_menu():
#     print("\n")
#     print("1. Add to file")
#     print("2. View all records")
#     print("3. Quit program")
#     menu_choice = int(input("Choose a menu option number from 1-3: "))
#     return menu_choice


# def show_all_records():
#     """Displays all records in the Salaries.csv file"""
#     file = csv.reader(open("Salaries.csv"))
#     print("\n")
#     for name, salary in file:
#         print(f"Name: {name}, Salary: {salary}")


# def add_to_file():
#     file = open("Salaries.csv", "a")
#     name = input("Enter your name: ").title()
#     salary = int(input("Enter your salary: "))
#     file.write(f"{name},{salary}\n")
#     file.close()


# def check_menu_choice(menu_choice):
#     while menu_choice < 1 or menu_choice > 3:
#         menu_choice = int(input("That isn't an option. Select a number from 1-3: "))
#     if menu_choice == 1:
#         add_to_file()
#         check_menu_choice(show_menu())
#     elif menu_choice == 2:
#         show_all_records()
#         check_menu_choice(show_menu())
#     else:
#         print("Ending program, thank you for using the list!")


# def main():
#     check_menu_choice(show_menu())


# main()


# * 123
# * In Python, it is not technically possible to directly delete a record from a .csv file. Instead you need to save the file to a temporary list in Python, make the changes to the list and then overwrite the original file with the temporary list.
# * Change the previous program to allow you to do this. Your menu should now look like this:
# * 1.    Add to file
# * 2.    View all records
# * 3.    Delete a record
# * 4.    Quit program
# * Enter the number of your selection:
def show_menu():
    print("\n")
    print("1. Add to file")
    print("2. View all records")
    print("3. Delete a record")
    print("4. Quit program")
    menu_choice = int(input("Choose a menu option number from 1-4: "))
    return menu_choice


def show_all_records():
    """Displays all records in the Salaries.csv file"""
    file = csv.reader(open("Salaries.csv"))
    print("\n")
    for row in file:
        print(f"Name: {row[0]}, Salary: {row[1]}")


def add_to_file():
    file = open("Salaries.csv", "a")
    name = input("Enter your name: ").title()
    salary = int(input("Enter your salary: "))
    file.write(f"{name},{salary}\n")
    file.close()


def delete_a_record():
    file = list(csv.reader(open("Salaries.csv")))
    salaries = []
    for row in file:
        salaries.append(row)
    for row in salaries:
        print(f"{salaries.index(row)}, {row}")

    choice = int(input("Choose an index number to delete a salary from the list: "))
    print(f"Deleting {salaries[choice]}...")
    del salaries[choice]

    x = 0
    file = open("Salaries.csv", "w")
    for row in salaries:
        newRecord = salaries[x][0] + "," + salaries[x][1] + "," + "\n"
        file.write(newRecord)
        x += 1
    file.close()


def check_menu_choice(menu_choice):
    while menu_choice < 1 or menu_choice > 4:
        menu_choice = int(input("That isn't an option. Select a number from 1-4: "))
    if menu_choice == 1:
        add_to_file()
        check_menu_choice(show_menu())
    elif menu_choice == 2:
        show_all_records()
        check_menu_choice(show_menu())
    elif menu_choice == 3:
        delete_a_record()
        check_menu_choice(show_menu())
    else:
        print("Ending program, thank you for using the list!")


def main():
    check_menu_choice(show_menu())


main()
