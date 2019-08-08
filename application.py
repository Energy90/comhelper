from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import SignUpForm, LogInForm 

# configure application
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.secret_key = 'e54f2db73b00d08570fe221a8dca0a08'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    form = LogInForm()
    return render_template("login.html", title='Login', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template("signup.html", title='Signup', form=form)


if __name__ == '__main__':
    app.run(debug = True)
