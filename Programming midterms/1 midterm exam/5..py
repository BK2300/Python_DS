demographics = {
 "Alice": {"age": 22, "gender": "female", "city": "Odense"},
 "Bob": {"age": 27, "gender": "male", "city": "Copenhagen"},
 "Charlie": {"age": 35, "gender": "male", "city": "Aarhus"},
 "Diana": {"age": 29, "gender": "female", "city": "Odense"},
 "Elias": {"age": 40, "gender": "male", "city": "Aalborg"},
 "Freja": {"age": 31, "gender": "female", "city": "Copenhagen"},
 "Gustav": {"age": 24, "gender": "male", "city": "Odense"},
}

ages = [student["age"] for student in demographics.values()] #This lines searches for each values assigned to "age" in our dictionary
average_age = sum(ages) / len(ages) #sums all "age" together and divides its with the number of values.
print(f"{average_age:.2f}") #My f-string formats the float to only 2 decimal places
print() #this print statment is irrelevant. just wanted space for the next question
# ________________

count = 0
for person in demographics.values(): #loops through each person
    if person["city"] == "Odense": #checks if they are from "Odense"
        count += 1  #adds another if found another
print(f"There are {count} people from Odense.")
print()
# ________________
gender = 0
for student in demographics.values():
    if student["gender"] == "male":
        gender += 1
print(f"There is {gender} amount of males")
print(f"There is {7 - gender} females")
print()
#_______________

oldest_age = max(person["age"] for person in demographics.values())
print(f"The oldest age in the class is: {oldest_age}")







