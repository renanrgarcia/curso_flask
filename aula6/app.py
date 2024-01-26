# Aula 06 - Métodos HTTP

from flask import Flask

app = Flask(__name__, static_folder='static')


@app.route('/add')
def add():
    return 'Ok'


if __name__ == '__main__':
    app.run(debug=True)
