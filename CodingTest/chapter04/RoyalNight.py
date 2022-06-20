input_data = input()
input_row = int(input_data[1])
# a1을 숫자로 바꾸는 과정 ord('a')=97
input_column = int(ord(input_data[0]))-int(ord('a')) + 1
count=0
# 움직일 수 있는 경우 나열 UDLR과 유사
steps = [(-2,1),(2,1),(-2,-1),(2,-1),(-1,2),(-1,-2),(1,2),(1,-2)]

for step in steps:
    row = input_row + step[0]
    column = input_column + step[1]

    if 1<=row<=8 and 1<=column<=8:
        count += 1

print(count)