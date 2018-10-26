from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Signup</h1>
    <form method='POST>
        <label>Username 
            <input name="username" type = "text" value = '{username}' />
        </label>
        <p class="error">{username_error}</p>
        <label>Password
            <input name="passwd" type="password" value='{passwd}' />
        </label>
        <p class="error">{passwd_error}</p>
        <label>Email (optional) 
            <input name="email" type = "text" value = '{email}' />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Validate" />
    </form>
"""

@app.route('/validate-user')
def display_signup_form():
    return signup_form.format(username='', username_error='', passwd='', passwd_error='', email='', email_error='')

####### the try/except block ############
def is_integer(num):
    try: 
        int(num)
    except ValueError:
        return False

@app.route('/validate-user', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error =''
    minutes_error =''

####### testing the try/except block ############

######### 
    if len() is_integer(hours):
        hours_error = 'Not a valid integer'
    else: 
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range'

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
    else:
        minutes= int(minutes)
        if minutes > 59 or minutes < 0:
            



app.run()