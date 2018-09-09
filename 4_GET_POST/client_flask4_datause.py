import requests

url = 'http://127.0.0.1:5000'

# 응답을 얻고자 하는 리소스 경로를 설정
response1 = requests.get(url + '/path data')
response2 = requests.get(url + '/get_hello', params = {'get_hello_data' : 'hello'})
response3 = requests.post(url + '/post_hi', data = {'post_hi_data': 'hi'})

# 응답 코드 출력
print(response1)
print(response2)
print(response3)

print(response1.url)
print(response2.url)
print(response3.url)

print(response1.content)
print(response2.content)
print(response3.content)

'''
<Response [200]>
<Response [200]>
<Response [200]>
http://127.0.0.1:5000/path%20data
http://127.0.0.1:5000/get_hello?get_hello_data=hello
http://127.0.0.1:5000/post_hi
b'path data'
b'hello'
b'hi'
'''
