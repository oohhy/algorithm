stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
# 젤 오른쪽거 삭제
stack.pop() 
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
# 리스트 요소 역으로 출력
print(stack[::-1])