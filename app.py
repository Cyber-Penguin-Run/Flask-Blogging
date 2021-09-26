from flask import Flask, render_template, url_for, flash, redirect
from flask.helpers import flash
from forms import RegistrationForm, LoginForm
#app variable to set flask to an instance. 
#(__name__) is the name of the module, flask will know where to look for templates and static files#
app = Flask(__name__)
app.config['SECRET_KEY'] = '3b821b898e7d54ea69d477ce20aa666a'

posts = [
    {
        'author': 'Zimin Chen',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 21, 2018'
    }
]



#Root page of the website. Returns text of 'Hello World!'
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #Temp valiation for now to sign into the app.
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect (url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html',title='Login', form=form)



#run the debug environment, need to delete this when putting app into production.
if __name__=='__main__':
    app.run(debug=True)