name = input("Enter your full name: ")
letters_count = len(name.replace(" " , ""))
print(f"Hi {name}! Your name has {letters_count} letters, excluding spaces.")