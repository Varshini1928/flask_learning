from flask import Flask ,request

app=Flask(__name__)
app.config["SECRET_KEY"]='change-me'

@app.route("/")
def home():
    return "<h1>Home Page</h1><a href='/login'>Go to login</a>"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST" :
        return "Submit the form"
    
    return "Show the form"


if __name__=="__main__":
    app.run(debug=True)
