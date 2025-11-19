# Sort list of dictionaries by age

users = [{"name": "A", "age": 30},
         {"name": "B", "age": 22},
         {"name": "C", "age": 27}]

users.sort(key=lambda x: x["age"])
print(users)
