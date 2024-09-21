from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "welcome to flask"

@app.route('/bye')

def bye():
    return "bye for today we will be back tomorrow" 
@app.route('/hello')
def greet():
    return "hello from the other side"

@app.route('word')
def wordfind():
    return "where we find essential vocavularry for us"

if __name__=="__main__":
    app.run(debug=True)
