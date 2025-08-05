"""
Set is mutable but it's elements are not
"""

collection = set()

collection.add(0)
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)

print(collection)

collection.remove(2)
print(collection)

collection.pop()
print(collection)

collection.clear()
print(collection)

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))