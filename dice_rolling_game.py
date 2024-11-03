# Ask: roll the dice?
# If user enters y
    # Generate a random number
    # Print them
# If user enters n
    # print thank you message
    # terminate the program
# Else
    # print invalid choice

import random

while True:
    choice = input('Roll the dice? (y/n)').lower()
    if choice == 'y':
        random_number1 = random.randint(1, 6)
        random_number2 = random.randint(1, 6)
        print(f'{random_number1},{random_number2}')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Please enter y or n.')
