## Author: Feras Isied
## Description: A program to check if the user provided number is odd or even
## Formula: A number is even if number % 2 == 0
##          A number is odd if number % 2 == 1

userNum = float(input('Please enter a number: \n')) 

if (userNum % 2) == 0:
    print('The number', userNum, 'is an even number!')
elif (userNum % 2 ) == 1:
    print('The number', userNum, 'is an odd number!')
else:
    print('Error, please enter a valid number!')
