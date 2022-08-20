# LIst

---

#### 시간 복잡도

- 빅-오 표기법

  계수는 생략, 최고차항만 고려하여 시간복잡도를 표시

---

#### 배열의 장점

- 여러 변수가 필요할 때 편하게 접근, 활용 가능

---

# 정렬

### 버블 정렬

- 인접한 원소끼리 계속 자리를 교환하면서 정렬

- 교환하며 자리를 이동하는 모습이 물 위로 올라오는 거품 같아서 버블정렬이라 함

- 복잡도 `O(n^2)` 

- 코드

  ```python
  def bubble_sort(arr, N):
      for i in range(N-1, 0, -1):
          for j in range(i):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
  ```

---

### 카운팅 정렬

- 정수 형태의 자료에만 적용 가능

- 각 항목의 발생 회수를 기록하기 위해, 정수 인덱스를 갖는 카운트 배열을 사용

- 집합 내의 가장 큰 정수를 알아야 카운트 배열 할당 가능

- 시간 복잡도 : `O(n+k)`, n은 리스트 길이, k는 정수의 최댓값

- 코드

  ```python
  def counting_sort(input_arr, k):
      counting_arr = [0] * (k+1)
      # 1. counting array에 arr내 원소의 빈도수 담기
      for i in range(0, len(input_arr)):
          counting_arr[input_arr[i]] += 1
          
      # 2. 누적(counting_arr 업데이트)
      for i in range(1, len(counting_arr)):
          counting_arr[i] += counting_arr[i - 1]
  
      # 3. result_arr 생성
      result_arr = [-1] * len(input_arr)
  
      # 4. result_arr에 정렬하기(counting_arr를 참조)
      for i in range(len(result_arr) - 1, -1, -1):
          counting_arr[input_arr[i]] -= 1
          result_arr[counting_arr[input_arr[i]]] = input_arr[i]
  
      return result_arr
  
  ```


### 선택 정렬

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환

- 과정 

  - 주어진 리스트 중 최솟값을 찾는다
  - 그 값을 리스트 맨 앞의 값과 교환
  - 반복

- 시간 복잡도 O(n^2), 버블, 삽입 정렬보다는 적음

- 코드

  ```  python
  def selection_sort(arr, N):
      for i in range(N-1):
          min_idx = i
          for j in range(i+1, N):
              if arr[min_idx] > arr[j]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
  ```

  

---

# 2차원 배열

- 2중 리스트를 통해 표현 가능

- 빈 2차원 배열 만들기 

  `arr = [[0] * N for _ in range(N)]`

### 배열 순회

- n X m 배열의 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회 : `for i in range(n):  for j in range(m): arr[i][j]`

  열 우선 순회 : `for j in range(m):  for i in range(n):  arr[i][j]`

  지그재그 순회 : `for i in range(n):  for j in range(m): arr[i][j + (m-1-2*j) * (i%2)]`

  전치 행렬(transpose) : `if i < j: arr[i][j], arr[j][i] = arr[j][i], arr[i][j] `

- 델타를 이용한 2차 배열 탐색

  2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

  ```python
  di = [0,0,-1,1]
  dj = [-1,1,0,0]
  for i in range(N):
      for j in range(N):
          for k in range(4):
              ni = i + di[k]
              nj = j + dj[k]
              if 0 <= ni < N and 0 <= nj < N:
                  test(arr[ni][nj])
  ```


---

# 비트연산자

- & : 비트 단위로 AND

- | : 비트 단위로 OR

- << : 피연산자의 비트 열을 왼쪽으로 이동

- \>> : 피연산자의 비트 열을 오른쪽으로 이동

  1 << n : 2^n, 즉 이진법 숫자 00001 에서 1을 오른쪽으로 n칸만큼 이동

  i & (1 << j) : i의 j번째 비트가 1인지 아닌지 검사

---



# 검색

저장되어 있는 자료 중 원하는 항목을 찾는 작업

- 탐색 키 : 자료를 구별하여 인식할 수 있는 키

### 검색 종류

- 순차 검색

  - 일렬로 되어 있는 자료를 순서대로 검색, 탐색 키를 찾는 방법

  - 간단하고 직관적, but 시간 복잡도가 높음 O(n)

  - 정렬되지 않은 경우에도 사용 가능

- 이진 검색

  - 자료의 가운데 항목과 키 값을 비교하여 다음 검색의 위치를 결정, 검색 계속 진행

  - 자료가 정렬된 경우에만 사용 가능

  - 코드

    ```python
    def binarySearch(arr, N, key):
        start = 0
        end = N-1
        while start <= end:
            middle = (start + end) // 2
            print(middle, arr[middle])
            if arr[middle] == key:
                return True
            elif arr[middle] > key:
                end = middle - 1
            else:
                start = middle + 1
        return False
    ```

    재귀함수 버전

    ```python
    def binarySearch(arr, start, end, key):
        if start > end:
            return False
        else:
            middle = (start + end) // 2
            # print(middle, arr[middle])
            if arr[middle] == key:
                return True
            elif arr[middle] > key:
                return binarySearch(arr, start, middle-1, key)
            else:
                return binarySearch(arr,  middle+1, end, key)
    ```

    

- 해쉬
