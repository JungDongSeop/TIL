딕셔너리 생성
    dict_A = {a='apple', list=[1,2,3]}
    dict_A = dict()
딕셔너리 값 추가
    score['algorithm'] = 80
딕셔너리 값 수정
    score.update({'algorithm'} = 85)
    score ['algorithm'] = 85
딕셔너리 값 삭제
    del(score['algorithm'])
딕셔너리 2개 결합
    dic1.update(dic2)

딕셔너리 value들 평균
    sum(dict1.value()) / len(sum)

2차원 빈 배열
    arr = [[0 for _ in range(row)] for _ in range(column)]        전부 0
    arr = [range(row) for _ in range(column)]            전부 range(n)
    arr = [[0]*row for _ in range(column)]
    arr = numpy.ones((column, row))

배열 합치기
    list1 = [[1, 10], [2, 22], [3, 19]]
    list2 = [[4, 2], [5, 9], [6, 3]]            

    list3 = list(map(list.__add__, list1, list2))
    print(list3)                [[1, 10, 4, 2], [2, 22, 5, 9], [3, 19, 6, 3]]    

list 문자열로 출력
    string = ''.join(a)             list 요소 사이에 아무것도('') 안넣음
