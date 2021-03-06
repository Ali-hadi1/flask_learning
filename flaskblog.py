from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1caae790185db9529f000ce7b22d83ab'

posts = [
    {
        'author':'Ali',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'april 20 2020'
    },
    {
        'author':'hadi',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'april 20 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts= posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form =form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form =form)


if __name__=='__main__':
    app.run(debug=True)  