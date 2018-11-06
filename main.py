from flask import Flask, request, redirect, render_template
import cgi 
import jinja2
import os 

# TODO:
# If all input is valid, show a welcome page with a message of "Welcome, [username]!"

# TODO: 
# Use templates: index.html and welcome.html to render the page. 

app = Flask(__name__)
app.config['DEBUG'] = True      
# displays runtime errors in the browser, too

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    v_password_error = ''
    email_error = ''

    ####### testing the try/except block ############

# # TODO:
# # Check for errors and reject and render feedback:

    if " " in username or len(username) < 3 or len(username) > 20 or "":
        username_error = "Username cannot have spaces and must be between 3 and 20 characters"
 
   # return render_template("index.html", username=username, username_error=username_error)

    
    if len(password) > 20 or len(password) < 3 or "" or " " in password:
        password_error = 'Password must be between 3 and 20 characters.'
    
    if password != v_password:
        # password must match verified password
        v_password_error = "Passwords must match."
# email must have:
    if email:
        if not ('@'in email):
            email_error = "Email must contain @."

        if len(email) > 20 or len(email) < 3:
            email_error = "Email must be between 3 and 20 characters."

        if not ('.' in email):
            email_error = "Email must contain a . ."

        if ' ' in email:
            email_error = "Email must not contain spaces."
    
    if not username_error and not password_error and not v_password_error and not email_error:
        return render_template("welcome.html", username=username, email=email)
    else:
        # redisplay the form with the error messages.
        return render_template("index.html", username=username, username_error=username_error, password_error=password_error, v_password_error=v_password_error, email_error=email_error)

            # Go ahead and insert 
            # This inserts into the placeholder variable username, password, and #email however if one of the values is invalid, it will still be in #there. If one of the {values} above is valid, it can stay in place #and the user doesn't have to re-enter the valid value and they can #focus on the one that's invalid.
            # Each of those strings must still be empty to pass here
            # So it gets a success! message.


app.run()