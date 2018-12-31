# for github
# works only on Linux because of the console clear function
# python 3 required
import math
import os
import time
def main():
    try:
        print('+----------------+'), print('|    PyMaths      |'), print('| a) addition     |'), print('| b) subtraction  |'), print('| c) multiply     |'), print('| d) division     |'), print('| e) square root  |'), print('| f) about pymaths|'), print('-------------------')
        print('Entering an invalid operation will restart the script.')
        usr_choice = input(">> Operation: ")
        if(usr_choice == 'a' or usr_choice == 'a)'):
            print("\n"), addition()
        elif(usr_choice == 'b' or usr_choice == 'b)'):
            subtraction()
        elif(usr_choice == 'c' or usr_choice == 'c)'):
            multiply()
        elif(usr_choice == 'd' or usr_choice == 'd)'):
            division()
        elif(usr_choice == 'e' or usr_choice == 'e)'):
            squareroot()
        elif(usr_choice == 'f' or usr_choice == 'f)'):
            pymathsinfo()
        else:
            print(usr_choice,'is an invalid operator !')
    except Exception as error:
        print(error)
def addition():
    try:
        numberA = int(input("Enter the first number (x): "))
        numberB = int(input("Enter the second number (y): "))
        print('x + y =', numberA + numberB, '( where x is', numberA, 'and y is', numberB, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def subtraction():
    try:
        numberA = int(input("Enter the first number (x): "))
        numberB = int(input("Enter the second number (y): "))
        print('x - y =', numberA - numberB, '( where x is', numberA, 'and y is', numberB,')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def multiply():
    try:
        numberA = int(input("Enter the first number (x): "))
        numberB = int(input("Enter the second number (y): "))
        print('x * y =', numberA * numberB, '( where x is', numberA, 'and y is', numberB, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def division():
    try:
        numberA = int(input("Enter the first number (x): "))
        numberB = int(input("Enter the second number (y): "))
        print('x : y =', numberA / numberB, '( where x is', numberA, 'and y is', numberB, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def squareroot():
    try:
        numberA = int(input("Enter the number (x): "))
        print('The square root of x is', math.sqrt(numberA), '( where x is', numberA, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def pymathsinfo():
    try:
        print("\nPyMaths is a simple calculator script made in Python 3.6.7.\nIt can be really useful for maths operations !\nThe reason for why PyMaths works only on Linux is because of the clear console function.\nIn 5 seconds, the script will be restarted !"), time.sleep(5), os.system('clear')
        print("The script has been restarted !")
        main()
    except Exception as error:
        print(error)
        main()
main()
calculateagain = 'Y'
while (calculateagain == 'Y' or calculateagain == 'y'):
    os.system('clear')
    print("The script has been restarted !")
    main()
