# import math
from math import *

print("-------------------------------------")
# print Hello World
print("Hello World!")
print("-------------------------------------")

# draw a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
print("-------------------------------------")

# variables & data types
first_name = "John"
last_name = "Doe"
age = 30
is_Married = False
print(first_name, last_name, age, is_Married)
print("-------------------------------------")

# working with strings
print("John\nDoe")
phrase = "HELLO WORLD!"
print("phrase.lower():", phrase.lower()) # or .upper()
print("phrase.isupper():", phrase.isupper()) # or .islower()
print("len(phrase):", len(phrase)) # length of string
print("phrase[0]:", phrase[0]) # first character
print("phrase.index('O'):", phrase.index('O')) # index of first occurence of 'o'
print("phrase.replace('H', 'Y'):", phrase.replace('H', 'Y')) # replace first occurence of 'H' with 'Y'
print("-------------------------------------")

# working with numbers
print(2.0987)
print(-2.0987)
print(3 + 4)
print(10 % 3)
my_num = -5
print(str(my_num) + " is my number") # convert number to string
print("abs(my_num):", abs(my_num)) # absolute value
print("pow(3, 2):", pow(3, 2)) # 3 to the power of 2
print("max(4, 6):", max(4, 6)) # max of 4 and 6
print("min(4, 6):", min(4, 6)) # min of 4 and 6
print("round(3.7):", round(3.7)) # round to nearest integer
print("floor(3.7):", floor(3.7)) # round down to nearest integer
print("ceil(3.7):", ceil(3.7)) # round up to nearest integer
print("sqrt(36):", sqrt(36)) # square root
print("-------------------------------------")

# getting user input
name = input("Enter your name: ")
print("Hello", name)
age = input("Enter your age: ")
print("You are", age, "years old")
print("-------------------------------------")

# working with lists
my_list = [1, 2, 3]
print("my_list:", my_list)
print("my_list[1]:", my_list[1])
print("my_list[-1]:", my_list[-1])
print("my_list[1:]:", my_list[1:])
print("my_list[0:2]:", my_list[0:2])
my_list[1] = 4
print("my_list:", my_list)
print("-------------------------------------")

# working with list methods
numbers = [5, 2, 9, 6, 3, 1, 8]
lucky_numbers = [4, 8, 15, 16, 23, 42]
numbers.extend(lucky_numbers)
numbers.append(27)
numbers.insert(0, 77)
print("numbers:", numbers)
print("max(numbers):", max(numbers))
print("min(numbers):", min(numbers))
print("sum(numbers):", sum(numbers))
print("len(numbers):", len(numbers))

print("-------------------------------------")