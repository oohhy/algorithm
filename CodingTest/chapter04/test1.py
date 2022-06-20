count_min_sec= 0
list_a=[]
n = int(input())
min = list(range(60))
hour = list(range(n+1))


for i in range(n+1):
    if "3" in str(hour[i]) :
        list_a.append(hour[i])
      
    else:
        continue  

print(list_a)