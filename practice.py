import sys
sys.stdin = open('input.txt')

# 백준 12728번

# 2**30 < 2000000000 < 2**31

# N을 이진법으로 하고, 각 숫자에 대해 함수 실행
print(bin(7))
print(len(bin(7)))

def func(N):
    # N이 1이면
    if N == 1:
        return 6
    if N == 2:
        return 28
    if N == 3:
        return 144

    howlong = len(bin(N)) - 3

    
    r = 2**howlong
    return power_list[howlong] 
        
        

    pass

    # N이 짝수면
    if N % 2 == 0:
        return (1000 + func(N//2) ** 2 - 2 * four_list[((N//2 % 50) + 48) % 50]) % 1000
    # N이 홀수면
    # else:
    #
    #     return (1000 + power_list[] - 4*func(N-2)) % 1000


# 4의 거듭제곱을 1000으로 나눈 나머지는 4^2과 4^52 이 같다.
four_list = [16, 64, 256, 24, 96, 384, 536, 144, 576, 304, 216, 864, 456, 824, 296, 184, 736, 944, 776, 104, 416, 664, 656, 624, 496, 984, 936, 744, 976, 904, 616, 464, 856, 424, 696, 784, 136, 544, 176, 704, 816, 264, 56, 224, 896, 584, 336, 344, 376, 504]


# A^n + B^n 에서 n==2**i 일 때의 값은 power_list[i] 와 같다.
power_list = [1, 6, 28, 752]
ab_list = [1, 4, 16, 256]

for i in range(4, 32):
    ab_list.append((ab_list[i-1] ** 2) % 1000)
    power_list.append((power_list[i-1] ** 2 - 2 * ab_list[i] ** 2) % 1000)

# power_list = [1, 6, 28, 752, 912, 512, 232, 952, 112, 112, 232, 152, 312, 712, 232, 352, 512, 312, 232, 552, 712, 912, 232, 752, 912, 512, 232, 952, 112, 112, 232, 152]
# ab_list = [1, 4, 16, 256, 536, 296, 616, 456, 936, 96, 216, 656, 336, 896, 816, 856, 736, 696, 416, 56, 136, 496, 16, 256, 536, 296, 616, 456, 936, 96, 216, 656]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # tmp = (func(N) + 999) % 1000
    #
    # if tmp < 10:
    #     answer = '00' + str(tmp)
    # elif tmp < 100:
    #     answer = '0' + str(tmp)
    # else:
    #     answer = str(tmp)
    # print(f'Case #{tc}: {answer}')

