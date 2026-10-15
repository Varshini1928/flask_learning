
from flask import Flask, render_template ,url_for


app =Flask(__name__)
app.config['secret_key']='2ef68a4e307f133dbdf45325c96803a9'

@app.route("/")
def home():
    return "<h1><i> Welcome to the home page </i></h1>"

@app.route("/about")
def about():
    return "About"


if __name__ =="__main__":
    app.run(debug=True)
