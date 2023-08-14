# A program to help calculate car rental costs.
# Author: Tanner Jones
# Date Written: Jan,12th 2023

#Gathering Customer information from user
CustName = input("What is the customers name: ")
Phone = input("What is their Phone Number: ")
NumDays = int(input("How Many Days was the car rented:"))
MilageRent = float(input("How many kilometers did the car have when rented: "))
MilageReturn = float(input("How many kilometers did the car have when returned: "))

#Listing Constants

Day = 35

Km = 0.10

HSTrate = 0.15

#Performing required calculations

Tottravel = (MilageReturn - MilageRent)
DayCost = NumDays * Day
Rentcost = DayCost + (Tottravel * Km)
HST = (DayCost * HSTrate)
TotCost = Rentcost + HST

#Displaying Requried outputs

print()
print("Customer Name:", CustName)
print("Customer Phone Number:", Phone)
print("Number of days rented:", NumDays)
print("Number of KM at rental:", MilageRent)
print("Number Of KM after rental:", MilageReturn)

print()
print("-"*50)  #Spacing Inputs from Calculations
print()

print("Total Km Traveled:", Tottravel)
print("The cost to rent the car:$", Rentcost)
print("HST Tax on Daily Cost of rental:$", HST)
print("Total cost with HST:$", TotCost)