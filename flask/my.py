from flask import Flask

app = Flask(__name__)

@app.route('/myrule')
def myrule():
    return "here only my rule will be followed"


if __name__== "__main__":
    app.run(debug=True)
