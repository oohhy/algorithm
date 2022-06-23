def dfs(graph, v, visited):
    # 방문한거 체크
    visited[v] = True
    # 방문한 번호 출력(줄바꿈 없이) 
    print(v, end=' ')

    for i in graph[v]:
        # if not 뒤의 결과가 False이면 아래 코드 실행
        if not visited[i]:
            dfs(graph, i, visited)

# visited = [False, False, ... , False] 방문한거 체크하는 용도
visited = [False] * 9 
# 1부터 순서대로 각 노드에사 갈 수 있는 노드 (작은 것 부터)
graph = [
        # 리스트 순서가 0부터 시작하기 때문에 넣어준것   
        [ ],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

dfs(graph, 1, visited)