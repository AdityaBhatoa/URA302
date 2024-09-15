# Twinkle, Twinkle, Little Star Poem
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")


# Input first and last name, then print in reverse order
fname = input("Enter your given name: ")
lname = input("Enter your surname: ")

print(f"{lname} {fname}")


# Calculate the area of a circle given its radius
import math

rad = float(input("Input the circle's radius: "))

circle_area = math.pi * rad ** 2
print(f"The circle's area is: {circle_area}")


# Display first and last colors from a list
colors = ["Red", "Green", "White", "Black"]

print(f"First: {colors[0]}, Last: {colors[-1]}")


# Perform a calculation based on input number n
n_value = input("Provide a number: ")

nn_value = n_value * 2
nnn_value = n_value * 3

calculated_result = int(n_value) + int(nn_value) + int(nnn_value)
print(f"Result of n + nn + nnn: {calculated_result}")


# Convert a comma-separated string into a list and tuple
nums = input("Enter values separated by commas: ")

num_as_list = nums.split(",")
num_as_tuple = tuple(num_as_list)
print(f"List: {num_as_list}")
print(f"Tuple: {num_as_tuple}")


# Convert Celsius temperature to Fahrenheit
temp_celsius = float(input("Input temperature in Celsius: "))

temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {temp_fahrenheit}")


# Swap and increment two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
x, y = y, x

x += 1
print(f"After swapping and adding 1: First number: {x}, Second number: {y}")


# Check if a number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# Check if a year is a leap year
yr = int(input("Enter a year: "))

if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")


# Calculate Euclidean distance between two points
x1, y1 = map(float, input("Provide coordinates for point 1 (x1, y1): ").split())
x2, y2 = map(float, input("Provide coordinates for point 2 (x2, y2): ").split())

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between the points is: {dist}")


# Check if three angles can form a triangle
ang1 = float(input("First angle: "))
ang2 = float(input("Second angle: "))
ang3 = float(input("Third angle: "))

if ang1 + ang2 + ang3 == 180:
    print("These angles form a triangle")
else:
    print("These angles do not form a triangle")


# Calculate compound interest
principal = float(input("Principal amount: "))
rate = float(input("Interest rate: "))
time = float(input("Time in years: "))
compoundings_per_year = float(input("Compoundings per year: "))

total_amount = principal * (1 + rate / (100 * compoundings_per_year)) ** (compoundings_per_year * time)
interest = total_amount - principal
print(f"The compound interest is: {interest}")


# Check if a number is prime
number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


# Calculate sum of squares of numbers up to N
N = int(input("Enter a positive integer: "))

sum_of_squares = sum(i ** 2 for i in range(1, N + 1))
print(f"Sum of squares from 1 to {N}: {sum_of_squares}")
