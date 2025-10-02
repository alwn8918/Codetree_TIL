nums = list(map(int, input().split()))

total = sum(nums)
avg = int(sum(nums) / len(nums))

print(total)
print(avg)
print(total - avg)