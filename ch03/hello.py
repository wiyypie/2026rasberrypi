from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        a = request.form['text']
        return f"입력한 값: {a}"

    return '''
    <form method="post">
        <input type="text" name="text">
        <button type="submit">전송</button>
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

