n, k = map(int, input().split())
count = 0
target = 0

while n >= k:
    target = (n // k) * k
    n = target
    count += n - target
    n //= k
    count += 1

    if n < k:
        break

count += n-1
print(count)
