from flask import Flask, request

app = Flask(__name__)

# HTTP 메서드 타입 중에서 GET과 POST에 따라 요청 처리

# GET vs POST
# GET은 'url + ?쿼리 스트링'의 형태로 주소줄에 정보를 노출한다
# 그리고 위의 형태로는 많은 양의 데이터를 전달하기 어렵다

# Post는 HTTP 메시지의 바디에 데이터를 포함하므로 많은 양의 데이터를 전달
# 또한 요청은 암호화 되기 때문에 데이터 변경 목적으로도 사용

# GET은 정보를 요청하고 얻을 때, POST는 수행할 때

# GET, POST 동시에 처리
@app.route('/', methods = ['GET', 'POST'])
def flaskworld():
    print(request.method)
    return "Hello flask"


# GET 메서드 타입에 대한 요청처리
@app.route('/get_hello', methods = ['GET'])
def helloworld():
    print(request.method)
    return "Hello flask"

# POST 메서드 타입에 대한 요청처리
@app.route('/post_hi', methods = ['POST'])
def hiworld():
    print(request.method)
    return "Hi flask"


if __name__=="__main__":
    app.run(port=5000)

'''
GET
127.0.0.1 - - [15/Aug/2018 21:21:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [15/Aug/2018 21:21:28] "GET /get_hello HTTP/1.1" 200 -
GET
127.0.0.1 - - [15/Aug/2018 21:21:28] "GET /post_hi HTTP/1.1" 405 -
POST
127.0.0.1 - - [15/Aug/2018 21:21:28] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [15/Aug/2018 21:21:28] "POST /get_hello HTTP/1.1" 405 -
POST
127.0.0.1 - - [15/Aug/2018 21:21:28] "POST /post_hi HTTP/1.1" 200 -
'''
