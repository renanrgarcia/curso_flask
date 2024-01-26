from flask import Flask

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<nome>')
def hello(nome=''):
    return '<h1>Hello {}</h1>'.format(nome)


@app.route('/blog/')
@app.route('/blog/<int:postID>')
def blog(postID=-1):
    if postID >= 0:
        return f'blog info {postID}'
    else:
        return 'Blog todo'


@app.route('/blog/<float:postID>')
def blogFloat(postID=-1):
    if postID >= 0:
        return f'blog float info {postID}'
    else:
        return 'Blog float todo'


if __name__ == '__main__':
    app.run(debug=True)
