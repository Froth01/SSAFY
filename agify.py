import requests # 패키지를 사용하기 위해 import

response = requests.get('https://api.agify.io/?name=doi&country_id=KR')
data = response.json()
print(data)
print(data['age'])
