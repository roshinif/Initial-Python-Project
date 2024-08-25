# Exercises 1
## 1.
# from random import random

print("Hello, Roshini Fernando!")

# Exercises 2
# 1
name = input("What is your name?")
print(f"Hello, {name}! ,")

# 2
import math
radius = float(input("What is the radius of a circle?"))
print("The area of a circle is:", math.pi * radius ** 2)

# 3
length = float(input("What is the length of a rectangle?"))
width = float(input("What is the width of a rectangle?"))
perimeter = 2 * length + 2 * width
area = length * width
print(f"The perimeter of a rectangle is:,{perimeter} ")
print(f"The area of a rectangle is:,{area} ")

# 4
num1 = int(input("Write three integer numbers:"))
num2 = int(input())
num3 = int(input())
print(f"Sum of 3 numbers is: {num1 + num2 + num3}, product {(num1 + num2 + num3)/3}, average {(num1 + num2 + num3)/3}")

# 5
print("Enter talents:")
talents = float(input())
print("Enter pounds")
pounds = float(input())
print("Enter lots")
lots = float(input())
kilograms = ((talents*20+pounds)*32 + lots)*8.8133
grams = 1000.0*(kilograms - int(kilograms))
print(f"The weight in modern units: \n{int(kilograms)} kilograms and {grams:.2f} grams")


# 6
import random
numbers1 = random.randint(0,9)
numbers2 = random.randint(0,9)
numbers3 = random.randint(0,9)
print(f"first combination: {numbers1},{numbers2},{numbers3}")

numbers4 = random.randint(1,6)
numbers5 = random.randint(1,6)
numbers6 = random.randint(1,6)
numbers7 = random.randint(1,6)
print(f"second combination: {numbers4},{numbers5},{numbers6},{numbers7}")










