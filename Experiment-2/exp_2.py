n = int(input())
arr = list(map(int, input().split()))
total_ones = sum(arr)
transformed = [1 if x == 0 else -1 for x in arr]
max_sum = transformed[0]
current_sum = transformed[0]
for i in range(1, n):
    current_sum = max(transformed[i], current_sum + transformed[i])
    max_sum = max(max_sum, current_sum)
if max_sum < 0:
    print(n - 1)
else:
    print(total_ones + max_sum)