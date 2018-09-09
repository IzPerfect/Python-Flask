from flask import Flask, render_template

app = Flask(__name__)

# flask에서는 render_template를 사용하여 HTML을 불러올 수 있다
@app.route('/')
def flaskworld():
    return render_template('render_ex.html')

if __name__=='__main__':
    app.run(port=5100)
