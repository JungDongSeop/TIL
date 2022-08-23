import requests

url = 'https://api.agify.io/?name=michael'
response = requests.get(url).json()       #url에 요청을 보냄, 그 결과물을 response에 담음
print(type(response))
name = response['name']
age = response['age']
count = response['count']

print('이름이' + str(name) + ' 인 사람의 나이는' + str(age) + '입니다')