inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# Find out how many items in the inventory
inventory_len = len(inventory)
print(f"There are {inventory_len} items in inventory")

# find the first item in inventory
first = inventory[0]
print(f"The first item is: {first}")

#find the last item in inventory
last = inventory[-1]
print(f"The last item is: {last}")

# Select a portion of the inventory
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# Select the first three items in inventory
first_3 = inventory[0:3]
print(first_3)

# Coun the number of twin beds available
twin_beds = inventory.count("twin bed")
print(f"There are {twin_beds} twin beds available")

# Remove the fifth element on the list. 
removed_item = inventory.pop(4)
print(f"{removed_item} has been removed")

# Insert new item
inventory.insert(10, "19th Century Bed Frame")
print(f"New inventory list")

# Sort the inventory in order
inventory.sort()
print(inventory)