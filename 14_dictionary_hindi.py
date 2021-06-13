hindDict = {"Pankha" : "Fan",
            "Kalam" : "Pen",
            "Kitaab" : "Book",
            "Vigyaan" : "Science"}
fetch = input("Enter the Hindi word:\n ")
print("The English word for this is: ", hindDict.get(fetch))