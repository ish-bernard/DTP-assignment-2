#Input different types & convert to strings

s = input ("Enter a string:")
t = int(input("Enter an integer:"))
f = float(input("Enter a float:"))


print (f"{s} is a", type(s))
print (f"{t} is a", type(t))
print (f"{f} is a", type(f))

result = [str(s), str(t), str(f)]

print(f"converted list:{result}")