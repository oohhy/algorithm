# deque(stack과 que의 장점을 모은것) 쓰기 위해서 import
from collections import deque

# queue는 deque라이브러리 방식으로 쌓고 삭제할거임!!
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
# 젤 왼쪽거 삭제
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)