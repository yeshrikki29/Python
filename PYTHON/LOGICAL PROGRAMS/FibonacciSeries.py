Number=int(input("Enter a Number: "))
PreviousNumber   = 0
CurrentNumber = 1
while(PreviousNumber <= Number):
    print(PreviousNumber , end=" ")
    Sum=PreviousNumber+CurrentNumber
    PreviousNumber=CurrentNumber
    CurrentNumber=Sum