from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html',
                            title = "index with Jinja",
                            message = "What's your name?")

@app.route('/', methods = ['POST'])
def form():
    field = request.form['field']
    return render_template('index.html',
                            title="index with Jinja",
                            message = "Hi, %s" % field)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
