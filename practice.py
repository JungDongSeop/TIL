N = int(input())
arr = list(map(int, input().split()))

def sum_of_stack(stack, answer):
    tmp = 0
    for i in stack:
        tmp += arr[i-1]
    return min(answer, abs(all_sum - 2*tmp))

def check():
    # 시작점 1인 BFS
    queue = [1]
    visited = [False] * (N+1)
    check_set = set([1])
    while queue:
        now = queue.pop(0)
        if not visited[now]:
            visited[now] = True
            for next in adjList[now]:
                queue.append(next)

        for i in queue:
            check_set.add(i)
    # 이 때 전부 연결했으면, check 완료
    if len(check_set) == N:
        return True

    # 전부 연결 못했으면, 연결 안 한 tmp_start 찾아서 다시 BFS
    tmp_start = 0
    for j in range(1, N+1):
        if j not in check_set:
            tmp_start = j
            break

    # 다시 BFS
    queue = [tmp_start]
    visited = [False] * (N + 1)
    visited[tmp_start] = True
    check_set_2 = set()
    while queue:
        now = queue.pop(0)
        for next in adjList[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
        for i in queue:
            check_set_2.add(i)

    if len(check_set.union(check_set_2)) == N:
        return True

    return False

def check_reaminder(stack):
    tmp_start = 0
    for j in range(1, N + 1):
        if j not in stack:
            tmp_start = j
            break
    short_adjList = []

    queue = [tmp_start]
    visited = [False] * (N + 1)
    check_set = set([1])
    while queue:
        now = queue.pop(0)
        if not visited[now]:
            visited[now] = True
            for next in adjList[now]:
                queue.append(next)

        for i in queue:
            check_set.add(i)
    # 이 때 전부 연결했으면, check 완료

def DFS():

    if not check():
        return -1

    answer = 10000
    for qq in range(1, N+1):
        stack = [qq]
        visited = [False] * (N+1)
        visited[qq] = True

        while stack:
            now = stack[-1]
            if adjList != []:
                for next in adjList[now]:
                    if not visited[next]:
                        stack.append(next)
                        visited[next] = True
                        break
                else:
                    stack.pop()
            else:
                return -1



            answer = sum_of_stack(stack, answer)

    return answer



adjList = [0] * (N+1)
for q in range(1, N+1):
    tmp_list = list(map(int, input().split()))
    tmp_list.pop(0)
    adjList[q] = tmp_list

all_sum = sum(arr)
# print(adjList)
print(DFS())