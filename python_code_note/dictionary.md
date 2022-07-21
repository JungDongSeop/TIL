딕셔너리 생성

```python
dict_A = {a='apple', list=[1,2,3]}
dict_A = dict()
```

딕셔너리 값 추가

```python
dict_1['algorithm'] = 80
```

    딕셔너리 key 값에는 immutable만 들어갈 수 있음

    딕셔너리 value는 전부 가능

딕셔너리 값 수정

```python
dict_1.update({'algorithm'} = 85)
dict_1['algorithm'] = 85
```

딕셔너리 값 삭제

```python
del(dict_1['algorithm'])
```

추가 메서드

```python
dict_1.keys()        # {[key_1, key_2]}
dict_1.values()        # {[valus_1, calue_2]}
dict_1.items()        # {[(key_1, value_1), (key_2, value_2)}
```

딕셔너리 2개 결합

```python
dic1.update(dic2)
```

딕셔너리 value들 평균

```python
sum(dict1.value()) / len(sum)
```
