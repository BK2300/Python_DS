# Write a program that asks the user for a number, n.  Then use loops to repeat-edly print a message.


n = int(input("Insert a number between 1-100: "))

while n > 0:
#    x = n -= 1
    print(f"{n} books on Python on the shelf. Take one down, pass it around, {n-1} books left.")
    n -= 1

print("Goodbye")








