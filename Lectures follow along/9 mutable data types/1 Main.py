# Dictonary

# To find a key or a value in a dictionary.
# imagen having a database and trying to find information about someone. But only has his employee_id

person = {"name": "Anna", "age": 25}
print(person.get("name"))   # Anna
print(person.get("city"))   # None


#If a key doesnt exist, give me value "X"
print(person.get("city", "Unknown"))   # 'Unknown'


# Looping with a key word that doesnt exist
employees = [
    {"name": "Anna", "department": "HR"},
    {"name": "Bo"},
    {"name": "Clara", "department": "Finance"}
]

for emp in employees:
    print(emp.get("department", "Not assigned"))


# Counting
sales = ["Coca-Cola", "Fanta", "Coca-Cola", "Sprite", "Sprite", "Sprite", "Sprite"]
counts = {}
for item in sales:
    counts[item] = counts.get(item, 0) + 1
print(counts)


# Merging dictionary
grocery = {'milk': 13, 'apple': 29, 'banana': 15, 'salt': 9, 'butter': 30,}
drinks = {'water': 9, 'juice': 35}
grocery.update(drinks)
print(grocery)








