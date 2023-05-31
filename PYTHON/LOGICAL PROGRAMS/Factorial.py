def factorial(number):
    if(number == 0):
        return 1
    else:
        return number*factorial(number-1)
    
Number=int(input("Enter a number: "))
if Number<0:
    print("Factorial is not defined for negative numbers.")
else:     
    result = factorial(Number)
    print(f"Factorial of {Number} is {result}.")

