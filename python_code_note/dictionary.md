딕셔너리 생성

```python
dict_A = {a='apple', list=[1,2,3]}
dict_A = dict()
```

딕셔너리 함수

```python
dict_1['algorithm'] = 80            # 값 추가        
dict_1.update({'algorithm'} = 85)   # 값 수정
dict_1['algorithm'] = 85            # 값 수정
del(dict_1['algorithm'])            # 값 삭제
dic1.update(dic2)                    # 딕셔너리 2개 결합
```

    딕셔너리 key 값에는 immutable만 들어갈 수 있음

    딕셔너리 value는 전부 가능

추가 메서드

```python
dict_1.keys()        # {[key_1, key_2]}
dict_1.values()        # {[valus_1, calue_2]}
dict_1.items()        # [(key_1, value_1), (key_2, value_2)]
```

딕셔너리 정렬

```python
dict_sorted = sorted(dictA.items())        # key 순으로 정렬, list로 나
dict_sorted = sorted(dictA.items(), key = operator.itemgetter(1))
                                    # value 순으로 정렬, import operator
dict_sorted = sorted(dictA.items(), key = lambda x: x[1])
                                    # value 순으로 정렬
                                    # 역으로 정렬 시 reverse = True 추가
```

딕셔너리 value들 평균

```python
sum(dict1.value()) / len(sum)
```
