#### Python code to "bake a cake" ####

ingredients = ["flour", "sugar", "eggs", "milk"] # Values are ingredients for baking a cake

oven_temp = 180 #This is assign as a string. Its should be a integer.

# Check if all main ingredients are included
if "flour" in ingredients and "sugar" in ingredients and "eggs" in ingredients: #need to be close with a colon
    # the code before check only one condition. Now it checks each individually, like booleans. so make sure all 3 ingrediens are there
    print("Ingredients are complete!")
else:
    print("Missing ingredients!")

# oven preheatingAA
print(f"Preheating oven to {oven_temp} degrees Celsius") #1: print was with cap "P". 2 after the comma. there was a " to many and the last one before the tuple was a '.
# Think the f-string wants to be used for the "oven_temp, which is not been used

for i in range(0, 30):
    print("Baking... minute", i)
    if i == 15:
        print("Cake is ready!")
        break # Stop the loop when cake is ready
print("Cake baked successfully")