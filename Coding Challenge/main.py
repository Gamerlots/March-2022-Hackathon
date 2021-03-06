# Write a program that prints all the integers from 1 to 100 except the multiples of 10.

# for number in range(1, 101):
#     if number % 10 != 0:
#         print(number)





# Print the letters of "YoungWonks" in different lines using a for loop.

# for letter in "YoungWonks":
#     print(letter)





# Using a while loop, print from 30 to 1.

# number = 30
# while number > 0:
#     print(number)
#     number -= 1





# Create a list of five car names. Sort the list in alphabetical order and print the car names in different lines.

# names = ["Toyota", "Honda", "Mercedes", "BMW", "Lexus"]
# names.sort()

# for name in names:
#     print(name)





# Create an empty list. Use the random module to put 10 random integers into the list. 
# The integers should be in range from -100 to 25. Print the list.

# from random import randint

# numbers = []

# for _ in range(10):
#     numbers.append(randint(-100, 25))

# print(numbers)





# Create the following list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Use nested loops to print the content of this 2D list in the form of rows and columns as shown below.
# 123
# 456
# 789

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in numbers:
#     for column in row:
#         print(column, end="")
#     print()





# Create a dictionary to store the names of four people as keys and their age as values. 
# Print the names of only those people who are at least 16 years of age.

# names = {"John": 10, "Beth": 29, "Doe": 78, "Adam": 16}

# for name, age in names.items():
#     if age >= 16:
#         print(name)





# Create a dictionary with the names of five fruits as keys and their respective prices as values. Find the sum of all the prices and print it.
# Tip: Use dictionary_name[key] to get the value of a key in a dictionary.

# fruits = {"Apples": 1, "Bananas": 10, "Strawberries": 4, "Mangoes": 6, "Tomatoes": 9}
# total_price = 0

# for price in fruits.values():
#     total_price += price

# print(total_price)





# Use nested while loops to generate the Chess board as shown below. The print function must print only one character at a time.
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB
# BWBWBWBW
# WBWBWBWB

# row = 1
# column = 1

# while row < 9:
#     while column < 9:
#         if (row + column) % 2:
#             print("W", end="")
#         else:
#             print("B", end="")
#         column += 1
#     print()

#     row += 1
#     column = 1





# Write a function that takes a list as an argument. The function picks one of the elements of the list using the random module and prints it. 
# Call the function two times.

# from random import choice

# def pick_random(list_of_numbers):
#     random_number = choice(list_of_numbers)
#     print(random_number)


# numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers_2 = [10, 11, 12, 13]

# pick_random(numbers_1)
# pick_random(numbers_2)





# Create an empty list. Keep on adding random integers in the range 1 to 100 (including both end points) to the list 
# till the list contains five integers that are multiples of both 2 and 5. Print the list.
# Example of such a list: [10, 60, 70, 50, 40].

from random import randint

numbers = []
counter = 0

while counter < 5:
    number = randint(1, 100)

    if number % 2 == 0 and number % 5 == 0:
        counter += 1
    
    numbers.append(number)


print(numbers)
