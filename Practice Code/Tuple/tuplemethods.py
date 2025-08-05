# Define a tuple
my_tuple = (1, 2, 3, 4, 5, 2, 6)

# Print the original tuple
print(f"Original tuple: {my_tuple}")

# Accessing elements and slicing
print(f"Element at index 2: {my_tuple[2]}")
print(f"Slice [1:4]: {my_tuple[1:4]}")

# Using tuple methods
count_item = my_tuple.count(2)
print(f"count(2): {count_item}")

index_item = my_tuple.index(4)
print(f"index(4): {index_item}")

# Tuple concatenation
new_tuple = my_tuple + (7, 8)
print(f"Concatenated tuple: {new_tuple}")

# Tuple repetition
repeated_tuple = my_tuple * 2
print(f"Repeated tuple: {repeated_tuple}")

# Tuple length
length = len(my_tuple)
print(f"Length of tuple: {length}")

# Checking membership
is_in_tuple = 3 in my_tuple
print(f"Is 3 in tuple: {is_in_tuple}")

# Iterating through a tuple
print("Iterating through tuple:")
for item in my_tuple:
    print(item)

# Nested tuples
nested_tuple = (1, 2, (3, 4), 5)
print(f"Nested tuple: {nested_tuple}")
print(f"Accessing nested tuple element: {nested_tuple[2][1]}")