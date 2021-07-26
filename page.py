from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        day = request.form["dt"]

        firstStock = request.form["s1"]

        secondStock = request.form["s2"]

        return redirect(url_for("chart", date=day))
    else:
        return(render_template("base.html"))


@ app.route("/chart")
def chart(date):  # , stock1, stock2):
    date2 = date
    return(date2)
    # return(("{date1}, {s1}, {s2}").format(date1=date2, s1=stock1, s2=stock2))


if __name__ == "__main__":
    app.run(debug=True)
