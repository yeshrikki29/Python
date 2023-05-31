Number=int(input("Enter a Number: "))
sum=0
OriginalNumber=Number

while(Number !=0):
    digit=Number%10
    sum+=pow(digit,3)
    Number/=10
    
if(sum==OriginalNumber):
    print(f"{OriginalNumber} is an Armstrong Number")
else:
    print(f"{OriginalNumber} is not an Armstrong Number")