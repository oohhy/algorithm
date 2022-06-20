# m커지면 속도 느림, 시간 오버
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[n-1]
second = array[n-2]
output = 0


while True:
    if m == 0:
        break
    output = output + first * k
    m=m-k
    if m == 0:
        break
    output = output + second
    m=m-1

print(output)

