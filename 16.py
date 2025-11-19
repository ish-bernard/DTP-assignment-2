# Sort alphabetically then reverse (case-insensitive)

words = ["python", "Java", "ruby", "C++", "Go"]
words.sort(key=str.lower)
words = words[::-1]
print(words)
