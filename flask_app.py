from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/', methods=['GET'])
def hello():
    """ The @app.route is the one that the browser will use to point
        to the url being used
    """
    return render_template('hello2.html') 


@app.route('/', methods=['GET'])
def hey():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run()
