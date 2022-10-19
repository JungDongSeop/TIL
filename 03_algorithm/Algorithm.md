# Algorithm

이왕이면 지킬 것

- 주석, 변수명 이해하기 쉽게 할 것

- 익숙해질 때까지 내장함수 막 쓰지 말 것

- 1일 1알고리즘

- f스트링 안에 계산식 넣지 않기 (이왕이면 변수명만 넣기)

배운 점?

- 중복을 고려하지 않아야 할 경우, 집합 생각해보기

## 정렬

버블 정렬

- 인접한 2개의 값을 비교, 교체

- 복잡도 O(n^2)

카운트 정렬

- 주어진 행렬의 i번째 값 a에 대해, 새로운 count_list 만든 뒤 count_list[a] += 1

- 복잡도 O(n+k) `k는 값 a 중 최댓값`

선택 정렬

- 주어진 자료 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환(맨 앞으로)

- 교환 횟수가 버블, 삽입 정렬보다 작다

- 복잡도 O(n^2)

## 브루트 포스 (완전탐색검사)

모든 경우의 수를 검사

#### 비트 연산자

`&` : 비트 단위로 AND 연산

`|` : 비트 단위로 OR 연산

`1<<n` : 2^n, 즉1짜리 bit를 오른쪽으로 n칸 이동

`i&(1<<j)` : i의 j번째 비트가 1인지 아닌지를 검사

이를 이용해서 부분집합을 생성하는 코드 만들 수 있음

#### 검색

저장된 자료 중 원하는 항목을 찾는 작업

탐색 키 : 자료를 구별하여 인식할 수 있는 키

- 순차 검색 (전부 순회하여 조사)
  
  - 일렬로 되어 있는 자료 검색, 간단, 비효율적
  
  - 복잡도 O(n) (정렬되어 있든 아니든)

- 이진 검색 (절반씩 나눠서 조사)
  
  - 자료의 가운데 키 값과 비교하여 다음 검색의 위치 결정, 정렬된 형태만 가능
  
  - 검색 범위의 시작 s, 끝 e를 이용하여 반복문 수행 (`while s <= e` 형태 추천, 이후 `s=m+1`, `e=m-1`)

- 해쉬 

#### 전치행렬

`arr = list(zip(*arr))`

#### 배열의 상하좌우 구하기

```python
di = [0,0,-1,1]
dj = [-1,1,0,0]
```

해서 각 i, j에 i+di, j+dj

#### 순열

TSP (Traveling Salesman Problem) 등에 적용 가능

- 최소 변경을 통한 방법 

  - 각 순열들은 이전의 상태에서 요소 2개만을 바꿔 생성 가능

  - ```python
    perm(n, k):
        if n == k:
            print arr
        else:
            for i in range(k, N):
                arr[i], arr[j] = arr[j], arr[i]
                perm(n, k+1)
                arr[i], arr[j] = arr[j], arr[i]
    ```

  - d

#### 부분집합 전부 출력

```python
for i in range(1<<N):
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()
```

## 백트래킹

모든 경우를 '탐색', 이전 단계로 거슬러 올라가 다른 가능성을 찾는 것

    `모든 가능성을 찾는 건 맞지만, 가능성 없는 경우는 제외`

1 2 3 6

1 2 4 5

## 스택

- 선형구조, 후입선출

- 저장소 자체를 스택이라 부르기도 함

- 스택에서 마지막 삽입된 원소의 위치를 top (stack pointer) 이라 함

- 연산
  
  - 삽입: 저장소에 자료 저장. push라 부름
  
  - 삭제 : 저장소에서 자료 꺼냄, 꺼낸 자료는 삽입 자료의 역순으로 꺼냄, pop
  
  - isempty (공백 확인, pop 전에 사용?), peek (top에 있는 원소를 반환)

append, pop은 느림, 그 때 배열 크기를 정하고, 스택을 함수로 구현하면 괜찮은 경우가 있다?

구현

```python
stacksize = 10
stack = [0] * stackSize
top = -1


top += 1        # top 증가
stack[top] = 1    # 스택에 push

top += 1        # push(2)
stack[top] = 2

top -= 1        # pop
temp = stack[top + 1]
print(temp)

temp = stack[top]
top -= 1
print(temp)
```

- 고려사항 : 스택의 크기 변경이 어렵다. 이는 동적 연결리스트를 이용하여 해결(복잡하지만, 메모리를 효율적으로 사용 가능)

스택 응용 : 괄호 검사 문제 풀기, 프로그래밍 언어의 함수 실행

## 재귀 호출

- 자기 자신을 호출하여 순환 수행되는 것

- 경우에 따라 일반적인 함수보다 간단하고 크기도 작게 작성 가능

- 메모이제이션을 활용해 실행 속도 향상 가능

- memoizatioin을 재귀적 구조에 사용하는 것보다, 반복적 구조로 DP를 구현하는 것이 더 효율적 (함수 호출 없이 테이블을 체우므로)

## DP (Dynamic programing)

- 최적화 문제를 해결하는 알고리즘, 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 뒤, 그 해들을 이용하여 큰 부분문제들을 해결

- 메모이제이션도 DP의 일종

- top-down : 하향식 접근, 큰 문제들을 작은 문제들로 나누고, 작은 문제들을 풂

- bottom-up : 작은 문제들을 먼저 풀고, 이후 큰 문제들을 풂 (타뷸레이션, tabulation)

피보나치 dp 예시

```python
def fibo_dp(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])

    return f[n]
```

## DFS, BFS

비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

## DFS

- 깊이 우선 탐색(Depth First Search)

- 갈 수 있는 한 깊이 탐색, 더이상 갈 수 없으면 마지막 갈림길로 되돌라와서 다른 방향으로 탐색을 반복

- 가장 마지막의 갈림길의 정점으로 되돌아가서 DFS를 반복하니, 후입선출 구조의 스택 사용

- 스택 사용

- 구조
  
  1. 시작 정점 v를 결정하여 방문
  
  2. v에 인접한 정점 중에서 
     
     - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문
     
     - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2. 반복
  
  3- 스택이 공백이 될 때까지 2.를 반복

- 논리 구조       

```
visited[], stack[] 초기화 (visited는 전부 False로, stack은 공백으)
DFS(v)
    시작점 v 방문
    visited[v] 가 true;
    while{
        if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            push(v);
            v <= w;  (w에 방문)
        else
            if (스택이 비어 있지 않으면)
                v = pop(stack)
            else
                break
    }
end DFS
```

- 코드

```python
adjList = [[1,2], .. ] (인접한 목록 리스트)
def dfs(v, N):            # N은 정점의 개
    visited = [0] * N    # visited
    stack = [0] * N        # stack
    top = -1

    visited[v] = 1        # 시작점 방문 표시
    while True:
        for w in adjList[v]: # if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:  # push(v);
                top += 1
                stack[top] = v  
                v = w            # v <= w; (w에 방문)
                visited[w] = 1   # visited[w] <= True
                break
        else:                    # w가 없으면
            if top != -1:        # 스택이 비어있지 않은 경우
                v = stack[top]       # pop
                top -= 1
            else:                # 스택이 비어있으면
                break                # while 빠져나감
```

재귀로도 표현 가능

```python
def DFS(start):
    visited[start] = 1
    print(start, visited)

    for next in range(1, V+1):
        if G[start][next] == 1 and visited[next] == 0:
            DFS(next)
```

## BFS

- 너비 우선 탐색(Breadth First Search)
- 큐 사용

## 덱



명령은 총 여덟 가지이다.

- push_front X: 정수 X를 덱의 앞에 넣는다.
- push_back X: 정수 X를 덱의 뒤에 넣는다.
- pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 덱에 들어있는 정수의 개수를 출력한다.
- empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
- front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.





## 다익스트라

- 큐를 사용, 큐는 우선순위 힙을 사용해 현재까지 이동거리가 가장 작은 값을 맨 앞에 오도록 작성 (최소힙)

  이 덕분에 복잡도 $O(M)$ 이 아니라 $O(\log M)$이 가능

- 다음에 갈 점 next에 대해서, 여태까지 조사한 거리보다 더 빠른 이동이 가능하면, 조사

- 음의 가중치는 조사 불가. 음의 가중치가 있다면 벨만-포드 사용

나무위키 다익스트라 참조

```python
def dijkstra(start, goal):
    distance = [INF] * (N+1)        # 해당 노드까지의 거리 리스트
    heap = []                       # 우선순위 큐

    heappush(heap, (0, start))      # 튜플의 크기 비교는 앞에 값부터 비교. 이를 이용해 원소 (거리, 노드)를 힙에 추가
                                    # 우선순위 큐를 사용해야, 최소값을 구하는 복잡도가 O(log M)이 된다. 최종 복잡도는 O(M log M)
                                    # 그냥 최소값을 구하면 복잡도가 O(M), 결국 최종 복잡도는 O(M^2)
    distance[start] = 0

    # 방문한 도시가 있는 동안
    while heap:
        dist, now = heappop(heap)       # 이동 거리가 최소인 노드를 꺼냄
        if distance[now] < dist:            # 그 노드보다 효율적인 움직임이 있으면, 넘어감
            continue
            
        # 갈 수 있는 길들 heap에 추가 (자동 정렬 됨),
        for next, long in adjList[now]:
            cost = dist + long
            # 조사한 거리보다 더 빠른 이동이 가능하면
            if distance[next] > cost:
                distance[next] = cost
                heappush(heap, (cost, next))
```



## 분리 집합 알고리즘

- 트리를 사용
- 서로 분리된 단순 그래프에서 임의의 노드 및 간선이 추가된 경우, 노드 A와 B가 연결된 상태인지 확인하기 위해 DFS, BFS를 사용하는 건 너무 비효율적이다.
- 분리된 단순그래프를 트리 형태로 구현. 만약 트리 T와 T'을 연결하는 간선이 추가된 경우 둘의 부모 노드를 연결하는 간선 하나만 그린다.
- 그러면 노드 A와 B가 연결된 형태인지는 트리의 높이 만큼의 복잡도만 사용해서 계산 가능

백준 16566 카드게임

```python
# tree에 적절한 부모 노드를 찾는 함수
def find(x):
    if x == tree[x]:
        return x

    v = find(tree[x])
    tree[x] = v
    return v

# 두 개의 분리노드를 연결하는 함수 (a의 부모노드를 b로)
def union(a, b):
    if b >= M:
        return 
    a = find(a)
    b = find(b)

    tree[a] = b

idx = find(idx)
print(all[idx])
union(idx, idx+1)

# 문제는 반복문으로도 풀었음
```



## 벨만 포드 알고리즘

- 그래프의 최단 거리를 찾는 알고리즘
- 모든 V에 대해서, 모든 E를 순회 
- 어떤 간선 (s, e, d)에서 distance[e]를 교체할 수 있을 정도로 이득인 경우가 있으면(더 짧은 이동 방법), distance[e] 수정
- 다익스트라보다 느리지만, 음의 가중치도 계산할 수 있다. (모든 V에 대해 모든 E를 조사하니)

백준 1865 웜홀

```python
# 벨만-포드 알고리즘
def bellman_ford(start):
    distance = [INF] * (V+1)
    distance[start] = 0

    # 모든 노드에 대해
    # (마지막 노드는 빼도 됨. 어차피 V와 연결된 나머지 점들에서
    #  V와 연관된 간선들을 전부 조사했으니)
    for v in range(1, V+1):
        # 모든 간선에 대해 조사
        for s, e, d in edges:
            cost = distance[s] + d
            # 만약 더 짧은 길이 존재하면, 길이 교체
            # if distance[s] != INF and distance[e] > cost:     # 처음에 이렇게 하니, 1이 도달하지 못하는 음의 사이클을 무시
            if distance[e] > cost:
                distance[e] = cost
            	if v == V:				# 이 경우 음의 사이클이 존재
                    return False
```



## 플로이드 워셜 알고리즘

- 그래프에서 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘. DP? 타뷸레이션? 의 일종

- 시간복잡도는 $O(V^3)$

- 방법

  임의의 노드 **s**에서 **e**까지 가는 데 걸리는 최단거리를 구하기 위해, **s**와 **e** 사이의 노드인 **m**에 대해 **s**에서 **m**까지 가는 데 걸리는 최단거리와 **m**에서 **e**까지 가는 데 걸리는 최단거리를 이용

- 코드

  ```python
  d = [[INF] * (N+1) for _ in range(N+1)]			# 이후 주어진 버스 노선들(s, e, d)로 리스트 수정
  
  for m in range(1, N+1):
      for s in range(1, N+1):
          for e in range(1, N+1):
              if s == e:
                  d[s][e] = 0
              if d[s][e] > d[s][m] + d[m][e]:
                  d[s][e] = d[s][m] + d[m][e]
  ```

- 설명

  - m == 1일 때, 1과 직접적으로 연결된 모든 노드 (s, e)들에 대해서 d 최소값 저장   

    (s, 1, e) 꼴

  - m == 2일 때, 1과 2를 지나는 연결된 모든 노드 (s, e)들에 대해서 d 최소값 저장   

    (s, 1, e) (s, 2, e) (s, 1, 2, e) (s, 2, 1, e) 꼴

  - 반복. 



## 이진 탐색

```python
# 이진탐색 하는 함수. 만약 정확한 값이 없으면, 바로 오른쪽 인덱스를 출력
def bin_search(l, r, target, arr):
    if l > r:
        return l        # 없으면 a[i]<target<a[i+1] 일 때 i+1 출력
    mid = (l + r) // 2

    if target == arr[mid]:
        return mid
    if target > arr[mid]:       # 오른쪽에 있음
        l = mid + 1
    else:
        r = mid - 1

    return bin_search(l, r, target)
```





## 투 포인터

1차원 배열이 있을 때, 이 배열에서 각자 다른 원소를 가리키는 2개의 포인터를 조작하는 알고리즘

백준\_2467_용액 (내 풀이는 투포인터 안씀)



## LIS

최장 공통 부분 수열

그래프를 채워나가는 DP 방식으로 해결 가능. $O(n^2)$

$O(n\log n)$으로 가능

- `largest = []` 리스트를 만든 뒤, 수열을 순회하면서 숫자 a에 대해 이분탐색으로 가장 큰 숫자가 나오면 append, 그게 아니면 a 보다 큰 수 중 제일 작은 수를 a로 교체. 

  이 때 `len(largest)`가 바로 LCS의 길이

- 이 방식으로는 LIS의 길이만 구하고, LIS 자체는 구할 수 없다. 이를 위해 `record_idx = [0] * (N)` 만든 뒤, i번째 값이 largest에 삽입 될 때 largest의 해당 인덱스를 record_idx에 저장. 

  이러면 나중에 record_idx에 대해 `for i in range(N-1, -1, -1)`, record_idx 가 1씩 작아지는 i들을 찾아 따로 저장하면 된다.

-  코드 : 백준\_14003_가장 긴 증가하는 부분 수열 5

- 이분탐색은 `from bisect import bisect_left, bisect_right`



## LCS

최소 공통 부분 수열

LIS 를 이차원 리스트 DP로 $O(MN)$으로 해결한 것처럼 해결

백준\_9251_LCS

```python
A, B = input(), input()
graph = [[0] * len(B) for _ in range(len(A))]

# A, B를 행, 열로 갖는 그래프 만들기
# 만약 A[a], B[b]가 겹치면, graph[a][b] == graph[a-1][b-1] + 1
# 만약 안겹치면, 바로 위 or 왼쪽 중 큰 값
for a in range(len(A)):
    for b in range(len(B)):
        if A[a] == B[b]:
            graph[a][b] = (graph[a-1][b-1] if a-1 >= 0 and b-1 >= 0 else 0) + 1
        else:
            graph[a][b] = max(graph[a][b-1] if b-1 >= 0 else 0, graph[a-1][b] if a-1 >= 0 else 0)

print(graph[-1][-1])
```



## 중간에서 만나기

- 큰 문제를 절반으로 나눠서 해결하는 방법

- 이후 투포인터 등을 활용해 효율적으로 문제 해결 가능

- 백준 1208 참조

  - 경우의 수 $2^{40}$ 을 $2^{20} + 2^{20}$ 으로 나눠서 해결 가능






## 최소 신장 트리

- MST

  - prim : 정점 기준, 정점의 개수가 적을 때 유리, $O(V+E)\log V)$
  - kruskal : 간선 기준, 간선의 개수가 적을 때 유리, $O(E \log V)$

- 다른 사람들 풀이를 보니, 크루스칼에서 매번 parent[x]를 바꿔서 최대한 트리의 높이를 줄였다. 

  이 방법 좋은듯

  ```python
  def find(x):
      if x != parent[x]:	
          # x = parent[x]			# 내가 하던 방식
          parent[x] = find(parent[x])
      return parent[x]
  ```




## 위상 정렬

순서가 정해져있는 작업을 차례로 수행할 때, 그 순서를 결정하는 알고리즘

ex) 대학 수강신청 시 선수과목 등

순서

1. 큐를 사용, 진입노드가 0인 노드들 전부 큐에 삽입

2. 이후 큐에서 노드를 하나 pop, 그 노드를 now 라 하자.

3. 인접 리스트에서 다음으로 갈 수 있는 노드들 순회, 그 노드들 중 하나를 next라 하자.

4. next의 진입 노드를 1 감소 (이미 고려한 간선은 삭제하는 효과). next를 큐에 삽입.

   이후, 만약 next의 진입 노드가 0개이면 next를 큐에 삽입

5. 반복

백준\_1005_ACM Craft

- https://developmentdiary.tistory.com/465 참조

  ```
  이렇게 하면 방향순대로 모든 경우를 순회할 수 있음..?
  # 한 번 간 간선을 삭제하는 이유?
  # 위상 정렬은 싸이클이 없고, 간선을 삭제해가면서 진입차수가 가장 작은 노드들을 먼저 삽입하므로
  # 어차피 아래에서부터 테이블을 채워나가는 효과가 생긴다.
  # 우리의 목표 건물을 맨 위라고 하면, 어차피 맨 왼쪽부터 고려하면서 타뷸레이션 하는 느낌
  ```

- 코드

  ```python
  def func():
      global answer
  
      q = deque()
      for i in range(1, N+1):     # 진입차수가 0인 노드들 큐에 넣음
          if not degree[i]:
              q.append(i)
              dp[i] += times[i]
  
      # 큐가 있는 동안 반복
      while q:
          now = q.popleft()
  
          for next in adjList[now]:
              degree[next] -= 1                               # 진입 차수 줄이고
              dp[next] = max(dp[next], dp[now] + times[next])  # 작업 시간 갱신
              if degree[next] == 0:                           # 진입차수 0인 노드 삽입
                  q.append(next)
  
  
  T = int(sys.stdin.readline())
  for tc in range(T):
      N, K = map(int, sys.stdin.readline().split())                # 건물 개수, 건물 순서 규칙 개수
      times = [0] + list(map(int, sys.stdin.readline().split()))    # 건물 별 짓는 시간
      arr = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
      W = int(sys.stdin.readline())                                # 목표 건물
  
      parent = list(range(N+1))           # 분리 집합
      adjList = [[] for _ in range(N+1)]  # 인접 리스트
      degree = [0] * (N+1)                # 진입 차수
      dp = [0] * (N+1)                    # 작업 시간 타뷸레이션
      for a, b in arr:
          adjList[a].append(b)
          degree[b] += 1
  
      # 정답 구하기
      func()
      print(dp[W])
  ```






## 세그먼트 트리

구간을 저장하기 위한 이진 트리

ex) 여러 개의 데이터가 존재할 때 특정 구간의 합을 구하는 데 사용하는 자료 구조.

시간 복잡도 $O(\log n)$으로 부분합을 구할 수 있다.

https://velog.io/@heyoni/2042 참조



1. segment_tree = [0] * (4*N) 으로 트리를 구현한다.

   이 때 arr의 원소들은 리프 노드에 저장함. arr[2 * idx + 1]을 해도 인덱스 에러가 나지 않기 위해 트리의 크기를 충분히 할당

2. 재귀함수를 사용하여 트리를 채운다.

3. 재귀함수를 활용하여 트리에 저장된 값을 (log n) 개만 바꾼다.

4. 재귀함수를 활용하여 행렬의 부분합을 구한다.

트리 만들기

```python
# 세그먼트 트리를 채우는 함수
# idx 는 segment_tree 리스트의 인덱스
# start, end 는 그 segemnt_tree[idx] == sum(arr[start:end+1]) 이 되도록 하는 start 와 end
def tree_fill(start, end, idx):
    # 리프 노드 채우기
    if start == end:
        segment_tree[idx] = arr[start]
        return segment_tree[idx]

    # 현재 노드 채우기
    mid = (start + end) // 2
    segment_tree[idx] = tree_fill(start, mid, idx*2) + tree_fill(mid+1, end, idx*2+1)
    return segment_tree[idx]

arr = [0] + list(map(int, input().split())
N = len(arr) - 1                 
segment_tree = [0] * (4*N)

# 세그먼트 트리 채우기
tree_fill(1, N, 1)
```



트리 값 수정

```python
# 트리에서 리프 노드의 숫자가 바뀌었을 때, 트리 전체의 부분합들 수정
# target 은 arr[target] = num 으로 수정될 때의 target (num 은 수정할 값, target 은 수정할 인덱스)
# diff 는 num - arr[target]
def tree_update(start, end, idx, target, diff):
    # 트리 수정
    segment_tree[idx] += diff

    # 만약 리프 노드에 도달하면 (arr[target] 을 나타내는 노드에 도달하면)
    if start == end:
        return

    # 재귀함수로 리프 노드를 찾아간다.
    mid = (start + end) // 2
    if target <= mid:
        return tree_update(start, mid, idx*2, target, diff)
    else:
        return tree_update(mid+1, end, idx*2+1, target, diff)

tree_update(1, N, 1, target, num - arr[target])		# 트리 수정
arr[target] = num									# 배열 수정
```



부분합 구하기

```python
# 목표로 하는 부분합을 찾아가는 함수
# S, E 는 우리가 sum(arr[S:E+1]) 을 목표로 할 때의 S, E
def tree_find(start, end, idx, S, E):
    # 만약 현재 노드가 나타내는 부분합이 arr[S:E+1] 안에 있으면, 그 값 더함
    if S <= start and end <= E:
        return segment_tree[idx]
    # 만약 조사 범위를 벗어났으면, return 0
    if E < start or end < S:
        return 0

    # 재귀함수로 더 깊이 들어감
    mid = (start + end) // 2
    # 왼쪽 절반, 오른쪽 절반 탐색
    return tree_find(start, mid, idx*2, S, E) + tree_find(mid+1, end, idx*2 + 1, S, E)

print(tree_find(1, N, 1, S, E))
```













## 0-1 배낭 문제

조합 최적화 문제. DP와 백트래킹을 활용해 해결. 조금 약한 부분임

백준\_12865_평범한 배낭

- 타뷸레이션

```python
# 타뷸레이션으로 해결
N, K = map(int, input().split())

# 정답을 저장할 리스트
# answer[a][b] 는 물건 a개가 주어질 때, 정확히 무게 b를 갖는 조합의 최고 가치
answer = [[0] * (K+1) for _ in range(N+1)]      

# answer 채우기
for n in range(1, N+1):
    weight, value = map(int, input().split())
    # 모든 무게에 대하여
    for k in range(1, K+1):
        # 무게 k가 weight를 담은 상태일 수 있을 때
        if k >= weight:
            answer[n][k] = max(answer[n-1][k], value + answer[n-1][k-weight])
        # 아닐 때 (그냥 안 담음)
        else:
            answer[n][k] = answer[n-1][k]

print(answer[N][K])
```

백준\_7579_보석 가게

- 재귀함수 활용한 DP (시간초과)

- ```python
  def knapsack(result, memory, idx):
      global answer
      if result >= answer:
          return 10001
      if memory >= M:     # 메모리 충분히 확보
          answer = result
          return result
      if idx == N:        # 메모리 확보 못했으면 중지
          return 10001
  
      else:
          # idx 번째  고르는 경우
          left = knapsack(result + cost[idx], memory + memories[idx], idx+1)
          # idx 번째 안고르는 경우
          right = knapsack(result, memory, idx+1)
          return min(left, right)
  ```

- 



## 크누스 최적화?

- `dp[i][j] = min(dp[i][k] + dp[k][j]) + C[i][j]` 형태의 점화식을 가지면서, `C[a][c]+C[b][d]≤C[a][d]+C[b][c]` 와 `C[b][c]≤C[a][d]` 를 만족할 때 사용 가능한 기법이다.
  - 시간복잡도 $O(n^3)$ 을 $O(n^2)$ 으로 줄여준다.
- 그런데 비실용적이라고? 잘 안쓰인다는 듯. 혹은 다른 방법이 더 빠르다던가.
- [여기](http://www.teferi.net/ps/%EA%B5%AC%EA%B0%84_%EB%B6%84%ED%95%A0_%EB%B0%A9%EC%8B%9D%EC%97%90_%EA%B4%80%ED%95%9C_dp#%ED%96%89%EB%A0%AC_%EC%97%B0%EC%87%84_%EA%B3%B1%EC%85%88) 참조
- 백준 11049 행렬 곱셈 순서 문제를 최적화 하는데 사용 가능



## 최적 이진 검색 트리

- 뭔지 모름. 이름만 들어봤다.
- [여기](http://www.teferi.net/ps/%EA%B5%AC%EA%B0%84_%EB%B6%84%ED%95%A0_%EB%B0%A9%EC%8B%9D%EC%97%90_%EA%B4%80%ED%95%9C_dp#%ED%96%89%EB%A0%AC_%EC%97%B0%EC%87%84_%EA%B3%B1%EC%85%88) 참조
- [Garsia-Wachs algorithm](https://en.wikipedia.org/wiki/Garsia%E2%80%93Wachs_algorithm) 위키
- 다음에 위키피디아 읽어보기




dd
