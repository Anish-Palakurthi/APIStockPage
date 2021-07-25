from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST, "GET"])
def home():
    return(render_template("stockpage.html"))


if __name__ == "__main__":
    app.run(debug=True)
