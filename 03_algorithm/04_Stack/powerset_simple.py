data = list(range(1, 11))
N = len(data)

# idx : 현재 조사 위치
# total : 최종 만들어질 부분집합
def powerset(arr, idx, total):
    # 모든 원소들 조사했는지 알려면
    if idx == N:
        if sum(total) == 10:
            print(*total)
        return

    powerset(arr, idx+1, total + [arr[idx]])
    powerset(arr, idx+1, total)

powerset(data, 0, [])