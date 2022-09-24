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

dd
