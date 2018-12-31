# for github
# works both on Windows and on Linux
# python 3 required
from math import sqrt
from datetime import datetime
import os
import time
def main():
    try:
        print('+-----------------+'), print('|    PyMaths      |'), print('| a) addition     |'), print('| b) subtraction  |'), print('| c) multiply     |'), print('| d) division     |'), print('| e) square root  |'), print('| f) modulos      |'), print('| g) odd/even nr. |'), print('| h) about pymaths|'), print('-------------------')
        print('[PyMaths] script started at', datetime.now(), '!')
        print('Entering an invalid operation will restart the script.')
        usr_choice = input(">> Operation: ")
        if(usr_choice == 'a' or usr_choice == 'a)'):
            addition()
        elif(usr_choice == 'b' or usr_choice == 'b)'):
            subtraction()
        elif(usr_choice == 'c' or usr_choice == 'c)'):
            multiply()
        elif(usr_choice == 'd' or usr_choice == 'd)'):
            division()
        elif(usr_choice == 'e' or usr_choice == 'e)'):
            squareroot()
        elif(usr_choice == 'f' or usr_choice == 'f)'):
            modulos()
        elif(usr_choice == 'g' or usr_choice == 'g)'):
            oddoreven()
        elif(usr_choice == 'h' or usr_choice == 'h)'):
            pymathsinfo()
    except Exception as error:
        print(error)
def addition():
    try:
        numberX = int(input("x (first number) = "))
        numberY = int(input("y (second number) = "))
        print('x + y =', float(numberX + numberY), '( where x is', numberX, 'and y is', numberY, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def subtraction():
    try:
        numberX = int(input("x (first number) = "))
        numberY = int(input("y (second number) = "))
        print('x - y =', float(numberX - numberY), '( where x is', numberX, 'and y is', numberY,')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def multiply():
    try:
        numberX = int(input("x (first number) = "))
        numberY = int(input("y (second number) = "))
        print('x * y =', float(numberX * numberY), '( where x is', numberX, 'and y is', numberY, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def division():
    try:
        numberX = int(input("x (first number) = "))
        numberY = int(input("y (second number) = "))
        print('x : y =', float(numberX / numberY), '( where x is', numberX, 'and y is', numberY, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def squareroot():
    try:
        numberX = int(input("x (the number) = "))
        print('The square root of x is', sqrt(float(numberX)), '( where x is', numberX, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def modulos():
    try:
        numberX = int(input("x (first number) = "))
        numberY = int(input("y (second number) = "))
        print('x % y =', float(numberX % numberY), '( where x is', numberX, 'and y is', numberY, ')')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def pymathsinfo():
    try:
        if (os.name == 'nt'):
            windowsconsoleclear()
        else:
            linuxconsoleclear()
        print("-+-+-+-+-+-+-+-+-+-+-+-+"), print("| author: Dragan Cezar |"), print("| version: 0.4.3       |"), print("| os: Windows and Linux|"), print("-+-+-+-+-+-+-+-+-+-+-+-+"), print("This message will disappear in 5 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 4 seconds, restaring the script !"), time.sleep(1), print("This message will disappear in 3 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 2 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 1 second, restarting the script !"), time.sleep(1.2)
        if (os.name == 'nt'):
            windowsconsoleclear()
        else:
            linuxconsoleclear()
        main()
    except Exception as error:
        print(error)
        main()
def oddoreven():
    try:
        numberX = int(input("x (the number) = "))
        if (numberX % 2 == 0):
            print(numberX,'is an even number because x % 2 = 0', '( x is', numberX, ') !')
        else:
            print(numberX,'is an odd number because x % 2 is not equal to 0', '( x is', numberX, ') !')
        calculateagain = input("Would you like to run the script again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print(error)
        calculateagain = input("An error has occured. Would you like to run the script again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def windowsconsoleclear():
    os.system('cls')
def linuxconsoleclear():
    os.system('clear')
main()
calculateagain = 'Y'
while (calculateagain == 'Y' or calculateagain == 'y'):
    if (os.name == 'nt'):
        windowsconsoleclear()
    else:
        linuxconsoleclear()
    print("The script has been restarted !")
    main()
