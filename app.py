# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps
from flask import flash

# create the application object
app = Flask(__name__)
app.secret_key = 'my precious'

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
# use decorators to link the function to a url
@app.route('/')
def home():
     return render_template('index.html')  # render a template
     
@app.route('/about')
def about():
     return render_template('about.html')  # render a template


@app.route('/blog')
def blog():
     return render_template('blog.html')  # render a template

@app.route('/contact')
def contact():
     return render_template('contact.html')  # render a template

@app.route('/travel_destination')
def travel_destination():
     return render_template('travel_destination.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('/'))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
