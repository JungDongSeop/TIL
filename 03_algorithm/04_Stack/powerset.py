# N : 최대 조사 위치
# result

# 문제 해답 출력 시 연산 여기에 추가
def process_solution(arr, k, result):
    if result != 10:
        return

    # 부분집합 출력
    for i in range(1, k+1):
        if arr[i]:
            print(data[i], end=' ')
    print()

# 유망성 조사(백트래킹 문제 풀 때) 시 조건 여기에 추가
def construct_candidator(c):
    c[0] = 0
    c[1] = 1
    return 2

def powerset(arr, k, n, result):
    # 넣거나 안넣거나
    c = [0] * MAXCANDIDATES

    # 언제까지 조사 할거냐
    if k == n:
        # 내가 원하는 수식이 만들어 졌는지 확인할 함수
        process_solution(arr, k, result)
    else:
        k += 1
        # 유망성 조사
        ncandidates = construct_candidator(c)
        for i in range(ncandidates):
            # 내가 집어넣어준 arr의 k번째 값을 쓰거나 안쓰거나
            arr[k] = c[i]
            # arr[k] 번째를 쓴 상황
            if arr[k]:
                powerset(arr, k, n, result + data[k])
            else:
                powerset(arr, k, n, result)

MAXCANDIDATES = 100
NMAX = 100
data = list(range(11))
arr = [0] * NMAX
powerset(arr, 0, 10, 0)