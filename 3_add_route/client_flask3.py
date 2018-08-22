import requests

url = 'http://127.0.0.1:5000'

# 응답을 얻고자 하는 리소스 경로를 설정
response1 = requests.get(url + '/hello')
response2 = requests.get(url + '/hi')


print(response1)# 서버가 응답한 값을 반환
print(response1.content)# HTML코드를 가져온다
print(response1.text)# HTML코드를 가져온다

print(response2)# 서버가 응답한 값을 반환
print(response2.content)# HTML코드를 가져온다
print(response2.text)# HTML코드를 가져온다

'''
<Response [200]>
b'Hello flask'
Hello flask
<Response [200]>
b'Hi flask'
Hi flask
[Finished in 0.304s]
'''
