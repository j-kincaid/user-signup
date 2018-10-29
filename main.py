from flask import Flask, request, redirect, render_template
import cgi

# TODO: Create a signup form with fields for Username, Password, Verify
# Password, Optional email, and submit button

# # TODO:
# # Check for errors and reject and render feedback:
# No empty fields
# username and password must be >3 and <20 char
# password must match verified password
# email must have:
#  a single @
#  a single .
#  contain no spaces


# TODO:

# Each feedback message must be next to the the field it refers to.

# # TODO:
# Users should only have to enter email once. 
# # TODO:
# Password should be cleared for security reasons.

# TODO:
# If all input is valid, show a welcome page with a message of "Welcome, [username]!"

# TODO: 
# Use templates: index.html and elcome.html to render the page. 

# TODO:
# TODO:

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True      
# displays runtime errors in the browser, too

@app.route("/")
def index():
    return render_template('index.html', username_error, passwd_error, vpasswd_error, email_error)
@app.route("/signup", methods=['POST'])
def signup():
    password = request.form['password']
    template = jinja_env.get_template('password.html')
    return template.render(password=passwd)

@app.route('/validate-user')
def display_signup_form():
    return signup_form.format(username='', username_error='', passwd='', passwd_error='', email='', email_error='')

# ####### the try/except block ############
# def is_valid(signup):
#     try: 
#         int(num)
#     except ValueError:
#         return False

@app.route('/validate-user', methods=['POST'])
def validate_():

    username = request.form['username']
    passwd = request.form['password']
    email = request.form['email']

    name_error =''
    passwd_error =''
    email_error =''

####### testing the try/except block ############
if len(username) < 3 or len(username) > 20:
    username_error = "Must be between 3 and 20 characters"

for char in username:
    if char == " ":
        username_error = "Cannot Have Spaces"
        break
    else:
        username_error = ""

    ######### 
    if len(password) <= 0:
        input_error = 'Please complete all fields.'
    else: 
        if passwd != vpasswd:
            passwd_error = 'Passwords must match.'
        else: 
            username = int(username)
            passwd = int(passwd)
            if username > 20 or username < 3:
                name_error = 'Username and password must be between 3 and 20 characters.'
            if passwd > 20 or passwd < 3:
                    passwd_error = 'Username and password must be between 3 and 20 characters.'

        if not name_error and not passwd_error and not email_error:
        # redisplay the form with the error messages.
        # Go ahead and insert 
            return signup_form.format(name_error=name_error, passwd_error=passwd_error, email_error=email_error, username=username, passwd=passwd, email=email)
            # This inserts into the placeholder variable username, password, and #email however if one of the values is invalid, it will still be in #there. If one of the {values} above is valid, it can stay in place #and the user doesn't have to re-enter the valid value and they can #focus on the one that's invalid.
                # Each of those strings must still be empty to pass here
                # So it gets a success! message.
        else:
            return 'Success!'
        


app.run()