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
# file.write(str(newRecord))
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

# * 115
# * Using the Books.csv file, display the data in the file along with the row number of each.

# * 116
# * Import the data from the Books.cv file into a list. Display the list to the user. Ask them to select which row from the list they want to delete and remove it from the list. Ask the user which data they want to change and allow them to change it.
# * Write the data back to the original cv file, overwriting the existing data with the amended data.

# * 117
# * Create a simple maths quiz that will ask the user for their name and then generate two random questions. Store their name, the questions they were asked, their answers and their final score in a cv file. Whenever the program is run it should add to the .csv file and not overwrite anything.
