n = int(input())
plans = list(input() .split())
spot = [1, 1]

for i in range(len(plans)):
    if plans[i] == "R" and spot[1] < n:
        spot[1] += 1
        
            
    elif plans[i] == "L" and spot[1] > 1:
        spot[1] -= 1 
        
              
    elif plans[i] == "U" and spot[0] > 1:
        spot[0] -= 1
        
            
    elif plans[i] == "D" and spot[0] < n:
        spot[0] += 1
        
            
print(*spot) 