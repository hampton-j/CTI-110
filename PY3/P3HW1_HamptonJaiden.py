#12/6/24

# Hampton

# Debug the grading module 


mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5]


low = min(grades)
max = max(grades)
sum1 = sum(grades)
avg = sum1 / len(grades)


if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
    print('Your grade is: B')

elif avg >= 70:
    print('Your grade is: C')

elif avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F') 





