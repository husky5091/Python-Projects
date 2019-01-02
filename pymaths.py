from math import sqrt
from math import sin
from math import cos
from math import tan
from math import radians
from math import degrees
from math import log
from math import log10
from math import log2
from math import ceil
from math import pow
from datetime import datetime
import os
import time
from random import randint
def main():
    try:
        checkos()
        print('\033[94m+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m')
        print('\033[93m|             PyMaths CMD (commands)               |\033[0m')       
        print('\033[31m|--------------------------------------------------|\033[0m')       
        print('\033[36m| a) addition             | k) cos (cosine)        |\033[0m')         
        print('\033[92m| b) substraction         | l) tan (tangent)       |\033[0m')         
        print('\033[35m| c) multiply             | m) absolute value      |\033[0m') 
        print('\033[91m| d) division             | n) exponentiation      |\033[0m') 
        print('\033[90m| e) square root          | o) logarithm10 (log10) |\033[0m')
        print('\033[34m| f) modulos              | p) logarithm (log)     |\033[0m')
        print('\033[56m| g) odd or even          | q) degrees to radians  |\033[0m')
        print('\033[36m| h) pozitive or negative | r) radians to degrees  |\033[0m')
        print('\033[92m| i) random number        | s) prime number        |\033[0m')
        print('\033[35m| j) sin (sine)           | t) logarithm2 (log2)   |\033[0m')
        print('\033[91m| px) PyMaths details     | u) ceil                |\033[0m')
        print('\033[94m+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\033[0m')
        print('PyMaths started at', datetime.now(), '!')
        print('Entering an invalid operation will restart the script.')
        print("WARNING! Float numbers are written with '.' not with ',' !")
        usr_choice = input(">> ")
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
        elif(usr_choice == 'o' or usr_choice == 'o)' or usr_choice == 'O' or usr_choice == 'O)'):
            logg10()
        elif(usr_choice == 'p' or usr_choice == 'p)' or usr_choice == 'P' or usr_choice == 'P)'):
            logg()
        elif(usr_choice == 'q' or usr_choice == 'q)' or usr_choice == 'Q' or usr_choice == 'Q)'):
            degreestoradians()
        elif(usr_choice == 'r' or usr_choice == 'r)' or usr_choice == 'R' or usr_choice == 'R)'):
            radianstodegrees()
        elif(usr_choice == 't' or usr_choice == 't)' or usr_choice == 'T' or usr_choice == 'T)'):
            logg2()
        elif(usr_choice == 'u' or usr_choice == 'u)' or usr_choice == 'U' or usr_choice == 'U)'):
            ceill()
        elif(usr_choice == 's' or usr_choice == 's)' or usr_choice == 'S' or usr_choice == 'S)'):
            primenumber()
        elif(usr_choice == 'px' or usr_choice == 'px)' or usr_choice == 'PX' or usr_choice == 'PX)'):
            pymathsinfo()
    except Exception as error:
        print('An error has occured:', error)
def addition():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x + y =', float(numberX + numberY), '(', numberX, '+', numberY, '=', float(numberX + numberY), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def subtraction():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x - y =', float(numberX - numberY), '(', numberX, '-', numberY, '=', float(numberX - numberY), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def multiply():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x * y =', float(numberX * numberY), '(', numberX, '*', numberY, '=', float(numberX * numberY), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def division():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x / y =', float(numberX / numberY), '(', numberX, '/', numberY, '=', float(numberX / numberY), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def squareroot():
    try:
        numberX = float(input("Defining x as the number, give x a value: "))
        print('Result: The square root of x =', sqrt(float(numberX)), '( x has the value of', numberX, ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def modulos():
    try:
        numberX = float(input("Defining x as the first number, give x a value: "))
        numberY = float(input("Defining y as the second number, give y a value: "))
        print('Result: x % y =', float(numberX % numberY), '(', numberX, '%', numberY, '=', float(numberX % numberY), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def pymathsinfo():
    try:
        checkos()
        print("-+-+-+-+-+-+-+-+-+-+-+-+"), print("| author: Dragan Cezar |"), print("| version: 0.4.3       |"), print("| os: Windows and Linux|"), print("| publish: 1 jan. 2019 |"),print("-+-+-+-+-+-+-+-+-+-+-+-+"), print("This message will disappear in 5 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 4 seconds, restaring the script !"), time.sleep(1), print("This message will disappear in 3 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 2 seconds, restarting the script !"), time.sleep(1), print("This message will disappear in 1 second, restarting the script !"), time.sleep(1.2)
        checkos()
        main()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def oddoreven():
    try:
        numberX = float(input("Defining x as the number, give a value to x: "))
        if (numberX % 2 == 0):
            print('Result:', numberX,'is an even number because x % 2 = 0', '( x has the value of', numberX, ') !')
        else:
            print('Result:', numberX,'is an odd number because x % 2 is not equal to 0', '( x has the value of', numberX, ') !')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
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
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def generaterandom():
    try:
        numberX = int(input('We will generate a random number that starts from '))
        numberY = int(input('and ends at '))
        print('Generating a random number from', numberX, 'to', numberY, '...'), time.sleep(3), print('Result: A random number has been generated. The number is:', randint(numberX, numberY), '!')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def calculatesin():
    try:
        print('What is the angle measure ?')
        angle = int(input('The angle measure is: '))
        sinresultradians = sin(radians(angle))
        sinresultdegrees = sin(degrees(angle))
        print('Result (radians): sin (', angle ,')', '=', sinresultradians)
        print('Result (degrees): sin (', angle, ')', '=', sinresultdegrees)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def calculatecos():
    try:
        print('What is the angle measure ?')
        angle = int(input('The angle measure is: '))
        cosresultradians = cos(radians(angle))
        cosresultdegrees = cos(degrees(angle))
        print('Result (radians): cos (', angle ,')', '=', cosresultradians)
        print('Result (degrees): cos (', angle, ')', '=', cosresultdegrees)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def calculatetan():
    try:
        print('What is the angle measure ?')
        angle = int(input('The angle measure is: '))
        tanresultradians = tan(radians(angle))
        tanresultdegrees = tan(degrees(angle))
        print('Result (radians): tan (', angle ,')', '=', tanresultradians)
        print('Result (degrees): tan (', angle, ')', '=', tanresultdegrees)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def absolutevalue():
    try:
        numberX = float(input('Defining x as the number, give x a value: '))
        print('Result: The absolute value of', numberX, 'is', float(abs(numberX)), '! ( |', numberX, '| =', float(abs(numberX)), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def powerraise():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        power = float(input('Defining y as the power number, give y a value: '))
        print('Result:', numberX, 'raised to the power', power, 'is', float(pow(numberX, power)), '! (', numberX, '**', power, '=', float(pow(numberX, power)), ')')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def logg():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        print('Result: log (', numberX, ') =', log(numberX))
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def logg10():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        print('Result: log10 (', numberX, ') =', log10(numberX))
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def logg2():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        print('Result: log2 (', numberX, ') =', log2(numberX))
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()   
def degreestoradians():
    try:
        degrees23 = float(input('Defining x as the angle, give x a value: '))
        print('Result:', degrees23, 'degrees converted into radians is:', radians(degrees23), 'radians!')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def radianstodegrees():
    try:
        radians23 = float(input('Defining x as the angle , give x a value: '))
        print('Result:', radians23, 'radians converted into degrees is:', degrees(radians23), 'degrees!')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit() 
def ceill():
    try:
        numberX = float(input('Defining x as the number, give a value to x: '))
        print('Result: ceil (', numberX, ') =', ceil(numberX))
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def primenumber():
    try:
        num = int(input('Defining x as the number, give x a value: '))
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print('Result:', num ,"is not a prime number !")
                    break  
                else:
                    print('Result:', num ,"is a prime number !")
                    break
        elif (num <= 1):
            print(num, 'is not a prime number !')
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if (runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
    except Exception as error:
        print('An error has occured:', error)
        runagain = input("Would you like to run PyMaths again ? (Y/N): ")
        if(runagain == 'N' or runagain == 'n'):
            checkos()
            quit()
def checkos():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')
main()
runagain = 'Y'
while (runagain == 'Y' or runagain == 'y'):
    checkos()
    print("The script has been restarted !")
    main()