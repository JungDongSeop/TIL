# Stack

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 특징
  - 선형 구조
  - 삽입, 제거가 한 곳에서만 이루어짐
  - 후입선출 (LIFO)
- 연산
  - 삽입 : stack에 자료를 저장. push라고 부름
  - 삭제 : stack에 자료를 꺼냄. pop이라고 부름
  - isEmpty (공백 확인), peek (stack의 top에 있는 원소 반환)

- 고려 사항
  - 미리 배열의 크기를 할당해야 할 경우, 스택의 크기 변경이 어렵다 (파이썬의 pop, append 혹은 재귀를 쓸 수 있지만, 연산 시간이 오래 걸리거나 재귀 깊이 한계에 도달하는 단점이 있음)
  - 동적 연결리스트를 이용하여 구현 가능. 구현이 복잡하지만 메모리를 효율적으로 사용 가능

- 재귀함수의 함수 호출도 스택의 일종

- 계산기의 구현 시에도 stack을 활용해 식을 후위표기식으로 표현하고, 다시 stack을 활용해 사칙연산을 수행할 수 있다.

---

# 동적 계획법

- 최적화 문제를 해결하는 알고리즘의 일종

- 입력 크기가 작은 부분 문제들을 모두 해결한 후, 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다

  

### 메모이제이션

- 재귀함수의 중복 호출을 막기 위해, 이전에 계산한 값을 저장하여 매번 다시 계산하지 않도록 하는 기술.
- 동적 계획법의 핵심 기술

---

# DFS

- 깊이 우선 탐색(Depth First Search)

- 갈 수 있는 한 깊이 탐색, 더이상 갈 수 없으면 마지막 갈림길로 되돌라와서 다른 방향으로 탐색을 반복

- 가장 마지막의 갈림길의 정점으로 되돌아가서 DFS를 반복하니, 후입선출 구조의 스택 사용

- 스택 사용

- 구조

  1. 시작 정점 v를 결정하여 방문

  2. v에 인접한 정점 중에서 

     - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문

     - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2. 반복

  3. 스택이 공백이 될 때까지 2.를 반복

---

# 백트래킹

- 해를 찾는 도중 막히면 되돌아가서 다시 해를 찾는 기법

- 최적화 문제와 결정 문제를 해결 가능

  - 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 yes or no로 답하는 문제

    ex) 미로 찾기, n-Queen, Map Coloring, 부분 집합의 합 문제

- 미로찾기의 경우, DFS처럼 구현한다. 이 때 1000걸음 안에 미로를 나가야 하는 경우, 백트래킹으로 연산 시간을 줄일 수 있다.
- 기법
  - 어떤 노드의 유망성을 점검한 후, 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
  - 가지치기 : 유망하지 않는 노드가 포함된 경로는 더 이상 고려하지 않는다.
- 절차
  1. 상태 공간 트리의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지 점검
  3. 만일 그 노드가 유망하지 않으면, 부모 노드로 돌아가서 검색 계속

---

# 분할 정복 알고리즘

- 설계 전략
  - 분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다.
  - 정복 : 나눈 작은 문제를 각각 해결한다
  - 통합 : (필요하다면) 해결된 해답을 모은다.

- 거듭제곱 연산 시, 보통 방법은 O(n), 분할 정복은 O(log_2 n)

### 퀵 정렬

- 주어진 배열을 두 개로 분할하고, 각각을 정렬
- 합병정렬과의 차이점
  1. 합병정렬은 그냥 두 부분으로 나눔, 반면 퀵 정렬은 기준 아이템 중심으로, 이보다 작은것과 큰 것으로 나눔
  2. 각 부분 정렬이 끝난 후, 합병정렬은 '합병'이란 후처리가 필요하나, 퀵 정렬은 그렇지 않음



- 코드

  ```python
  def quickSort(a, begin, end):
      if begin < end:
          p = partition(a, bdgin, end)
          quickSort(a, begin, p-1)
          quickSort(a, p+1, end)
  
  def partition(a, begin, end):
      pivot = (begin + end) // 2
      L = begin
      R = end
      while L < R:
          while L<R and a[L] < a[pivot]:
              L += 1
          while L<R and a[R] >= a[pivot]:
              R -= 1
          if L<R:
              if L == pivot:
                  pivot = R
              a[L], a[R] = a[R], a[L]
      a[pivot], a[R] = a[R], a[pivot]
      return R
  ```

  
