# Here is some extra examples on dictionaries
# A HR-manager uses it like so:

#Creating a dataset
employees = {
    "E001": {"name": "Anna", "role": "Data Analyst", "salary": 52000},
    "E002": {"name": "Bo", "role": "ML Engineer", "salary": 61000},
    "E003": {"name": "Clara", "role": "HR Manager", "salary": 48000}
}

# find a employee
print(employees["E002"]["name"])

#Add a new employee
employees["E004"] = {"name": "David", "role": "Intern", "salary": 32000}

# Update salary of employee
employees["E001"]["salary"] += 2000

#Removing a employee
del employees["E003"]

for emp_id, info in employees.items():
    print(emp_id, info["name"], "→", info["role"])














