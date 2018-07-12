import math
nums = range(2, 100)
bound = int(math.sqrt(100))

for i in range(2, bound):
    nums = filter(lambda x: x%i or x==i, nums)

print nums