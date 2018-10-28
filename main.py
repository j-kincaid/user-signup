from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    template = jinja_env.get_template('signup_form.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['password']
    template = jinja_env.get_template('password.html')
    return template.render(name=passwd)

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

    # if not is_integer(minutes):
    #     minutes_error = 'Not a valid integer'
    # else:
    #     minutes= int(minutes)
    #     if minutes > 59 or minutes < 0:
                

app.run()