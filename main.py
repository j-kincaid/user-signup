from flask import Flask, request, redirect, render_template
import cgi


# TODO:
# If all input is valid, show a welcome page with a message of "Welcome, [username]!"

# TODO: 
# Use templates: index.html and welcome.html to render the page. 



app = Flask(__name__)
app.config['DEBUG'] = True      
# displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=['POST'])
def signup():
    password = request.form['password']
    template = jinja_env.get_template('index.html')
    return template.render('index.html')

@app.route('/validate-user')
def signup_form():
    return signup_form.format(username='', username_error='', password='', password_error='', email='', email_error='')

# ####### the try/except block ############
# def is_valid(signup):
#     try: 
#         int(num)
#     except ValueError:
#         return False

@app.route('/validate', methods=['POST'])
def validate_user():
    validated_user = request.form['index.html']

    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']

    ####### testing the try/except block ############

# # TODO:
# # Check for errors and reject and render feedback:

# No empty fields
    for char in username:
        if char == " ":
            username_error = "Username cannot Have Spaces"
            break
        else:
            username_error = ""

    
    for char in password:
        if char == " ":
            password_error = "Password cannot Have Spaces"
            break
        else:
            password_error = ""


    for char in email:
        if char == " ":
            email_error = "Email cannot Have Spaces"
            break
        else:
            email_error = ""
            
# username and password must be >3 and <20 char
    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters"

        ######### 
        if len(password) > 20 or len(password) < 3:
            password_error = 'Password must be between 3 and 20 characters.'
        if password != v_password:
# password must match verified password
            password_error: "Passwords must match."
        else: 
                password_error = ""
# email must have:
#  no spaces
        if " " in email:
            email_error = "Email must not contain spaces."
#  a single @
        if "@ " not in email:
            email_error = "Email must contain @."
#  a single .
        if ". " not in email:
            error = "Email must contain a . ."
# between 20 and 3 characters
        if len(email) > 20 or len(email) < 3:
            error = "Email must be between 3 and 20 characters."
        else: 
            email_error =" "

        if len(username_error)==0 and len(password_error) == 0 and len(email_error) == 0:
            return render_template("welcome.html", username=username, password=password, v_password=v_password, email=email)
        else:
            # redisplay the form with the error messages.
            return render_template("index.html", username=username, username_error=username_error, password_error=password_error, v_password_error=v_password_error, email_error=email_error)
            # Go ahead and insert 
            # This inserts into the placeholder variable username, password, and #email however if one of the values is invalid, it will still be in #there. If one of the {values} above is valid, it can stay in place #and the user doesn't have to re-enter the valid value and they can #focus on the one that's invalid.
            # Each of those strings must still be empty to pass here
            # So it gets a success! message.

@app.route('/welcome')
def welcome():
    return render_template('welcome.html ', username=username)

app.run()