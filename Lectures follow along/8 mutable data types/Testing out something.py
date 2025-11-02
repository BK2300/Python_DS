# lets us try to think like a data analyst and try out something


# Find out every unique item
sales = ["Coca-Cola", "Fanta", "Sprite", "Coca-Cola", "Fanta", "Coca-Cola"]
unique_brands = set(sales)
print(unique_brands)
#Converting it to a set. To find the each unique names


# find out how many times the item appears
unique_brands = list(unique_brands)
count_coke = unique_brands.count("Coca-Cola")
print(count_coke)
#tried to convert it back to a list. But seems to disrupt the amount of coca colas from the original. So thats not a smart idea to do.






