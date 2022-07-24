2차원 빈 배열

```python
arr = [[0 for _ in range(row)] for _ in range(column)] # 전부 0
arr = [range(row) for _ in range(column)]             # 전부 range(n)
arr = [[0]*row for _ in range(column)]                # 전부 0
arr = numpy.ones((column, row))                        # import numpy
```

배열 합치기

```python
list1 = [[1, 10], [2, 22], [3, 19]]
list2 = [[4, 2], [5, 9], [6, 3]]
list3 = list(map(list.__add__, list1, list2))
print(list3)              #[[1, 10, 4, 2], [2, 22, 5, 9], [3, 19, 6, 3]]    
```

배열 최댓값

```python
max(list1)
min(list1)
```

list 관련 함수

```python
list1.count(1)    # list 안의 특정 원소 개수 세기
listA.sort()    # sort(reverse = True) 하면 역으로 정렬
sorted(listA)    # sort()와 달리 새 목록 반환 (sort는 그 list 내부에서 정)
```

list 문자열로 출력

```python
string = ''.join(a)            #list 요소 사이에 아무것도('') 안넣음
```

문자열 출력(string interpolation)

```python
name = '철수'
print(f'안녕, {name}야')            # f
print('안녕, {}야'.format(name))    # format 형
```

string 은 immutable?? 몰랐음

문자열 안의 특정 문자열 제거

```python
str = "hello, world"
new_str = str.replace(',', '', 1)    # str의 ',' 를 1개만 삭제
result = re.sub(',', '', str)        # import re 해야함
```

list 정령

```python
listA.sort()    # sort(reverse = True) 하면 역으로 정렬
sorted(listA)
```
