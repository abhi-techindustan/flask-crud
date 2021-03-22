# # from flask import Flask
# # from flask import request

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return 'Hello World'

# # @app.route('/aman')
# # def index1():
# #     return 'Hello Aman'

# # @app.route('/abhi')
# # def index2():
# #     return 'Hello Abhi how are you'

# # @app.route('/kuldeep')
# # def index3():
# #     number1 =  request.args.get('number1')
# #     number2 =  request.args.get('number2')
# #     number3 = number1 + number2
# #     return f'The sum of {number1} and {number2} is {number3}'

# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, request, render_template
# import mysql.connector

# mydb=mysql.connector.connect(
#     host="localhost",
#     user="abhi",
#     password="aman",
#     database="aman"
# )
# mycursor=mydb.cursor()

# app = Flask(__name__,template_folder='template')
# @app.route('/', methods = ['POST', 'GET'])
# def index():
#     print(request.method)
#     if request.method=="POST":
#         sql = "insert into form(name, age) values(%s, %s)"
#         name = request.form.get('name')
#         age = request.form.get('age')
#         val = (name, age)
#         print(name)
#         print(age)
#         mycursor.execute(sql, val)
#         mydb.commit()

#         mycursor.execute("select * from form")
#         myresult = mycursor.fetchall()
#         print(myresult)
#         mydb.close()
#     return render_template('index.html')

# @app.route('/aman')
# def index1():
#     mycursor.execute("select * from form")
#     myresult = mycursor.fetchall()
#     print(myresult)
#     return render_template('index1.html', Data=myresult)
#     return str(myresult)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask
# # from forms import ContactForm
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.debug = True
# # app.config['SECRET_KEY'] = 'a really really really really long secret key'

# # manager = Manager(app)
# db = SQLAlchemy(app)

from flask import Flask, render_template, request , make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import re 
import smtplib
from smtplib import SMTPException


app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://abhi:aman@localhost/abhi'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), default = 'asdasd')
    password= db.Column(db.String(120), nullable=True)
    otp= db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(120), nullable = True)
    age = db.Column(db.String(120), nullable= True)
db.create_all()

@app.route('/signup', methods = ['POST'])
def signUp():
    email = request.json.get('email')
    password = request.json.get('password')
    if(re.search(regex,email)):
        user = Signup(
            email = email,
            password = password
        )
        db.session.add(user)
        db.session.commit()
        return 'User created successfully!'
    else:
        return 'please enter a valid email'
# if __name__ == "__main__":
#     app.run(debug=True)

@app.route('/signin', methods = ['POST'])
def signin():
    email = request.json.get('email')
    password = request.json.get('password')
    print(Signup.query.all())
    res = Signup.query.filter_by(email=email).first()
    print(res)
    if res and res.password == password:
        return make_response({"message": "You are logged in "})
    else:
        return make_response({"message": "Invalid Credentials  "})

@app.route('/change_pass', methods = ['PUT'])
def change_pass():
    email = request.json.get('email')
    oldpassword = request.json.get('oldpassword')
    newpassword = request.json.get('newpassword')
    print(Signup.query.all())
    res = Signup.query.filter_by(email=email).first()
    print(res)
    if res and res.password == oldpassword:
        Signup.query.filter_by(email=email).update({'password':newpassword})
        res.password = newpassword
        setattr(res, 'password', newpassword)
        db.session.commit()
        return make_response({"message": "password changed "}) 
    else:
        return make_response({"message": "Invalid password "})

@app.route('/otp_generator')
def otp_generator():
    email = request.args.get('email')
    otp = random.randint(1000,9999)
    res = Signup.query.filter_by(email=email).first()
    res.otp = otp
    db.session.commit()
    sender = 'kwindominds@gmail.com'
    receivers = ['abhi@gmail.com']
    message = f"""
    Subject: OTP to Reset password
    
    Your otp is {otp}.
    """

    smtpObj = smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.starttls()
    smtpObj.login(sender,'Kwindominds1995@')
    smtpObj.sendmail(sender, receivers, message) 
    return make_response({"message": "otp sent successfully"})

@app.route('/forgot_pass', methods = ['PUT'])
def forgot_pass():
    email = request.json.get('email')
    otp = request.json.get('otp')
    newpassword = request.json.get('newpassword')
    res = Signup.query.filter_by(email=email).first()
    print(res.otp)
    if res and res.otp == otp:
        Signup.query.filter_by(email=email).update({'password':newpassword})
        db.session.commit()
        return make_response({"message": "password changed "}) 
    else:
        return make_response({"message": "Invalid password "})

@app.route('/edit_profile', methods = ['PUT']) 
def edit_profile():
    email = request.json.get('email')
    name = request.json.get('name')
    age = request.json.get('age')
    print(Signup.query.all())
    res = Signup.query.filter_by(email=email).first()
    print(res)
    if res:
        Signup.query.filter_by(email=email).update({'name':name})
        Signup.query.filter_by(email=email).update({'age':age})
        db.session.commit()
        return make_response({"message": "Profile updated"})
    else:
        return make_response({"message": "email does not exist"})
        