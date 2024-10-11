
# CTI 110
# P1HW2
#J Hampton
# 10/8/24
# This program does a travel budget 
"""
3. Ask user to enter their budget 
4. Ask user to enter travel destination
5. Ask user for amount they will spend on gas 
6. Ask user for amount they will spend on accommodation 
7. Ask user for amount they will spend on food 
8.Add expenses
9.Subtract expenses from budget 
10. Display results 
"""
print (" Trip Calculator ")
# ask user to enter their budget
budget = float(input("What is your travel budget? $ "))
# Where are they going
dest = input("Where are you are going? ")
gas = float(input ("how much is spent on gas? "))
hotel = float(input("how much is spent on hotel? "))
food = float(input ("how much is spent on food? "))
expenses = gas + food + hotel
remaining = budget - expenses
print("----------TravelExpenses--------")
print("location:", dest)
print("Initial Budget:", budget)
print("fuel:", gas)
print ("accomodation:",hotel)
print("food:",food)
print("total",expenses)
print("remaining balance:",remaining)
