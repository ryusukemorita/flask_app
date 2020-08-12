from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            title="index with Jinja",
                            message = "test")

@app.route('/<id>/<password>')
def index2(id, password):
    msg = 'id: %s, password: %s' % (id, password)
    return render_template('index.html',
                            title="index with Jinja",
                            message = msg)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
