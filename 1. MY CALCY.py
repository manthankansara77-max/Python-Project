# MY CALCY :--
from fractions import Fraction
import math 
import matplotlib.pyplot as plt


A = "1 - addition"
B = "2 - subtraction"
C = "3 - multiplication"
D = "4 - division"
E = "5 - square root"
F = "6 - percentage"
G = "7 - logarithm"
H = "8 - power"
I = "9 - exponential (e = 2.71)"
J = "10 - trigonometry"
K = "11 - Round Down"
L = "12 - Round up"
M = "13 - Factorial"
N = "14 - Greatest common divisor"

print(A + "\n" + B + "\n" + C + "\n" + D + "\n" + E + "\n" + F + "\n" + G + "\n" + H + "\n" + I + "\n" + J + "\n" + K + "\n" + L + "\n" + M + "\n" + N )
try:
    option = int(input("which type you want? :"))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

try:
    if(option in [1,2,3,4,8,14]):
        num1 = int(input("enter first number :"))
        num2 = int(input("enter second number :"))

    elif(option in [5,7,9,13]):
        num3 = int(input("enter number: "))

    elif(option == 6):
        num4 = int(input("enter percentage: "))
        num5 = int(input("of how much: "))

    elif(option in [11,12]):
        num6 = float(input("enter number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

try:
    if(option == 10):
        print("a - sin0")
        print("b - cos0")
        print("c - tan0")
        print("d - cosec0")
        print("e - sec0")
        print("f - cot0")
    
        sub_option = (input("which one do you want:"))
    
        if sub_option in ['a','b','c','d','e','f']:
        
            angle_type = input("Enter D for Degree or R for Radian: ")
            angle = float(input("Enter the angle: "))
    
        if angle_type.upper() == 'R':
            rad = math.radians(angle)
            fraction = Fraction(int(angle), 180).limit_denominator() 
            
            def print_radians(fraction):
                if fraction.numerator == 1:
                    print(f"Angle in Radians = π/{fraction.denominator}")
                elif fraction.denominator == 1:
                    print(f"Angle in Radians = {fraction.numerator}π")
                else:
                    print(f"Angle in Radians = {fraction.numerator}π/{fraction.denominator}")
            print_radians(fraction)
        
        elif angle_type.upper() == 'D':
            rad = angle
            print(f"Angle in Degrees = {math.degrees(rad)}°")

        if sub_option == 'a':
            result = math.sin(rad)

        elif sub_option == 'b':
            result = math.cos(rad)

        elif sub_option == 'c':
            result = math.tan(rad)

        elif sub_option == 'd':
            result = 1 / math.sin(rad)

        elif sub_option == 'e':
            result = 1 / math.cos(rad)

        elif sub_option == 'f':
            result = 1 / math.tan(rad)
except :
    print("Invalid input.")
    exit()

try:
    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2
    elif(option == 5):
        result = num3 ** 0.5   
    elif(option == 6):
        result = (num4 / 100) * num5
    elif(option == 7):
        result = math.log10(num3)
    elif(option == 8):
        result = math.pow(num1,num2)
    elif(option == 9):
        result = math.exp(num3)
    elif(option == 11):
        result = math.floor(num6)
    elif(option == 12):
        result = math.ceil(num6)
    elif(option == 13):
        result = math.factorial(num3)
    elif(option == 14):
        result = math.gcd(num1,num2)
finally:
    print("Processing Complete")

print("your answer is", result ) 


