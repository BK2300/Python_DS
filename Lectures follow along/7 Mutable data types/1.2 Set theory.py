A = {1, 2, 3}
B = {3, 4, 5}
"""
    | Operation      | Eksempel | Resultat       | Forklaring            |                  |
    | -------------- | -------- | -------------- | --------------------- | ---------------- |
    | Union          |   `A     |   B`           | `{1, 2, 3, 4, 5}`     | kombinerer begge |
    | Intersection   | `A & B`  | `{3}`          | fælles elementer      |                  |
    | Difference     | `A - B`  | `{1, 2}`       | elementer kun i A     |                  |
    | Symmetric diff | `A ^ B`  | `{1, 2, 4, 5}` | ikke fælles elementer |                  |"""

# Er 3 ∈ A ? #Is 3 in set A
# Er 3 ∈ B ?
print(3 in A)   # True
print(3 in B)  # True

# Union
print(A | B)  # all unique numbers
# A ∪ B = {1, 2, 3, 4, 5}

# Intersection
print(A & B)  # number in between both sets
# A ∩ B = {3}

#Difference
print(A - B) # B Value removed. whats left?
# A − B = {1, 2}

# Symmetric Difference (A △ B)
print(A ^ B) # elements that either A or B. not in both
# A △ B = {1, 2, 5, 6}

#Subset & superset
print(A <= B)  # False
print(B >= A)  # False


# Set theory excercise
word1 = set("banana")
word2 = set("bandana")

print("Bogstaver i begge ord:", word1 & word2)
print("Bogstaver kun i det første:", word1 - word2)
print("Alle bogstaver:", word1 | word2)


# Add or remove elements
students_2024 = ["Anna", "Bo", "Clara"]
students_2025 = ["Bo", "Clara", "David"]

A = set(students_2024)
B = set(students_2025)

print("Fælles studerende:", A & B)
print("Kun 2024:", A - B)
print("Kun 2025:", B - A)

