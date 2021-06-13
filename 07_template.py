letter = '''Dear ,<|name|>,
          You are selected!
          <|date|>'''

a = input("Enter your name:\n ")
b = input("Enter the date:\n ")

letter = letter.replace("<|name|>", a)
letter = letter.replace("<|date|>", b)
print(letter)