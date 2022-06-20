n = int(input())
plans = list(input() .split()) 
x, y = 1, 1

move_x = [0, 0, -1, 1]        
move_y = [-1, 1, 0, 0]        
move_types = ["L", "R", "U", "D"]

for plan in plans: 
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + move_x[i]
            ny = y + move_y[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y) 