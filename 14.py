# Remove duplicates without using set()

data = [1, 2, 2, 3, 1, 4]
unique = []

for item in data:
    if item not in unique:
        unique.append(item)

print(unique)