import requests

url = 'http://127.0.0.1:5000'

# 응답을 얻고자 하는 리소스 경로를 설정
response_get1 = requests.get(url)
response_get2 = requests.get(url + '/get_hello')
response_get3 = requests.get(url + '/post_hi')

response_post1 = requests.post(url)
response_post2 = requests.post(url + '/get_hello')
response_post3 = requests.post(url + '/post_hi')

# 응답 코드 출력
print(response_get1)
print(response_get2)
print(response_get3)

print(response_get1.content)
print(response_get2.content)
print(response_get3.content)

print(response_post1)
print(response_post2)
print(response_post3)

print(response_post1.content)
print(response_post2.content)
print(response_post3.content)

# 만약 서버가 조건에 맞지 않은 요청을 했다면 [405]를 출력
'''
<Response [200]>
<Response [200]>
<Response [405]>
b'Hello flask'
b'Hello flask'
b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>405 Method Not Allowed</title>\n<h1>Method Not Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n'
<Response [200]>
<Response [405]>
<Response [200]>
b'Hello flask'
b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>405 Method Not Allowed</title>\n<h1>Method Not Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n'
b'Hi flask'
'''
