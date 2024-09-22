from flask import Flask , render_template 

app = Flask(__name__)

@app.route('/')
def homepage():
    return "null"

@app.route('/home')
def home():
    return  render_template("home.html")


@app.route('/hello')
def greet():
    return "hello from the other side"

@app.route('/word')
def wordfind():
    return "where we find essential  for us"

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)
