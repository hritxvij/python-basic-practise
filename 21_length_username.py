username = input("Please enter your username: ")
length = len(username)<10
if  length is True:
    print("The username is less than 10 characters!")
else:
    print("The usename has more than 10 characters!")