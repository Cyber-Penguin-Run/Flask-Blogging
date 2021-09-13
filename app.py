from flask import Flask, render_template, url_for
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
    return render_template('register.html',title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Register', form=form)



#run the debug environment, need to delete this when putting app into production.
if __name__=='__main__':
    app.run(debug=True)