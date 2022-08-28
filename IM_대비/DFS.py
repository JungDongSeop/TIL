from pprint import pprint
import sys

sys.stdin = open('input.txt')


# 시작하는 정점 정보 전달 받아서
def DFS(start):
    stack = [start]
    visited = [0] * (V + 1)
    while stack:
        # 내 조사 대상 == stack의 마지막 정점
        start = stack.pop()
        if visited[start] == 0:
            visited[start] = 1
            # 모든 정점들 조사
            for next in range(1, V + 1):
                if G[start][next] == 1 and visited[next] == 0:
                    stack.append(next)

def DFS_recur(start):
    # visited는 외부에, 크기는 G와 같이
    visited[start] = 1

    for next in range(1, V+1):
        if G[start][next] == 1 and visited[next] == 0:
            DFS(next)








V, E = map(int, input().split())
data = list(map(int, input().split()))
print(V, E)
print(data)

G = [[0 for _ in range(E)] for _ in range(E)]
# pprint(G)

for i in range(E):
    '''
    G[1][2] = 1
    G[2][1] = 1

    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    # 0 2 4 6 8 10
    # 1 3 5 7 9 11
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1
pprint(G)
visited = [[False] * E for _ in range(E)]
DFS(1)