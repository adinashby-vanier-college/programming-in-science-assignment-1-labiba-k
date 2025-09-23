# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    return max(num1, num2, num3)

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    return min(num1, num2, num3)

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    for i in range(1, rows + 1):
        return "\n".join("*" * i for i in range(1, rows +1))

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
        return "\n".join(
            "Multiple of 3" if i % 3 == 0 else str(i)
            for i in range(1, limit + 1)
        )

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)

# Function 7: Do-While Loop Simulation – Ask for Positive Number
# This function should return the first positive number input by the user.
def ask_for_positive():
    while True:
        num = int(input("Enter a positive number: "))
        if num > 0:
            return num

# Test functions

if __name__ == "__main__":

   # Test 1
   print("---Test 1---")
   num1 = int(input("First number: "))
   num2 = int(input("Second number: "))
   num3 = int(input("Third number: "))
   print("Maximum is:", built_in_functions_max(num1, num2, num3))

   # Test 2
   print("---Test 2---")
   num1 = int(input("First number: "))
   num2 = int(input("Second number: "))
   num3 = int(input("Third number: "))
   print("Minimum is: ", built_in_functions_min(num1, num2, num3))

   # Test 3
   print("---Test 3---")
   num = int(input("Enter a number: "))
   print(check_number(num))

   # Test 4
   print("---Test 4---")
   rows = int(input("Rows: "))
   print(star_shape(rows))

   # Test 5
   print("---Test 5---")
   print(count_multiples_of_3(20))

   # Test 6
   print("---Test 6---")
   start = int(input("Enter the start of the range: "))
   end = int(input("Enter the end of the range: "))
   print("Sum of even numbers:", sum_of_even_numbers(start, end))

   # Test 7
   print("---Test 7---")
   print("You entered:", ask_for_positive())
