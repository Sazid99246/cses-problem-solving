n = int(input())

expected_sum = n * (n + 1) // 2
actual_sum = sum(map(int, input().split()))
print(expected_sum - actual_sum)
