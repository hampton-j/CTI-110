# Hampton Jaiden 

# 12/6/24

# P3HW2

# Calculating employees salary



employee = input(" Enter name of employee: ")

hours = float(input("Enter number of hours worked: "))

pay_rate = float(input("Enter employees pay rate: "))


if hours >40:
    net_pay = pay_rate*40

    over_time = pay_rate*1.5

    over_time_hours = hours-40

    over_time_pay = over_time * over_time_hours

    gross_pay = net_pay + over_time_pay

 
else:
    net_pay = hours*pay_rate

    over_time_pay = 0

    gross_pay = 0
    

print("---------------------------")


print("Employee name: ")

print("Hours Worked     Pay Rate      OverTime      OverTime Pay    RegHour pay      Gross Pay")

print(f'{hours:<pay_ratef} {over_time:<over_time_payf}') (f'{net_pay:<gross_payf}')

      
