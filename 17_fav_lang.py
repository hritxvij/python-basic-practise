friends = {"Anshu" : "Python",
           "UV" : "French",
           "Swapnil" : "Assamese"}

name = input("Please enter your name:\n ")
print("Your fav language is:\n", friends.get(name))   