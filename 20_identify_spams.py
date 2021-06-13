spam = ["make a lot of money", "buy now", "subscribe this", "click this"]

email = input("Enter the content: ")

if (email in spam):
    print("The email is a spam, please delete! X ")

else:
    print("This email is not a spam!")