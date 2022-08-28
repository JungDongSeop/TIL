def combination(idx):
    if idx == N:
        print(stack)
        return

    stack[idx] = 0
    combination(idx + 1)
    stack[idx] = 1
    combination(idx + 1)

N = 6
stack = [0] * N
combination(0)


# 이 방법으로도 가능
stack = [i for i in range(N//2)]
def combination_2():
    while stack[0] != N//2:

        cnt = 0
        if stack[-1] == N-1:
            while stack[-1] == N-1:
                stack.pop()
                cnt += 1
                if stack[-1] + cnt == N-1:
                    stack[-1] += cnt
                else:
                    stack[-1] += 1

            for i in range(cnt):
                stack.append(stack[-1] + 1)
        else:
            stack[-1] += 1