n = int(input())
hour = list(range(n+1))
min = list(range(60))
count_hour = 0 
count_min= 0 

for i in range(n+1):
    if "3" in str(hour[i]):
        count_hour += 1
    else:
        continue
        
    
for i in range(60):
    if "3" in str(min[i]):
        count_min += 1 
    else:
        continue  
        
# 전체-(3이 한 번도 안들어 있는 경우 count)
not_count_total = ((n+1)-count_hour) * (60-count_min) * (60-count_min)
count_total=(n+1)*60*60-not_count_total
print(count_total)