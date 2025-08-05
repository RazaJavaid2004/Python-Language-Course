# Define a list
my_list = [1, 2, 3, 4, 5, 3, 6]

# Print the original list
print(f"Original list: {my_list}")

# Using various list methods
my_list.append(7)
print(f"append(7): {my_list}")

my_list.extend([8, 9])
print(f"extend([8, 9]): {my_list}")

my_list.insert(3, 'a')
print(f"insert(3, 'a'): {my_list}")

my_list.remove(3)
print(f"remove(3): {my_list}")

pop_item = my_list.pop(2)
print(f"pop(2): {my_list} (popped item: {pop_item})")

index_item = my_list.index(4)
print(f"index(4): {index_item}")

count_item = my_list.count(3)
print(f"count(3): {count_item}")

my_list.sort()
print(f"sort(): {my_list}")

my_list.reverse()
print(f"reverse(): {my_list}")

copy_list = my_list.copy()
print(f"copy(): {copy_list}")

my_list.clear()
print(f"clear(): {my_list}")

# Demonstrate the usage of slicing and length
slice_list = copy_list[2:5]
print(f"slice [2:5]: {slice_list}")

list_length = len(copy_list)
print(f"length of list: {list_length}")