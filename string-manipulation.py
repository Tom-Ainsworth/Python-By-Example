# * 080
# * Ask the user to enter their first name
# * then display the length of their first name.
# * Ask for their surname
# * Display the length of their surname.
# * Join their first name and surname together with a space between
# * Display the result.
# * Display the length of their full name (including the space).
# firstName = input("Enter your first name: ")
# print(len(firstName))
# surname = input("Enter your surname: ")
# print(len(surname))
# fullName = firstName + " " + surname
# print(fullName)
# print(len(fullName))


# * 081
# * Ask the user to type in their favourite school subject.
# * Display it with "-" after each letter, e.g. S-p-a-n-i-s-h-,
# favSubject = input("What's your favourite school subject? ")
# for letter in favSubject:
#     print(letter, end="-")


# * 082
# * Show the user a line of text from your favourite poem and ask for a starting and ending
# * point. Display the characters between those two points.
# poem = "The wanderer, blown off course time and again"
# print(poem)
# startPoint = int(input("choose a starting number: "))
# endPoint = int(input("choose an ending number: "))
# print(poem[startPoint:endPoint])


# * 083
# * Ask the user to type in a word in upper case. If they type it in lower case, ask them to
# * try again. Keep repeating this until they type in a message all in uppercase.
# isUpper = False
# while isUpper != True:
#     upperCaseInput = input("Enter a word in upper case ")
#     if upperCaseInput.isupper():
#         isUpper = True
#         print("Thanks, your word is: " + upperCaseInput)
#     else:
#         print("Please try again")


# * 084
# * Ask the user to type in their postcode. Display the first two letters in uppercase.
# postCode = input("Please enter your postcode ")
# print(postCode[0:2].upper())

# * 085
# * Ask the user to type in their name and then tell them how many vowels are in their name.
# userName = input("Please enter your name ").lower()
# vowels = ("a", "e", "i", "o", "u")
# vowelCount = 0
# for letter in userName:
#     if letter in vowels:
#         vowelCount += 1
# print(f"Your name has {vowelCount} vowel(s) in it")


# * 086
# * Ask the user to enter a new password. Ask them to enter it again. If the two passwords match,
# * display "Thank you". If the letters are correct but in the wrong case, display the message
# * "They must be in the same case" otherwise display the message "Incorrect".
# password1 = input("Enter your password: ")
# password2 = input("Reenter your password: ")
# if password1 == password2:
#     print("Thank you")
# else:
#     for i in range(0, len(password1)):
#         if password1[i].lower() != password2[i].lower():
#             print("Incorrect")
#             break
#         if (
#             password1[i].isupper()
#             and not password2[i].isupper()
#             or password1[i].islower()
#             and not password2[i].islower()
#         ):
#             print("They must be in the same case")
#             break


# * 087
# * Ask the user to type in a word and then display it backwards on separate lines. For instance,
# * if they type in "Hello" it should display as shown below:
# * Enter a word: Hello
# * 1
# * 1
# * e
# * H
# * >>>
userString = input("Enter a word: ")
reversed = userString[::-1]
print(reversed)
