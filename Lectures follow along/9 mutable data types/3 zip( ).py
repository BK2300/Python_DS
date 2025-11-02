# Zip () is for combining several sekvenses (Like tuples, sets, lists)

#Simple
names = ["Anna", "Bo", "Clara"]
ages = [25, 30, 22]

combined = zip(names, ages)
print(list(combined)) # [('Anna', 25), ('Bo', 30), ('Clara', 22)]

# If lists doesnt have same amount of values
"""names = ["Anna", "Bo", "Clara"]
ages = [25, 30]
print(list(zip(names, ages)))
# It stops at the lowest value. in this situation. 2 """


# Looping
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# Comining 3 lists
names = ["Anna", "Bo", "Clara"]
ages = [25, 30, 22]
cities = ["Odense", "Aarhus", "Copenhagen"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) lives in {city}")


# unzipping
zipped = list(zip(names, ages))
print(zipped)  # [('Anna', 25), ('Bo', 30), ('Clara', 22)]

unzipped = list(zip(*zipped))
print(unzipped)


# combination with enumerate
for i, (name, age) in enumerate(zip(names, ages), start=1):
    print(f"{i}. {name} - {age}")







