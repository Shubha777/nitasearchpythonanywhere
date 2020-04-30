from flask import Flask, request, render_template

from testing import generatohtml

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def my_form():



    return render_template('lag.html')


@app.route('/', methods=['POST'])
def my_form_post():

       variable = request.form["nitasearch"]

       instrumentality=generatohtml(variable)

       return render_template('crap.html')


if __name__ == "__main__":

    app.run(debug=True)
