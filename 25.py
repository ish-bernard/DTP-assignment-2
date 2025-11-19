# Append 1–20, remove odd numbers, sort, get top 3

nums = []
for i in range(1, 21):
    nums.append(i)

nums = [n for n in nums if n % 2 == 0]   # remove odd numbers
nums.sort(reverse=True)

top3 = nums[:3]
print(top3)
