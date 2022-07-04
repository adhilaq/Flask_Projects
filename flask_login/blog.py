from flask import Flask, flash, redirect, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '957e15de26f2524d099053553c244347'



@app.route("/home/")
def home():
    return render_template("home.html", title="Home")

@app.route("/")
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect('login')

    return render_template('register.html', title='Register', form=form)

@app.route("/login",  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "adhilaq":
            flash(f'Account logged in for {form.username.data}!', 'success')
            return redirect('home')
        else:
            flash(f'Login unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)