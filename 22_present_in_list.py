logbook = ["Hritik", "Sam", "Uv", "Anshu"]
logbook = logbook.capitalise()
name = input("Please enter your name: ")

if (name in logbook):
    print("You are allowed to enter! :)")
else:
    print("Sorry, you aren't allowed! X")
