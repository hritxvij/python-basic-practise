# What if 2 values are same?

friends = {"Anshu" : "Python",
           "UV" : "French",
           "Swapnil" : "Python"}

name = input("Please enter your name:\n ")
print("Your fav language is:\n", friends.get(name))   