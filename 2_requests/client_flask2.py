import requests

url = 'http://127.0.0.1:5000'

response = requests.get(url)

print(response)# 서버가 응답한 값을 반환
print(response.content)# HTML코드를 가져온다
print(response.text)# HTML코드를 가져온다

'''
<Response [200]>
b'Hello world flask'
Hello world flask
[Finished in 0.274s]
'''
