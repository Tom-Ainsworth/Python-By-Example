# * 69 Create a tuple containing the names of five countries and display the
# * whole tuple. Ask the user to enter one of the countries that have been
# * shown to them and then display the index number (i.e. position in the list)
# * of that item in the tuple.
# countries = ('England', 'Ireland', 'Scotland', 'Wales', 'France')
# print(countries)
# choice = input("Enter one of the above countries: ")
# print(countries.index(choice))

# * 070 Add to program 069 to ask the user to enter a number and display the
# * country in that position.
# countries = ('England', 'Ireland', 'Scotland', 'Wales', 'France')
# print(countries)
# print(len(countries))
# choice = int(input(f"Enter a number between 0 and {len(countries)}: "))
# print(countries[choice])


# * 071 Create a list of two sports. Ask the user what their favourite sport
# * is and add this to the end of the list. Sort the list and display it.
# sports = ['football', 'tennis']
# choice = input('Choose a sport: ')
# sports.append(choice)
# print(sorted(sports))


# * 072 Create a list of six school subjects. Ask the user which of these
# * subjects they don't like. Delete the subject they have chosen from the
# * list before you display the list again.
# subjects = ['maths', 'science', 'english', 'drama', 'art', 'music']
# print(subjects)
# choice = input('Which subject do you like the least? ')
# subjects.remove(choice)
# print(subjects)


# * 073 Ask the user to enter four of their favourite foods and store them
# * in a dictionary so that they are indexed with numbers starting from 1.
# * Display the dictionary in full, showing the index number and the item.
# * Ask them which they want to get rid of and remove it from the list.
# * Sort the remaining data and display the dictionary.
# foods = {}
# choice1 = input("Choose four of your favourite foods. Choice 1: ")
# foods[1] = choice1
# choice2 = input('Choice 2: ')
# foods[2] = choice2
# choice3 = input('Choice 3: ')
# foods[3] = choice3
# choice4 = input('Choice 4: ')
# foods[4] = choice4

# print(foods)
# remove = int(input('Which one do you want to remove? '))
# del foods[remove]
# print(sorted(foods.values()))


# * 074 Enter a list of ten colours. Ask the user for a starting number
# * between 0 and 4 and an end number between 5 and 9. Display the list
# * for those colours between the start and end numbers the user input.
# colours = ['blue', 'green', 'black', 'yellow', 'red', 'purple', 'orange',
#            'pink', 'gold', 'silver']
# start = int(input('Enter a starting number between 1 and 4: '))
# end = int(input('Enter a ending number between 5 and 9: '))
# print(colours[start:end])


# * 075 Create a list of four three-digit numbers. Display the list to
# * the user, showing each item from the list on a separate line.
# * Ask the user to enter a three-digit number. If the number they have
# * typed in matches one in the list, display the position of that number
# * in the list, otherwise display the message "That is not in the list"
# digits = [123, 431, 541, 924]
# for num in digits:
#     print(num)
# choice = int(input(''))


# * 076 Ask the user to enter the names of three people they want to invite
# * to a party and store them in a list. After they have entered all three
# * names, ask them if they want to add another. If they do allow them to add
# * more names until they answer "no". When they answer "no", display how many
# * people they have invited to the party.
# guest_list = []
# for i in range(0, 3):
#     name = input("Enter a name: ")
#     guest_list.append(name)
# print(guest_list)


# * 077 Change program 076 so that once the user has completed their list of
# * names, display the full list and ask them to type in one of the names on
# * the list. Display the position of that name in the list. Ask the user if
# * they still want that person to come to the party. If theyanswer "no",
# * delete that entry from the list and display the list again. You are over
# * halfway there. Keep going, you have already learnt so much.
# guest_list = []
# for i in range(0, 3):
#     name = input("Enter a name: ")
#     guest_list.append(name)
# print(guest_list)
# choice = input("Choose a name from the list: ")
# print(f"{choice} is at index: {guest_list.index(choice)}")


# * 078 Create a list containing the titles of four TV programmes and display
# * them on separate lines. Ask the user to enter another show and a position
# * they want it inserted into the list. Display the list again, showing all
# * five TV programmes in their new positions.
programs = ["breaking bad", "hunters", "SNT", "the news"]
for i in range(len(programs)):
    print(i + "\n")


# * 079 Create an empty list called "nums" Ask the user to enter numbers. After
# * each number is entered, add it to the end of the nums list and display the
# * list. Once they have entered three numbers, ask them if they still want the
# * last number they entered saved. If they say "no", remove the last item from
# * the list. Display the list of numbers.
