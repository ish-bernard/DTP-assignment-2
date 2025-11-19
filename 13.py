#Modify list of fruits

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
fruits.insert(1, "Kiwi")
fruits[fruits.index("Banana")] = "Grapes"
fruits.remove("Mango")

print (fruits)