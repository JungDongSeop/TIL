
# 인접 리스트 adjList에 대한 BFS (V는 정점)
def BFS(S, G):
    visited = [False] * (V+1)
    queue = []
    queue.append((S, 0))
    visited[S] = True

    while queue:
        now, cnt = queue.pop(0)
        if now == G:
            return cnt

        for next in adjList[now]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, cnt+1))
    return 0

# 델타 탐색을 이용한 BFS
def BFS(rs, cs):
    visited = [[False]*N for _ in range(N)]
    queue = []
    queue.append((rs, cs))
    visited[rs][cs] = True

    while queue:
        r, c = queue.pop(0)
        # 도착점 '3'에 도착하면, return 1
        if arr[r][c] == 3:
            return 1

        # 상하좌우 움직임 구현
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            next_r, next_c = r + dr, c + dc

            if arr[next_r][next_c] != 1 and visited[next_r][next_c] == False:
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True

    return 0


arr = []
adjList = []
V = N = 0