#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallons_cost = float(input("Enter cost per gallons:\t\t"))
# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
gas_cost = gallons_used * gallons_cost
mile_cost = gallons_cost / mpg
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(gas_cost))
print("Cost Per Mile:\t\t"  + str(mile_cost))
print()
print("Bye")


