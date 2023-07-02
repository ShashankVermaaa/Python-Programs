Letter = '''Dear <|NAME|>
You are SELECTED!
<|DATE|>'''
Name = input("Enter your name : ")
Date = input("Enter date : ")
Letter = Letter.replace("<|NAME|>",Name)
Letter = Letter.replace("<|DATE|>",Date)
print(Letter)