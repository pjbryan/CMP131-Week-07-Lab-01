# PJ Bryan
# CMP-131-80230
# Week 07
# Lab 01
# Assignment 07
# 10/27/2026


# PROGRAM TITLE AND DIVIDERS
divider1 = "*******************"
divider2 = "-------------------"
print ("FAST FREIGHT SHIPPING CALCULATOR", divider1)
print()

# ASK AND STORE USER INPUT
packageWeight = float(input("Enter package weight (kilograms): "))

# VALIDATE PACKAGE WEIGHT
while packageWeight <= 0 or packageWeight >20:
  print ("ERROR! Must be more than 0 and no more than 20!")
else:
  print ("Your package size: ", packageWeight)
packageWeight = float(input("Enter package weight (kilograms): "))

# SHIPPING 
