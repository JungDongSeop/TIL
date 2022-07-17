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
for i in range(100000):
    tmp_lotto = random.sample(range(45),6)

    if set(numbers) == set(tmp_lotto):      # first
        #print('congratulation!')
        count[0]+=1
    elif len(set(numbers).intersection(set(tmp_lotto))) == 5 and bonus_number in set(tmp_lotto):
        count[1]+=1
    elif len(set(numbers).intersection(set(tmp_lotto))) == 5:
        count[2]+=1
    elif len(set(numbers).intersection(set(tmp_lotto))) == 4:
        count[3]+=1


print(count)