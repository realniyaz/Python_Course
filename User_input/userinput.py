# Get input from the user and store it in a variable

# 1. Getting a string input:
name = input("Enter your name: ")
print("Hello, " + name + "!")  # Output: Hello, [user's name]!

# 2. Getting an integer input:
try:  # Use a try-except block to handle potential errors
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")  # Output: You are [age] years old.
except ValueError:
    print("Invalid input. Please enter a number for age.")

# 3. Getting a float input:
try:
    height = float(input("Enter your height in meters: "))
    print("Your height is", height, "meters.") # Output: Your height is [height] meters.
except ValueError:
    print("Invalid input. Please enter a number for height.")

# 4. Getting multiple inputs on the same line (separated by spaces):
try:
    num1, num2 = map(int, input("Enter two numbers separated by spaces: ").split())
    print("The sum of the two numbers is:", num1 + num2)
except ValueError:
    print("Invalid input. Please enter two numbers separated by spaces.")

# 5. Getting input with a prompt that stays on the same line:
import sys
print("Enter your favorite color: ", end="")  # The 'end=""' prevents a newline
favorite_color = sys.stdin.readline().strip() # Reads line from input and removes any leading/trailing spaces
print("Your favorite color is", favorite_color + ".") # Output: Your favorite color is [favorite_color].


# Example combining different input types:
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (in meters): "))

    print("\n--- User Information ---") # \n adds a newline for better formatting
    print("Name:", name)
    print("Age:", age)
    print("Height:", height, "meters")

except ValueError:
    print("Invalid input. Please check your age and height.")
