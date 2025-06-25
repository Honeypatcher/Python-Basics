#Python Basics assignment
#Variables
#declare a variable and assign age to it
age =27
#Create two variables x = 10 and y = 5. Print their sum.
x = 10
y = 5
print(x + y)
#Using an invalid name to observe and note down the error
#2ndName = "Lux" >>The outcome of the code has been explained below.
#The error noted from running the above syntax captures an invalid decimal literal, due to
#the use of an alphanumeric statement to declare the variable.2ndNmame is also not defined
#Assign a string a variable and print it
name = "Jessica J"
age = 34
print("My name is", name,"and I am", age,"years old.")
#Challenge exercise 1
#Write a program that asks the user to input their name and age, and then prints a greeting.
#In this program we will use the f string format

name = input("What is your name? ")
age = input("What is your age? ")
#Printing a greeting in the message
print(f"Salutations,{name}! You are turning {age} years old.")

#2. DATA TYPES:EXCERCISE 
#Print the type of 42, 3.14, and 'hello'.
print(type(42))
print(type(3.14))
print(type('hello'))
#Convert '100' which is a string to an integer
#we are going to use the int function
s = '100'
num = int(s)
print(num)
#Add an integer and a float together. What is the result?
#Integer(x) and float(y)
x = 10
y = 3.14
print(x + y)
#What happens when you try to multiply a string by a number?
kgs = [56,76,89,54,90]
weight = kgs *10
print(weight)
#Challenge 2
#Write a program that:
#Asks the user to enter two numbers (as strings)
#Converts them to integers or floats
#Prints their sum and type
# Ask the user to input two numbers
#The Program below
x_1 = input("Enter the first number: ")
x_2 = input("Enter the second number: ")

# Convert the inputs to float (works for both integers and decimals)
x_1 = float(x_1)
x_2 = float(x_2)

# Calculate the sum
total = x_1 + x_2

# Print the sum and its data type
print("The sum is:", total)
print("The type of the result is:", type(total))
#Since th total was 79, we add 0.0 to the total to make it a float

#3. Data Structures
#Create a list of 5 fruits and print the third fruit.
fruits= ['mango','kiwi','banana','orange','apple','pawpaw']
print(fruits[2])
#Create a dictionary with keys: name, age. Print the value of age.
dict = {"name": "Wantam","age":5}  
print(dict["age"])
#Define a tuple with three numbers. Try modifying it. What happens?
oil = (40,55,67)
print(x)
#modifying the tuple
#oil[0] = 59
#print(oil)
#whn you try to modify the tuple you get an error
#Create a set from a list with duplicate values.
sales = [89,89,56,43,78,78,89] #list
revenue = set(sales)
print(revenue)
#Challenge 3
#Create a program that:

#Takes 5 user inputs and stores them in a list
#Converts the list into a set and prints the unique values
# Create an empty list to store inputs
shrek = []

# Take 5 inputs from the user
for k in range(5):
    value = input(f"Enter value {k+1}: ")
    shrek.append(value)

# Convert the list to a set to remove duplicates
unique_values = set(shrek)

# Print the results
print("Original List:", shrek)
print("Unique Values (Set):", unique_values)


#FOR LOOPs
#Exercise
#Use a for loop to print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#Use a while loop to print numbers until the user enters stop.
while True:
    user_input = input("Enter a number (or type 'stop' to end): ")
    
    if user_input.lower() == "stop":
        print("Program stopped.")
        break
    else:
        print("You entered:", user_input)
#Write a loop that prints even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)
    
#Explain what break and continue do in your own words
#Break- used inside a for/ while loop to terminate a program when a condition has been met
#Continue - In a for loop, it forces the code to go to its next iteration
#in a while loop it re-evaluates the assigned condition, if found to be True, starts a new iteration
#Challenge
#Write a guessing game that asks the user to guess a secret number between 1 and 10.

#Give feedback (too high / too low)
#Use a while loop.

#Import libraries
import  random
#syntax
def number_guessing_game():
    number = random.randint(1, 10)

    player_name = input("Hello, What's your name? ")
    number_of_guesses = 0

    print("Okay, " + player_name + "! I am guessing a number between 1 and 10:")

    while number_of_guesses < 5:
        guess = int(input())
        number_of_guesses += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            print('Correct! You guessed it.')
            break
        
#Control Flow
#Exercise
#Write a program that checks if a number is positive, negative, or zero.
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is 0.")
    
#Write a programme to see if someone is eligible to vote
age = int(input("Enter age : "))

if age >= 18:
    print("Eligible for Voting!")
else:
    print("Not Eligible for Voting!")

#Write a program that takes 3 numbers and prints the largest one.
# Get 3 numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest
largest = max(num1, num2, num3)

# Print the result
print("The largest number is:", largest)

#Practice combining and, or, not.
# Input age and nationality
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()

# and
if age >= 18 and nationality == "Egypt":
    print("You are eligible to vote in Egypt.")
else:
    print("You are NOT eligible to vote in Egypt.")

# or
if age < 10 or age > 57:
    print("You are eligible for a discount.")
else:
    print("No discount available.")

# not
has_ticket = input("Do you have a ticket? (yes/no): ").lower()
if not has_ticket == "yes":
    print("You need a ticket to enter.")
else:
    print("Welcome!")

#CHALLENGE 5
#Build a grading system:

#Input score (0–100)
#Output grade: A (90+), B (80–89), etc.
try:
    marks = float(input("Please enter the marks (0-100): "))
    # Validate the marks are within a plausible range (0-100)
    if 0 <= marks <= 100:
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print("Grade:", grade)
    else:
        print("Invalid marks. Please enter a value between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    
#FUNCTIONS
#Write a function greet(name) that prints “Hello, [name]”.
def say_hello(name):
    name = input("What is your name? ")
    if name == input(name):
        return("HEY," + name + "!" )
    else: 
        return("Hey there!")
#Create a function add(a, b) that returns the sum.
#Identifying the variables
a = 7
b = 9

def add(a, b):
    return a + b
#calling the function
res = add(a,b)
print(res)

#Modify add() to print “even” or “odd” based on the result.
def add(m, n):
    result = m + n
    print(f"Result: {result}")
    
    if result % 2 == 0:
        print("even")
    else:
        print("odd")


#Call a function from within another function.
def square(z):
    y = z*z
    return y
def sum_of_squares(x,y, z):
    a = square(z)
    b = square(y)
    c = square(x)
    return a + b + c
a = 10
b = -4
c = 7
result = sum_of_squares(a,b,c)
print(result)

#Challenge 6.
#Write a calculator function:

#Takes two numbers and an operation (+, -, *, /)
#Returns the result

def calculator(c, d, operation):
    if operation == '+':
        return c + d
    elif operation == '-':
        return c - d
    elif operation == '*':
        return c * d
    elif operation == '/':
        if c == 0:
            return "Error: Division by zero"
        return c / d
    else:
        return "Error: Unsupported operation"
print(calculator(10, 5, '+'))  # 15
print(calculator(10, 2, '/'))  # Error: Division by zero
print(calculator(7, 3, '*'))   # 21
print(calculator(9, 2, '^'))   # Error: Unsupported operation
