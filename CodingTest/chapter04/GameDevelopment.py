n, m = map(int, input().split())
# d = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 0을 m개 채운 리스트를 n개 가진 리스트(왔는지 안왔는지 check)
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
# 현재 위치는 방문 체크
d[x][y] = 1

# 맵 정보 받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북 동 남 서(바라보고있는 방향) 별 방향으로 이동 했을 때 좌표 변화
dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

# 기본 이동 절차를 함수로 
def turn_left():
    # 전역 변수 direction 선언 (선언 후 할당 가능)
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작 
count = 1
turn_time = 0
while True:
    # turn_left로 방향 바꾸기 
    turn_left()
    # 방향별 칸 이동할 곳 계산(예상 이동 좌표 nx, ny)
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 예상 이동 좌표가(nx, ny) 와본적 없고, 육지인지 확인
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # ok이면 온거 체크 
        d[nx][ny] = 1
        # 이동(x, y좌표 바꾸기)
        x = nx
        y = ny
        count += 1
        turn_time = 0
        # continue- 조건 만족 할 때 동안 계속 while문으로 돌아가서 방향 회전, 좌표이동 반복
        continue
    # ok 아니면 -> 회전만(x, y에 nx, ny대입 안하면 이동한거 아님)
    else:
        turn_time += 1
    
    if turn_time == 4:
        # 4면 다 가봤으면 방향 별 뒤로 1칸 물러나기
        nx = x - dx[direction]
        ny = y - dy[direction]
        # back 한 자리가 육지인지 확인
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # back 한 위치가 바다면 break
        else:
            break
        turn_time = 0

print(count)