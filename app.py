from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html',
                            title = "index with Jinja",
                            message = [ck, rd, sel])

@app.route('/', methods = ['POST'])
def form():
    ck = request.form.get('check')
    rd = request.form.get('radio')
    sel = request.form.getlist('sel')
    return render_template('index.html',
                            title="index with Jinja",
                            message = [ck, rd, sel])

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
