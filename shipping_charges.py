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

# Ask user for package weight
packageWeight = float(input("Enter package weight (kilograms): "))

# Validate package weight
while packageWeight <= 0 or packageWeight > 20:
  print ("ERROR! Must be more than 0 and no more than 20!")
  packageWeight = float(input("Enter package weight (kilograms): "))

# Ask user for shipping distance
shippingDistance = int(input("Enter shipping distance (miles): "))

# Validate shipping distance
while shippingDistance < 10 or shippingDistance > 3000:
  print ("ERROR! Distance must be between 10 and 3,000 miles.")
  shippingDistance = int(input("Enter shipping distance (miles): "))

# Determine shipping rate
if packageWeight <= 2:
  shippingRate = 1.10
elif packageWeight <= 6:
  shippingRate = 2.20
elif packageWeight <= 10:
  shippingRate = 3.70
else:
  shippingRate = 4.80

# Calculate shipping charge
shippingCharge = shippingRate * (shippingDistance / 500)

# Summary
print ("SUMMARY", divider2)
print (f"Package weight: {packageWeight:.2f} kilograms.")
print (f"Shipping distance: {shippingDistance:,} miles.")
print (f"Shipping rate per 500 miles: ${shippingRate:.2f}")
print (f"Total shipping charge: ${shippingCharge:,.2f}")

