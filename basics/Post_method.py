from flask import Flask, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-me"

@app.route("/")
def home():
    return "<h1>Home Page</h1><a href='/login'>Go to login</a>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return f"Welcome, {username}"

    return """
        <form method="POST">
            <input type="text" name="username" placeholder="Username">
            <br>
            <input type="text" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
