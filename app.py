from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    n = random.randrange(1, 10)
    data = []
    for n in range(n):
        data.append(random.randrange(0, 100))
    return render_template('index.html',
                            title = 'temp',
                            message = 'sum:',
                            data = data)

@app.template_filter('sum')
def sum_filter(data):
    total = 0
    for item in data:
        total += item
    return total

app.jinja_env.filters['sum'] = sum_filter

@app.route('/next', methods = ['GET'])
def next():
    return render_template('next.html',
                            title = "Next page",
                            message = "sample",
                            data = ['one', 'two', 'three'])


"""
# Post Method
@app.route('/', methods = ['POST'])
def form():
    ck = request.form.get('check')
    rd = request.form.get('radio')
    sel = request.form.getlist('sel')
    return render_template('index.html',
                            title="index with Jinja",
                            message = [ck, rd, sel])
"""

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
