import csv

# * 111
# * Create a csv file that will store the data in the 'Challenge_111.jpg file. Call it "Books.cv"
# file = open("Books.csv", "w")
# newRecord = "To Kill A Mockingbird,Harper Lee,1960\n"
# file.write(str(newRecord))

# newRecord = "A Brief History of Time,Stephen Hawking,1988\n"
# file.write(str(newRecord))

# newRecord = "The Great Gatsby,F. Scott Fitzgerald,1922\n"
# file.write(str(newRecord))

# newRecord = "The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985\n"
# file.write(str(newRecord))

# newRecord = "Pride and Prejudice,Jane Austen,1813\n"
# file.write(str(newRecord))

# file.close()


# * 112
# * Using the Books.csv file from program 111, ask the user to enter another record and add it to the end of the file. Display each row of the .csv file on a separate line.
# file = open("Books.csv", "a")
# newRecord = input("Enter a new record (eg: book name, author, published date): ").title()
# file.write(str(newRecord + ","))
# file.close()
# file = open("Books.csv", "r")
# print(file.read())
# file.close()


# * 113
# * Using the Books.csv file, ask the user how many records they want to add to the list and then allow them to add that many. After all the data has been added, ask for an author and display all the books in the list by that author.
# * If there are no books by that author in the list, display a suitable message.
# newBooks = int(input("How many books do you want to add? "))
# file = open("Books.csv", "a")
# for i in range(0, newBooks):
#     newRecord = input(
#         "Enter a new record (eg: book name, author, date published): "
#     ).title()
#     file.write(newRecord)
# file.close()
# booksByAuthor = input("Search for books via their author: ").title()
# bookCount = 0
# file = open("Books.csv", "r")
# reader = csv.reader(file)
# for row in file:
#     if booksByAuthor in str(row):
#         print(row)
#         bookCount += 1
# if bookCount == 0:
#     print("There are no books by that author")


# * 114
# * Using the Books.cs file, ask the user to enter a starting year and an end year. Display all books released between those two years.
# startQuery = int(input("Enter a starting year to search from: "))
# endQuery = int(input("Enter a ending year to search from: "))
# file = list(csv.reader(open("Books.csv")))
# tempList = []
# for row in file:
#     tempList.append(row)
# for i in tempList:
#     if startQuery <= int(i[2]) <= endQuery:
#         print(i)


# * 115
# * todo Using the Books.csv file, display the data in the file along with the row number of each.
# file = csv.reader(open("Books.csv"))
# tempList = []
# for row in file:
#     print(f"Index: {file.line_num}, book: {row}")


# * 116
# * Import the data from the Books.cv file into a list. Display the list to the user. Ask them to select which row from the list they want to delete and remove it from the list. Ask the user which data they want to change and allow them to change it.
# * Write the data back to the original cv file, overwriting the existing data with the amended data.
# open file, copy data to a new list row by row
file = list(csv.reader(open("Books.csv")))
bookList = []
for row in file:
    bookList.append(row)


for row in bookList:
    print(f"{bookList.index(row)}, {row}")

# Ask for user input within list length bounds
# delete selected book by index from list
choice = int(input("Choose an index number to delete a book from the list: "))
while choice < 0 or choice > len(bookList):
    choice = int(input("That index is out of range, please try again: "))
print(f"Deleting {bookList[choice]}...")
del bookList[choice]

for row in bookList:
    print(f"{bookList.index(row)}, {row}")

# Get user input to alter a book
alteration = int(input("Which entry would you like to alter? "))
for i in bookList[alteration]:
    print(f"{bookList[alteration].index(i)}, {i}")

# Get user input for which field to change eg title, autor, date
alterationPart = int(input("Which part would you like to alter? "))
newData = input("Write your new change: ")
bookList[alteration][alterationPart] = newData
print(bookList[alteration])

# After amendments, write new data back to csv file and save/close
file = open("Books.csv", "w")
x = 0
for row in bookList:
    newRecord = bookList[x][0] + "," + bookList[x][1] + "," + bookList[x][2] + "\n"
    file.write(newRecord)
    x += 1
file.close()
