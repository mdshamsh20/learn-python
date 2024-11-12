Importing Modules





import math  # Import the math module to access advanced mathematical functions like math.ceil()




Variables and Basic Operations

student_count = 1000  # Integer variable representing the number of students
rating = 4.99  # Float variable for course rating
is_published = False  # Boolean variable to track if the course is published
course_name = "Python Program"  # String variable holding the name of the course




String Operations

print(len(course_name))  # Prints the length of the string "Python Program", which is 13
print(course_name[0])  # Prints the first character of the string, 'P'
print(course_name[-1])  # Prints the last character of the string, 'm'
print(course_name[0:3])  # Slices and prints the first three characters, 'Pyt'
print(course_name[0:])  # Prints the entire string starting from index 0, "Python Program"
print(course_name[:3])  # Prints the first three characters, same as above, 'Pyt'
print(course_name[:])  # Prints the whole string, "Python Program"
print(student_count)  # Prints the value of student_count, which is 1000





String with Escape Characters

course = "python \n program"  # A string with a newline character between 'python' and 'program'
print(course)  # Prints the string with a line break between "python" and "program"




String Concatenation and Formatting

first = "mosh"  # First name
last = "hamed"  # Last name
full = first + " " + last  # Concatenates the first and last name with a space in between
full = f"{first} {last}"  # String interpolation (formatted string), combines first and last
full = f"{len(first)} {last}"  # Combines the length of 'first' (which is 4) and the last name
full = f"{len(first)} {2 + 2}"  # Combines the length of 'first' and the result of 2 + 2
print(full)  # Prints "4 4"




String Methods

course = "   Python Program    "  # String with leading and trailing spaces
print(course.upper())  # Converts the entire string to uppercase, "   PYTHON PROGRAM    "
print(course.title())  # Converts the first letter of each word to uppercase, "   Python Program    "
print(course.lower())  # Converts the string to lowercase, "   python program    "
print(course.capitalize())  # Capitalizes the first letter of the string, "   python program    "
print(course.count("o"))  # Counts how many times 'o' appears in the string, which is 2
print(course.find("o"))  # Finds the index of the first occurrence of 'o', which is 9
print(course.replace("P", "f"))  # Replaces all 'P' with 'f', "   fython frogram    "
print(course.replace("P", "f").replace("o", "d"))  # Replaces 'P' with 'f' and 'o' with 'd', "   fythdn frrdgram    "
print(course.strip())  # Removes leading and trailing spaces, "Python Program"
print(course.rstrip())  # Removes trailing spaces only, "   Python Program"
print(course.lstrip())  # Removes leading spaces only, "Python Program    "
print(len(course))  # Prints the length of the original string including spaces, 21
print("Pro" in course)  # Checks if "Pro" is in the string, returns True
print("pro" not in course)  # Checks if "pro" is not in the string, returns True because it's case-sensitive






Arithmetic Operations

print(10 + 2)  # Addition, result is 12
print(10 - 2)  # Subtraction, result is 8
print(10 * 2)  # Multiplication, result is 20
print(10 / 2)  # Division, result is 5.0 (float)
print(10 // 2)  # Integer division, result is 5 (removes decimal part)
print(10 % 3)  # Modulus, result is the remainder, which is 1
print(10 ** 2)  # Exponentiation, result is 10 squared, which is 100






Math Functions and Input/Output

x = 10  # Assigns 10 to the variable x
x = 10 + 2  # Adds 2 to x, so x is now 12
print(x)  # Prints 12
print(round(2.5))  # Rounds 2.5 to the nearest whole number, result is 2
print(abs(-2.5))  # Prints the absolute value of -2.5, result is 2.5
print(math.ceil(2.2))  # Uses math module to round 2.2 up to the next whole number, result is 3








User Input

x = input("x: ")  # Takes input from the user as a string
y = int(x) + 1  # Converts the input to an integer and adds 1
print(y)  # Prints the value of y
print(f"x: {x}, y:{y}")  # Prints the values of x and y using formatted string







String Slicing and User Input Example

fruit = "Apple"  # String 'Apple'
print(fruit[1:-1])  # Prints a slice of the string excluding the first and last character, 'ppl'
print(fruit[1])  # Prints the second character of the string, 'p'
birth_year = input("Enter your birth year: ")  # Takes user's birth year as input
age = 2024 - int(birth_year)  # Calculates age by subtracting birth year from 2024
print(age)  # Prints the calculated age







Basic Calculator with Input

First_number = input("first")  # Takes first number as input
Second_number = input("second")  # Takes second number as input
print(First_number + Second_number)  # Concatenates the two input strings
print(int(First_number) + int(Second_number))  # Adds the two input numbers
print(int(First_number) - int(Second_number))  # Subtracts the two input numbers
print(int(First_number) * int(Second_number))  # Multiplies the two input numbers
print(int(First_number) / int(Second_number))  # Divides the two input numbers
print(int(First_number) % int(Second_number))  # Finds the modulus of the two input numbers
print(int(First_number) ** int(Second_number))  # Exponentiation, first number to the power of second
print(int(First_number) // int(Second_number))  # Floor division of the two numbers
print(int(First_number) % 2)  # Checks if the first number is odd or even (remainder when divided by 2)
print(int(First_number) // 2)  # Floor division by 2
print(int(First_number) ** 2)  # First number squared







Conditional Statements

temperature = 5  # Assigns 5 to the variable temperature
if temperature > 30:  # Checks if temperature is greater than 30
    print("It's hot")  # If true, prints "It's hot"
    print("It's not hot")  # This line is incorrectly indented (it should align with the previous print)
elif temperature > 20:  # Else, checks if temperature is greater than 20
    print("its nice day")  # Prints this message if true
elif temperature > 10:  # Else, checks if temperature is greater than 10
    print("its a bit cold")  # Prints this message if true
else:  # If none of the above conditions are true
    print("its is cold")  # Prints "its is cold"







Weight Conversion

weight = float(input("Weight: "))  # Takes weight as input and converts it to a float
unit = input("(K)g or (L)bs: ")  # Asks user to specify the unit

if unit.upper() == "K":  # Checks if the unit is "K" (case-insensitive)
    converted = weight / 0.45  # Converts kilograms to pounds
    print("Weight in Lbs: " + str(converted))  # Prints the converted weight
else:  # If the unit is not "K"
    converted = weight * 0.45  # Converts pounds to kilograms
    print("Weight in Kgs: " + str(converted))  # Prints the converted weight





While Loops

i = 1  # Initialize i to 1
while i <= 50:  # Loop until i is greater than 50
    print(i)  # Prints the current value of i
    i = i + 1  # Increments i by 1 after each iteration






Nested Loop Example

i = 1  # Initialize i to 1
while i <= 10:  # Loop until i is greater than 10
    print(i * '*')  # Prints i number of '*' in each iteration
    i = i + 1  # Increments i by 1







Lists and List Operations

names = ["sachin", "BOB", "ashish", "Avanish"]  # List of names
names[0] = "Amit"  # Replaces the first element with "Amit"
print(names[0])  # Prints the first element of the list, "Amit"
print(names[2])  # Prints the third element of the list, "ashish"
print(names[-3].lower())  # Prints the second element ("BOB") in lowercase
print(names[-1].upper())  # Prints the last element ("Avanish") in uppercase







List Membership and Loops

numbers = [1, 2, 3, 4]  # List of numbers
print(1 in numbers)  # Checks if 1 is in the list, returns True
print(10 in numbers)  # Checks if 10 is in the list, returns False
print(len(numbers))  # Prints the length of the list, which is 4





For Loop

numbers = [1, 2, 3, 4, 5]  # List of numbers
for item in numbers:  # Iterates over each item in the list
    print(item)  # Prints the current item





While Loop to Iterate Over List

i = 0  # Initialize index to 0
while i < len(numbers):  # Loop until i is less than the length of the list
    print(numbers[i])  # Prints the current element in the list
    i = i + 1  # Increments i by 1






Ranges and Sequence Types

numbers = range(5, 10, 2)  # Creates a range of numbers starting from 5 to 9, stepping by 2
for number in numbers:  # Loops through the range
    print(numbers)  # Prints the range object
    print(number)  # Prints the current number in the range
print(list(numbers))  # Converts the range into a list and prints it, [5, 7, 9]
print(tuple(numbers))  # Converts the range into a tuple and prints it, (5, 7, 9)
print(set(numbers))  # Converts the range into a set and prints it, {5, 7, 9}





Tuples

numbers = (1, 2, 3, 4)  # Defines a tuple with four elements
print(numbers)  # Prints the tuple (1, 2, 3, 4)
