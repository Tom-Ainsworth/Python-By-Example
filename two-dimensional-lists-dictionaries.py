# * Challenges
# * 096
# * Create the following using a simple 2D list using the standard Python indexing:
# *       0   1   2
# * 0     2   5   8
# * 1     3   7   4
# * 2     1   6   9
# * 3     4   2   0
# nums = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
# print(nums)


# * 097
# * Using the 2D list from program 096, ask the user to select a row and a column
# * and display that value.
# rowSelection = int(input("Choose a row: "))
# columnSelection = int(input("Choose a column: "))
# print(
#     f"Here is your selection from row {rowSelection}, column {columnSelection} is: {nums[rowSelection][columnSelection]}"
# )


# * 098
# * Using the 2D list from program 096. ask the user which row they would like
# * displayed and display just that row. Ask ther to enter a new value and add it
# * to the end of the row and display the row again.
# rowSelection = int(input("Which row would you like to display? "))
# print(f"You chose row {rowSelection}: {nums[rowSelection]}")
# newSelection = int(input("Choose a value to add to the end of this row: "))
# nums[rowSelection].append(newSelection)
# print(f"The new row is: {nums[rowSelection]}")


# * 099
# * Change your previous program to ask the user which row they want displayed.
# * Display that row. Ask which column in that row they want displayed and
# * display the value that is held there. Ask the user if they want to change the
# * value. If they do, ask for a new value and change the data. Finally, display
# * the whole row again.
# rowSelection = int(input("Which row would you like to display? "))
# print(f"You chose row {rowSelection}: {nums[rowSelection]}")
# columnSelection = int(input("Which column in this row would you like to display? "))
# print(f"You chose column {columnSelection}: {nums[rowSelection][columnSelection]}")
# changeMind = input("do you want to change this column? y/n ")
# if changeMind.lower() == "y":
#     columnSelection = int(input("Which column in this row would you like to display? "))
#     print(f"You chose column {columnSelection}: {nums[rowSelection][columnSelection]}")
# print(nums[rowSelection])

# * 100
# * Create the following using a 2D dictionary showing the sales each person has
# * made in the different geographical regions:
# *           N       S       E       W
# * John      3056    8463    8441    2694
# * Tom       4832    6786    4737    3612
# * Anne      5239    4802    5820    1859
# * Fiona     3904    3645    8821    2451
# regionalSales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }


# * 101
# * Using program 100, ask the user for a name and a region. Display the
# * relevant data. Ask the user for the name and region of data they want to
# * change and allow them to make the alteration to the sales figure.
# * Display the sales for all regions for the name they choose
# regionalSales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# print(regionalSales.keys())
# name = input("Choose a salesperson from the names above: ").capitalize()
# area = input("Choose a region: N/S/E/W ").upper()
# print(
#     f"You chose {name}'s sales from the {area} region: {regionalSales[name][area]}"
# )
# newSalesFigure = int(input(f"Enter a new number for {name}'s {area} region: "))
# regionalSales[name][area] = newSalesFigure
# print(regionalSales[name])


# * 102
# * Ask the user to enter the name, age and shoe size for four people. Ask for
# * the name of one of the people in the list and display their age and shoe size.
newDict = {}
for i in range(0, 4):
    name = input("Enter a name: ").capitalize()
    age = int(input("Enter their age: "))
    shoeSize = int(input("Enter a shoe size: "))
    newDict[name] = {"Age": age, "ShoeSize": shoeSize}
query = input("Choose a name of one of the people you just added: ").capitalize()
print(newDict[query])


# * 103
# * Adapt program 102 to display the names and ages of all the people in the
# * list but do not show their shoe size.
for name in newDict:
    print((name), newDict[name]["Age"])


# * 104
# * After gathering the four names, ages and shoe sizes, ask the user to enter
# * the name of the person they want to remove from the list. Delete this row
# * from the data and display the other rows on separate lines.
personToRemove = input(
    "Choose the name of the person you want to remove: "
).capitalize()
del newDict[personToRemove]
for i in newDict:
    print((i), newDict[i])
