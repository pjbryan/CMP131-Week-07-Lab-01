# PJ Bryan
# CMP-131-80230
# Week 07
# Lab 01
# Assignment 07
# 10/27/2026


# Program title and dividers
divider1 = "*******************"
divider2 = "-------------------"
print ("SUM OF NUMBERS", divider1)

# User input
number = int(input("Enter a positive integer: "))

# Validate input
while number <=0:
  print ("ERROR! Must be a positive integer greater than 0.")
  number = int(input("Enter a positive integer: "))

# Accumulator
total = 0

# Summation
for currentNumber in range (1, number + 1):
  total += currentNumber

# Summary
print (divider2)
print ("Number entered:", number)
print ("Sum of number from 1 through", number, "is:" , total)
