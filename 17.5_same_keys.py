# What if the 2 key names are same

friends = {"Anshu" : "Python",
           "UV" : "French",
           "UV" : "Assamese"}

name = input("Please enter your name:\n ")
print("Your fav language is:\n", friends.get(name))   