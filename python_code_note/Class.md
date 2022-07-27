# Class

클래스

- 클래스 변수 : class 안에서 정의된 변수, `class.name`으로 접근

- 인스턴스 변수 : 인스턴스가 갖는 변수, `instance.name`으로 접근

```python
class Doggy():
    num_of_dogs = 0                      # 클래스 변수
    birth_of_dogs = 0

    def __init__(self, name, breed):     # 인스턴스 변
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark():
        return '멍멍'

    def get_status():
        return f'birth_of_dogs : {Doggy.birth_of_dogs}\nnum_of_dogs : {Doggy.num_of_dogs}'


# d1 = Doggy('바둑이', '리트리버')         인스턴스 변
# d2 = Doggy('누렁이', '진돗개')
# print(Doggy.bark())
# print(Doggy.get_status())
```

rkrk
