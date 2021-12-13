from random import randrange
# Data 1 =======================================
data1  = (7, False, "Apple", True, 7, 98.6)


# Cound the number of items
print(len(data1))

# Find the value of the 4th item
print(data1[3])

# Count how many times the number 7 appears
print(data1.count(7))

# Data 2 ========================================
data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

# Get random index of the item to be removed
index_to_remove = randrange(0, len(data2) - 1)
# Remove the item at the random index
data2.remove(list(data2)[index_to_remove])

data2.add("Alpha")

# Print the data2 set
for item in data2:
    print(item, end=" ")
print("")

# Data 2 =========================================

data3 = ["A", 7, -1, 3.14, True, 7]

# Print the data in reverse order
for i in range(len(data3) - 1, -1, -1):
    print(data3[i], end=" ")
print("")

# Change 2nd value
data3[1] = "B"

# Remove last item
data3 = data3[0 : len(data3) - 1]

for item in data3:
    print(item, end=" ")

# Data 4 ==========================================
# create a dictionary
data4 = {"name": "Joe",  "age": 26,   "active": True,  "hourly_wage": 14.75}

# change a value
data4["active"] = False

# Add a key, value
data4["address"] = "123 West Main Street"

salary = 40 * data4["hourly_wage"]
print(salary)

print(data4)