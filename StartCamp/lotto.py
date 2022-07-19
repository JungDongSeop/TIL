import requests
import random

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'

aa = requests.get(url).json()               #get requests from lotto url
numbers = []
for i in range(6,0,-1):                     # the lottery winning number's key is 'drwtNo1', ...
    numbers.append(int(aa['drwtNo'+str(i)]))

bonus_number = int(aa['bnusNo'])            # bonus number

print(numbers, bonus_number)


tmp_lotto = random.sample(range(45),6)      # random lottery numberspy

count = [0,0,0,0]
for i in range(8145060):
    tmp_lotto = random.sample(range(1, 46),6)
    a = set(numbers)
    b = set(tmp_lotto)
    c = a.intersection(b)
    if len(c) == 6:      # first
        #print('congratulation!')
        count[0]+=1
    elif len(c) == 5 and bonus_number in set(tmp_lotto):
        count[1]+=1
    elif len(c) == 5:
        count[2]+=1
    elif len(c) == 4:
        count[3]+=1


print(count)