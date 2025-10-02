arr = input().split()
list = [int(arr[0]), int(arr[1]), int(arr[2])]

total = sum(list)
avg = int(sum(list) / len(list))

print(total)
print(avg)
print(total - avg)