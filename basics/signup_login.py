from flask import Flask, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-me"

@app.route("/")
def home():
    return """
        <h1>Home Page</h1>
        <a href='/signup'>Sign up</a> | <a href='/login'>Login</a>
    """
    
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email_id = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")


        if not username or not email_id or not password or not confirm_password:
            return "Enter all the fields"
        if "@" not in email_id:
            return "Enter the correct email id"
        if len(password) < 8 or " " in password:
            return "Password must have at least 8 characters and no spaces"
        if password != confirm_password:
            return "Confirm password is different from your original password"
        return f"Welcome, {username}"

    return """
        <form method="POST">
            <input type="text" name="username" placeholder="Username">
            <br>
            <input type="text" name="email" placeholder="Email">
            <br>
            <input type="password" name="password" placeholder="Password">
            <br>
            <input type="password" name="confirm_password" placeholder="Confirm Password">
            <br>
            <button type="submit">Sign up</button>
        </form>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password :
           return "Fill the both fields"
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
