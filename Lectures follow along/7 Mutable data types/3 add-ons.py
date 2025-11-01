grocery = ["milk", "eggs", "bread", "salt", "butter", "eggs"]

#Number of elements
print(len(grocery))

# how many times something appears in the list
print(grocery.count("eggs")) # 2
print(grocery.count("bread")) # 1

# Where is the element in the list
print(grocery.index("bread")) #index 2

# add on (at the end of the list). Or if we making a new list
Groceries = []
Groceries.append("eggs") # ["eggs"]
Groceries.append("sugar") # ["eggs", "sugar"]
Groceries.append("milk") # ["eggs", "sugar", "milk"]
print(Groceries)

# Adding elements in a specific order of our list
Groceries.insert(1, "beer") # ["eggs", "beer", "sugar", "milk"]
Groceries.insert(7, "wine") # ["eggs", "beer", "sugar", "milk", "wine"]
Groceries.insert(-2, "juice") # ["eggs", "beer", "sugar", "juice", "milk", "wine"]
print(Groceries)

#Extending (like combining them together)
grocery = ["eggs", "sugar"]
drinks = ["wine", "water", "juice"]
fruits = ["apple", "banana", "orange"]
Groceries.extend(drinks)
Groceries.extend(fruits)
print(Groceries)

# Removing elements
Groceries.pop() #Removes last item
print(Groceries)

# Sorting them in alphabetically order
Groceries.sort() #By Alphabet
prices = [13, 29, 15, 10, 30, 29]
prices.sort() #By number size
print(Groceries)
print(prices)

# Reversing the ordering
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
months.reverse()
print(months)

# excercise
numbers = [10, -2, 6, 0, -4, 1, 4, 11]
minimum = numbers[0]
maximum = numbers[0]
total = 0
for number in numbers:
    total += number
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
print("Minimum = ", minimum)
print("Maximum = ", maximum)
print("Total = ", total)
# alternatively
numbers = [10, -2, 6, 0, -4, 1, 4, 11]
print("Minimum = ", min(numbers))
print("Maximum = ", max(numbers))
print("Total = ", sum(numbers))



