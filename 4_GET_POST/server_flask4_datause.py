from flask import Flask, request

app = Flask(__name__)

# HTTP 메서드 타입 중에서 GET과 POST에 따라 요청 처리 후 데이터 사용

@app.route('/<name>', methods = ['GET'])
def flaskworld(name):
    return name


# GET 메서드 타입에 대한 요청처리
@app.route('/get_hello', methods = ['GET'])
def helloworld():
    return request.args.get('get_hello_data')

# POST 메서드 타입에 대한 요청처리
@app.route('/post_hi', methods = ['POST'])
def hiworld():
    return request.form['post_hi_data']


if __name__=="__main__":
    app.run(port=5000)

'''
127.0.0.1 - - [16/Aug/2018 18:29:38] "GET /path%20data HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2018 18:29:38] "GET /get_hello?get_hello_data=hello HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2018 18:29:38] "POST /post_hi HTTP/1.1" 200 -
'''
