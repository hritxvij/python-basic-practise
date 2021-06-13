num1 = input("Enter the first number:\n ")
num2 = input("Enter the second number:\n ")
num3 = input("Enter the third number:\n ")
num4 = input("Enter the fourth number:\n ")

if   (num1>num2) and (num2>num3):
        print("The greatest number is:", num1)        
    
elif (num2>num1) and (num1>num3):
        print("The greatest nymber is:", num2)

else:
    print("The greatest number is:", num3)