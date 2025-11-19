# Convert CSV-style string to list of lists

text = "John,25,Engineer;Mary,30,Doctor;Sam,22,Designer"
result = [item.split(",") for item in text.split(";")]
print(result)
