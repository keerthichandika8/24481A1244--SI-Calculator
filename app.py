from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Flaskapp<=>routing"


@app.route('/greet/<uname>')
def greet(uname):
    return f"Good morning, {uname}!"


@app.route('/calculate', methods=['GET', 'POST'])
def SI():
    result = None
    total = None
    P = None
    R = None
    T = None

    if request.method == "POST":
        P = float(request.form['p'])
        R = float(request.form['r'])
        T = float(request.form['t'])

        result = (P * R * T) / 100
        total = P + result

    return render_template(
        'index.html',
        result=result,
        total=total,
        p=P,
        r=R,
        t=T
    )


if __name__ == "__main__":
    app.run(debug=True, port=3500)