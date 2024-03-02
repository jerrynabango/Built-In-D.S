my_list = []

# Add some numbers to my_list using extend()
my_list.extend([10, 20, 30, 40])

# Insert the number 15 at the second position in the list using insert()
my_list.insert(1, 15)

# Add more numbers to my_list using extend()
my_list.extend([50, 60, 70])

# Remove the last number from my_list using pop()
removed_number = my_list.pop()

# Organize the numbers in ascending order using sort()
my_list.sort()

# Find the index of the number 30 in my_list using index()
index_30 = my_list.index(30)

# Print the index of 30 in my_list
print("The index of the value 30 in my_list is:", index_30)
