from math import sqrt
from math import sin
from math import cos
from math import tan
from math import radians
from math import degrees
from math import log
from math import log10
from datetime import datetime
import os
import time
from random import randint
def main():
    try:
        print('+--------------------------------------------+'), print('|          PyMaths CMD (commands)            |'),       print('|--------------------------------------------|'),        print('| a) addition                                |'),         print('| b) subtraction                             |'),         print('| c) multiply                                |'), print('| d) division                                |'), print('| e) square root of a number                 |'), print('| f) modulos                                 |'), print('| g) check if number is odd or even          |'), print('| h) check if number is positive or negative |'),print('| i) generate a random number in an interval |'),print('| j) calculate sine (sin)                    |'),print('| k) calculate cosine (cos)                  |'),print('| l) calculate tangent (tan)                 |'),print('| m) absolute value of a number              |'),print('| n) raise a number to a power               |'),print('| p) calculate logarithm10 (log10)           |'),print('| o) calculate logarithm (log)               |'),print('| xc) details about pymaths program          |'), print('----------------------------------------------'),print('PyMaths script started at', datetime.now(), '!'),print('Entering an invalid operation will restart the script.'),print("WARNING! Float numbers are written with '.' not with ',' !")
        usr_choice = input(">> Operation: ")
        if(usr_choice == 'a' or usr_choice == 'a)' or usr_choice == 'A' or usr_choice == 'A)'):
            addition()
        elif(usr_choice == 'b' or usr_choice == 'b)' or usr_choice == 'B' or usr_choice == 'B)'):
            subtraction()
        elif(usr_choice == 'c' or usr_choice == 'c)' or usr_choice == 'C' or usr_choice == 'C)'):
            multiply()
        elif(usr_choice == 'd' or usr_choice == 'd)' or usr_choice == 'D' or usr_choice == 'D)'):
            division()
        elif(usr_choice == 'e' or usr_choice == 'e)' or usr_choice == 'E' or usr_choice == 'E)'):
            squareroot()
        elif(usr_choice == 'f' or usr_choice == 'f)' or usr_choice == 'F' or usr_choice == 'F)'):
            modulos()
        elif(usr_choice == 'g' or usr_choice == 'g)' or usr_choice == 'G' or usr_choice == 'G)'):
            oddoreven()
        elif(usr_choice == 'h' or usr_choice == 'h)' or usr_choice == 'H' or usr_choice == 'H)'):
            positiveornegative()
        elif(usr_choice == 'i' or usr_choice == 'i)' or usr_choice == 'I' or usr_choice == 'I)'):
            generaterandom()
        elif(usr_choice == 'j' or usr_choice == 'j)' or usr_choice == 'J' or usr_choice == 'J)'):
            calculatesin()
        elif(usr_choice == 'k' or usr_choice == 'k)' or usr_choice == 'K' or usr_choice == 'K)'):
            calculatecos()
        elif(usr_choice == 'l' or usr_choice == 'l)' or usr_choice == 'L' or usr_choice == 'L)'):
            calculatetan()
        elif(usr_choice == 'm' or usr_choice == 'm)' or usr_choice == 'M' or usr_choice == 'M)'):
            absolutevalue()
        elif(usr_choice == 'n' or usr_choice == 'n)' or usr_choice == 'N' or usr_choice == 'N)'):
            powerraise()
        elif(usr_choice == 'p' or usr_choice == 'p)' or usr_choice == 'P' or usr_choice == 'P)'):
            logg()
        elif(usr_choice == 'o' or usr_choice == 'o)' or usr_choice == 'O' or usr_choice == 'O)'):
            logg10()
        elif(usr_choice == 'xc' or usr_choice == 'xc)' or usr_choice == 'XC' or usr_choice == 'XC)'):
            pymathsinfo()
    except Exception as error:
        print('An error has occured', '(', error, ')')
def addition():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x + y =', float(numberX + numberY), '(', numberX, '+', numberY, '=', float(numberX + numberY), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def subtraction():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x - y =', float(numberX - numberY), '(', numberX, '-', numberY, '=', float(numberX - numberY), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def multiply():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x * y =', float(numberX * numberY), '(', numberX, '*', numberY, '=', float(numberX * numberY), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def division():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x / y =', float(numberX / numberY), '(', numberX, '/', numberY, '=', float(numberX / numberY), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def squareroot():
    try:
        numberX = float(input("Defining x as the number, give x a value: "))
        print('Result: The square root of x =', sqrt(float(numberX)), '( x has the value of', numberX, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def modulos():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x % y =', float(numberX % numberY), '(', numberX, '%', numberY, '=', float(numberX % numberY), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def pymathsinfo():
    try:
        if (os.name == 'nt'):
            windowsconsoleclear()
        else:
            linuxconsoleclear()
        print("-+-+-+-+-+-+-+-+-+-+-+-+"), print("| author: Dragan Cezar |"), print("| version: 0.4.3       |"), print("| os: Windows and Linux|"), print("| publish: 1 jan. 2019 |"),print("-+-+-+-+-+-+-+-+-+-+-+-+"), print("This message will disappear in 5 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 4 seconds, restaring the script !"), time.sleep(1), print("This message will disappear in 3 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 2 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 1 second, restarting the script !"), time.sleep(1.2)
        if (os.name == 'nt'):
            windowsconsoleclear()
        else:
            linuxconsoleclear()
        main()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        main()
def oddoreven():
    try:
        numberX = float(input("Defining x as the number, give a value to x: "))
        if (numberX % 2 == 0):
            print('Result:', numberX,'is an even number because x % 2 = 0', '( x has the value of', numberX, ') !')
        else:
            print('Result:', numberX,'is an odd number because x % 2 is not equal to 0', '( x has the value of', numberX, ') !')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def positiveornegative():
    try:
        numberX = float(input("Defining x as the number, give a value to x: "))
        if (numberX > 0):
            print('Result:', numberX, 'is a positive number because it is higher than 0 !', '( x =', numberX, ';', numberX, '> 0 ) !')
        elif (numberX == 0):
            print('Result:', numberX, 'is a positive number because it is 0 !', '( x =', numberX, ';', numberX, '= 0 ) !')
        else:
            print('Result:', numberX, 'is a negative number because it is lower than 0 !', '( x =', numberX, ';', numberX, '< 0 ) !')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def generaterandom():
    try:
        numberX = int(input('The interval starts from '))
        numberY = int(input('and ends at '))
        print('Generating a random number from', numberX, 'to', numberY, '...'), time.sleep(3), print('Result: A random number has been generated. The number is:', randint(numberX, numberY), '!')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def calculatesin():
    try:
        print('What is the angle measure ?')
        angle = int(input('The angle measure is: '))
        sinresultradians = sin(radians(angle))
        sinresultdegrees = sin(degrees(angle))
        print('Result (radians): sin (', angle ,')', '=', sinresultradians)
        print('Result (degrees): sin (', angle, ')', '=', sinresultdegrees)
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def calculatecos():
    try:
        print('What is the angle measure ?')
        angle = int(input('The angle measure is: '))
        cosresultradians = cos(radians(angle))
        cosresultdegrees = cos(degrees(angle))
        print('Result (radians): cos (', angle ,')', '=', cosresultradians)
        print('Result (degrees): cos (', angle, ')', '=', cosresultdegrees)
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def calculatetan():
    try:
        print('What is the angle measure ?')
        angle = int(input('The angle measure is: '))
        tanresultradians = tan(radians(angle))
        tanresultdegrees = tan(degrees(angle))
        print('Result (radians): tan (', angle ,')', '=', tanresultradians)
        print('Result (degrees): tan (', angle, ')', '=', tanresultdegrees)
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (calculateagain == 'N' or calculateagain == 'n'):
            quit()
def absolutevalue():
    try:
        numberX = float(input('Defining x as the number, give x a value: '))
        print('Result: The absolute value of', numberX, 'is', float(abs(numberX)), '! ( |', numberX, '| =', float(abs(numberX)), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
def powerraise():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        power = float(input('Defining y as the power number, give y a value: '))
        print('Result:', numberX, 'raised to the power', power, 'is', float(numberX ** power), '! (', numberX, '**', power, '=', float(numberX ** power), ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
def logg():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        print('Result: log (', numberX, ') =', log(numberX))
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
def logg10():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        print('Result: log10 (', numberX, ') =', log10(numberX))
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured', '(', error, ')')
        calculateagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(calculateagain == 'N' or calculateagain == 'n'):
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