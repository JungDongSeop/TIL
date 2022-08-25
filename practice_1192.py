N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

answer_1 = 0
answer_2 = 0
# 0이 포함된 장갑은 숫자만 더하고 없애버림
for i in range(N-1, -1, -1):
    if arr1[i] == 0 or arr2[i] == 0:
        answer_1 += arr1[i]
        answer_2 += arr2[i]
        arr1.pop(i)
        arr2.pop(i)

tmp_1 = 0
tmp_2 = 0
answer = 100000000000000

# 나머지 장갑 숫자
answer_tmp_1 = 0
answer_tmp_2 = 0

what_i = 0
what_j = 0

if N == 1:
    print(1)
    print(1)

else:
    # 2개 고를 수 있는 경우의 수 순회
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            # 2가지 방법 중에서 어느 방법이 더 작은지 비교
            # (max+1, 1), (1, max+1)
            max_1 = max(arr1[i], arr1[j])
            # min_1 = min(arr1[i], arr1[j])
            max_2 = max(arr2[i], arr2[j])
            # min_2 = min(arr2[i], arr2[j])

            if max_1 > max_2:
                tmp_1 = 1
                tmp_2 = max_2 + 1
            else:
                tmp_1 = max_1 + 1
                tmp_2 = 1

            if answer > sum(arr1) + sum(arr2) - arr1[i] - arr1[j] - arr2[i] - arr2[j] + tmp_1 + tmp_2:
                answer = sum(arr1) + sum(arr2) - arr1[i] - arr1[j] - arr2[i] - arr2[j] + tmp_1 + tmp_2
                answer_tmp_1 = tmp_1 - arr1[i] - arr1[j]
                answer_tmp_2 = tmp_2 - arr2[i] - arr2[j]
                what_i, what_j = i, j
    print(sum(arr1) + answer_tmp_1 + answer_1)
    print(sum(arr2) + answer_tmp_2 + answer_2)
    # print(what_i, what_j)