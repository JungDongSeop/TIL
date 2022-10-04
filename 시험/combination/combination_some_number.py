def combination(arr, idx, n):
    if len(stack) == n:
        print(stack)
        return

    for i in range((stack[-1] if stack else -1) + 1, idx + (len(arr) - n) + 1):
        if arr[i] not in stack:
            stack.append(i)
            combination(arr, idx + 1, n)
            stack.pop()

stack = []
combination([0, 1, 2, 3, 4, 5, 6], 0, 4)