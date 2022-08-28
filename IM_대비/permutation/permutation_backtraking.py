def permutation(idx):

    if idx == 5:
        print(use_list)
        return

    for i in range(4):
        if i not in use_list:
            use_list.append(i)
            permutation(idx + 1)
            use_list.pop()

use_list = []

permutation(1)