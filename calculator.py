#Calculator

import math
Num1 = float(input("Enter first number: "))
Operator = input("Enter the operator (+, -, *, /, ^, %, √ ): ")
Num2 = float(input("Enter second number: "))

if Operator== "+":
    print(Num1,"+",Num2,"=", Num1+Num2)

elif Operator== "-":
    print(Num1,"-",Num2,"=", Num1-Num2)

elif Operator== "*":
    print(Num1,"*",Num2,"=", Num1*Num2)

elif Operator== "/":
    if Num2==0 :
        print("Error, division by zero is not allowed.")
    else:
        print(Num1,"/",Num2,"=", Num1/Num2)

elif Operator== "^":
    print(Num1,"^",Num2,"=", Num1 ** Num2)  

elif Operator== "%":
    print(Num1,"%",Num2,"=", Num1%Num2)

elif Operator== "√":
    if Num1 < 0:
        print("Error, Square root of negative number is not possible.")
    else:
        print(math.sqrt(Num1))
              
else:
   print("Invalid choice!")







