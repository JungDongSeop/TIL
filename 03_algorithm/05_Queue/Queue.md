# Queue

- 선입선출 구조 (FIFO)
- 삽입(enQueue)는 머리(Front)에서만, 삭제(deQueue)는 꼬리(Rear)에서만
- 연산
  - deQueue, enQueue, createQueue, isEmpty, isFull, Qpeek
  - front, rear 두 개의 변수를 사용해 활용
    - 생성 : front = rear = -1
    - 삽입 : rear += 1
    - 삭제 : front += 1
- 원형 큐
  - 선형 큐 사용시 발생하는 잘못된 포화상태 인식을 해결하기 위해 사용
  - front = (front + 1) % n, rear = (rear + 1) % n
- 우선순위 큐
  - 우선순위를 가진 항목들을 저장하는 큐
  - 삽입 시 우선순위가 높은 순서대로 배열, 삭제는 일반 큐와 같음
  - 단, 삽입이 일어날 때 발생하는 재배치로 인해 시간과 메모리 낭비가 큼

---

# BFS

- 큐 활용
- 시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 코드

  ```python
  def BFS(G, v):	# 그래프 G, 탐색 시작점 v
      visited = [0]*n		# n : 정점의 개수
      queue = []			# 큐 생성
      queue.append(v)		# 시작점 v를 큐에 삽입
      while queue:		# 큐가 비어있지 않으면
          t = queue.pop(0)	# 큐의 첫번째 원소 반환
          if not visited[t]:	# 방문되지 않은 곳이면
              visited[t] = True	# 방문한 곳으로 표시
              visit(t)
          for i in G[t]:		# t와 연결된 모든 선에 대해
              if not visited[i]:	# 방문되지 않은 곳이면
                  queue.append[i]	# 큐에 넣기
  ```

  
