
#Input Validation Ch 8

from urllib import response


while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

# import PyinputPlus module
#run pip install --user pyinputplus


response = 

