# PJ Bryan
# CMP-131-80230
# Week 07
# Lab 01
# Assignment 07
# 10/27/2026

# Program table and dividers
divider1 = "*******************"
divider2 = "---------------------------"
print ("CALORIES BURNED", divider1)
print ()
print (f"|{"Minutes":^8}|{"Calories Burned":^16}|")
print (divider2)

# Required variables
caloriesperMinute = 3.6
minutes = 5
caloriesBurned = 0.0

# Process and print the minute values
for minutes in range (5, 31, 5):
  caloriesBurned = minutes * caloriesperMinute
  print (f"|{minutes:^8}|{caloriesBurned:^16.1f}|")
print (divider2)