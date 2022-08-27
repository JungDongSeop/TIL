# 순열 사용
from itertools import permutations
print(list(permutations([1, 2, 3], 3)))

# 숫자 N에서 r개의 숫자를 뽑아 순열을 만드는 함수(직접 구현)
# 백트래킹의 일종

def permutation(idx, N, r):
    if idx == N:
        print(data[:r])
    else:
        for j in range(idx, N):
            data[idx], data[j] = data[j], data[idx]
            permutation(idx + 1, N, r)
            data[idx], data[j] = data[j], data[idx]


data = [1, 2, 3]
permutation(0, len(data), 2)