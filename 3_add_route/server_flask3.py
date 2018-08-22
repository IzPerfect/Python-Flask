from flask import Flask

app = Flask(__name__)

# "/hello"와 "/hi"에 각각 라우팅한다
# "/hello"와 "/hi"라는 서로 다른 리소스 경로 설정
@app.route('/hello')
def helloworld():
    return "Hello flask"

@app.route('/hi')
def hiworld():
    return "Hi flask"


if __name__=="__main__":
    app.run(port=5000)
