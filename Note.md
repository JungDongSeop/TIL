string interpolation     (보간법)

실수로 max 등 예약어에 할당을 해 버렸다  => 명령어 `del max` 실행

왜 안바뀌지? 원본에는 변화가 없다

```python
for i in range(len(fruit_list)):

    fruit_list[i].lower()
```



여러 줄에 걸친 숫자들 input

```python
list_1 = [list(map(int, input().split())) for i in range(N)]
```

바로 list 의 원소들로 비교

```python
S = [[x1, y1], [x2, y2]]
for x, y in S:
    x = x + y
```
