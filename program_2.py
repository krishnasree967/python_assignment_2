# Count the total number of digits in a number.
# Write a program to count the total number of digits in a number using a while loop., For example, the number is 75869, so the output should be 5.


def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

user_num = 75869
total_digits = count_digits(user_num)
print(f"number of digits in {user_num} is: {total_digits}")