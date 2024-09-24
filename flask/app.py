from flask import Flask , render_template ,request

app = Flask(__name__)

@app.route('/')
def homepage():
    return "null"

@app.route('/home')
def home():
    name = "noman"
    age = 26
    livein = "feni"
    return  render_template("home.html", name=name,age=age,livein=livein)


@app.route('/hello')
def greet():
    return "hello from the other side"

@app.route('/word')
def wordfind():
    return "where we find essential  for us"

@app.route('/contact',methods=["GET","POST"])
def contact():
    if request.method == "POST":
        form_data = request.form
        name = form_data.get("name")
        email = form_data.get("email")
        text = form_data.get("text")
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)
