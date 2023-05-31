def isPallindrome(String):
    length=len(String)
    for i in range(length):
        if String[i] != String[length - i-1]:
            return False
    return True

String = input("Enter a String: ")
if (isPallindrome(String)):
    print(f"{String} is a Pallindrome")
else:
    print(f"{String} is not a pallindrome")