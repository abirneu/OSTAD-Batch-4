nums = list(range(1,11))

for i in nums:
    print(i, end=' ')

result = {i: "even" if i % 2 == 0 else "odd" for i in nums}
print(result)