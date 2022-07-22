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

dict에서 key 검색할 때

```python
존재하지 않는 key 를 dictionary[key] 로 사용하면 오류 남
(없으면 안되는, 오류가 발생해야 하는 상황일 때는 dicts[keys] 사)
대신
dicts.get('keys') 사용, value 반환, keys가 없으면 None 반환
dicts.get('keys', '없을 시 이 문장 반환') 하면 뒤의 문자를 반
```

dict  크기 순으로 정렬

```python
# key 오름차순
sorted_dict = sorted(my_dict.items())
# key 내림차순
sorted_dict = sorted(my_dict.items(), key = lambda item: item[0], reverse = True)
# value 오름차순
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1])
# value 내림차
sorted_dict = sorted(my_dict.items(), key = lambda item: item[1], reverse = True)
```
