# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return'Hello World'

# @app.route('/abhi')
# def index1():
#     number1 = request.args.get('number1')
#     number2 = request.args.get('number2')
#     return f'Hello {number1} your age is {number2}'

# @app.route('/aman')
# def index2():
#     number1 = int(request.args.get('number1'))
#     number2 = int(request.args.get('number2'))
#     number3 = number1 + number2
#     return f'Hello the sum of {number1} and {number2} is {number3}'

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, render_template

# app = Flask(__name__,template_folder='template')

# @app.route('/')
# def index():
#     return render_template('index.html', name='Jerry')

# if __name__ == "__main__":
#     app.run(debug=True)



import smtplib
from smtplib import SMTPException

sender = 'kwindominds@gmail.com'
receivers = ['abhi.techindustan@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

this is a test message.
"""

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
smtpObj.login(sender,'Kwindominds1995@')
smtpObj.sendmail(sender, receivers, message)         
print ("Successfully sent email")

