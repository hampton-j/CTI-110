
""""


print("test program")
count = 1
while count < 5:
    print ("count is", count)
    count = count + 1
print("done")




for number in range(5):
    print(number)
print("done")


# input validation
 num = int(input("Type a number from 1 to 3:"))
 while num < 1 or num > 3:
     print("Please try again")
     num = (int(input("Type a number from 1 to 3:"))
print("you entered", num)
"""


# P4LAB2 - Times Table
# CTI 110
# 11/14/24
# hamptonj
# ask for a number that is 0 or higher
# then display times table for that number
# from times 1 to times 12
# finally repeat if they want

def times_table():
    
    num = int(input("Enter an integer: "))
    print("No negative numbers please. ")
    num = int(input("Enter an integer: "))
    print("You entered", num)
    # finally do the times table
    for num2 in range(12):
        answer = num * num2 
        print(num, "*", num2,"=",answer)

def main():
    times_table()
    again = input("Do you want to run again? ")
    while (again == "yes"):
        times_table()
        again = input("do you want to run again? ")
    print("Goodbye!")

# start program
main()
    
