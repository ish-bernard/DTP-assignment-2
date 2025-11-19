# Multiples of 3, 5, and both

nums = list(range(1, 31))

mul3 = [n for n in nums if n % 3 == 0]
mul5 = [n for n in nums if n % 5 == 0]
mul_both = [n for n in nums if n % 3 == 0 and n % 5 == 0]

print(mul3, mul5, mul_both)
