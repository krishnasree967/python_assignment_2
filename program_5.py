# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
#For example: calculate the factorial of 5

number = int(input("Enter a number: "))
if number < 0:
    print("Enter positive number")
else:
    factorial = 1
    for i in range(1, number + 1):
      factorial *= i
    print(f"factorial of given number is: {factorial}")

