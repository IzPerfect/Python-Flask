from flask import Flask
# 플라스크를 import한다

#
app = Flask(__name__)# flask객체 생성


# URL /의 GET요청에 대해 뷰 함수를 등록
# @표시는 데코레이터라고 한다
# Flask에서 URL을 처리하는 방법을 URL Dispath라고한다.
# 밑의 코드는 클라이언트가 /를 요청하면 helloworld라는 함수를 실행한다는 것
# route 데코레이터에 추가된 함수를 뷰 함수라고 한다
@app.route("/")
def helloworld():# 뷰 함수
    return "Hello world flask"

# 플라스크 실행
# host ='0.0.0.0'은 서버가 외부에도 연결가능하게 만듬
# port = 포트설정, debug = 디버그 설정
if __name__=="__main__":
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0')
