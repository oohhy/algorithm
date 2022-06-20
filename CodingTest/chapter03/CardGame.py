n, m = map(int, input().split())
a = 0

for i in range(n):
    card = list(map(int, input().split()))
    
    if a < min(card):
        a = min(card)
print(a)