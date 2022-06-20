# 반복문 없애서 실행 빠름
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[n-1]
second = array[n-2]
output = 0

# 사이클에 들어가는 최대값 개수 6665666566 -> 6개
first_count = k * int(m/(k+1)) 
# 사이클 밖에 있는 최대값 개수까지 합 6665666566 -> 6+2개
first_count += m % (k+1)

second_count = m - first_count

output = first_count * first + second_count * second
print(output)

