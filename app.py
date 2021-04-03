from flask import Flask,redirect,url_for,render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, WaecRegistrationForm, AddCourse
import urllib.request, urllib.parse
import urllib
from flask_migrate import Migrate
import os
import secrets
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
# from models import *

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def __repr__(self):
        return f"Course('{self.id}', '{self.name}')"

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    parentname = db.Column(db.String, nullable=True)
    parentphone = db.Column(db.String, nullable=True)
    course = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Student('{self.id}', '{self.name}')"

class WaecRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    prevSchool = db.Column(db.String, nullable=False)
    completed = db.Column(db.String, nullable=False)
    # Courses
    course1 = db.Column(db.String, nullable=False)
    grade1 = db.Column(db.String, nullable=False)
    course2 = db.Column(db.String, nullable=False)
    grade2 = db.Column(db.String, nullable=False)
    course3 = db.Column(db.String, nullable=False)
    grade3 = db.Column(db.String, nullable=False)
    course4 = db.Column(db.String, nullable=False)
    grade4 = db.Column(db.String, nullable=False)
    course5 = db.Column(db.String, nullable=False)
    grade5 = db.Column(db.String, nullable=False)
    course6 = db.Column(db.String, nullable=False)
    grade6 = db.Column(db.String, nullable=False)
    # End
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    parentname = db.Column(db.String, nullable=True)
    parentphone = db.Column(db.String, nullable=True)
    course = db.Column(db.String, nullable=False)
    image_file = db.Column(db.String(200), default='default.png')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Student('{self.id}', '{self.name}')"


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    print(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    print ("The picture name is" + picture_fn)

    return picture_fn


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

def send_sms(api_key,phone,message,sender_id):
    params = {"key":api_key,"to":phone,"msg":message,"sender_id":sender_id}
    url = 'https://apps.mnotify.net/smsapi?'+ urllib.parse.urlencode(params)
    content = urllib.request.urlopen(url).read()
    print (content)
    print (url)

@app.route('/form/<string:course>', methods=['GET','POST'])
def form(course):
    form = RegistrationForm()
    if form.validate_on_submit():
        print(course)
        registration = Registration(name=form.name.data, dob=form.dob.data, email=form.email.data, phone=form.phone.data, parentname=form.parentName.data, parentphone=form.parentPhone.data, course=course)
        db.session.add(registration)
        db.session.commit()
        print('Form has validated successfully')
        flash(f'Your registration was successful. Please check your messages ', 'success')
        api_key = "jwqJEAkDUyxdK9ltLsIz2E0kH" #Remember to put your own API Key here
        phone = "‭0550701304‬" #SMS recepient"s phone number
        message = "You have recieved from Neges Educational Consult. Please check your dashboard for more information ."
        sender_id = "negesEduCon" #11 Characters maximum
        send_sms(api_key,"0550701304",message,sender_id)
        rec_message ="Thank you for registering to Neges Educational Consult. If you have any difficult, you can reach us on ‭+233550701304‬"
        send_sms(api_key,form.phone.data,rec_message,sender_id)
        return redirect(url_for('home'))
    return render_template('register.html', form=form )

@app.route('/registrations')
def registrations():
    students = Registration.query.all()
    print(students)
    return render_template('registrations.html', students=students)

@app.route('/dashboard')
def dashboard():
    course = Courses.query.all()
    waec = WaecRegistration.query.all()
    registration = Registration.query.all()
    total_course = len(course)
    total_waec = len(waec)
    total_registration = len(registration)
    return render_template('dashboard.html', course = total_course, registration=total_registration, waec=total_waec)

@app.route('/student/<int:id>')
def student(id):
    student=Registration.query.filter_by(id=id).first()
    return render_template("student.html", student=student)

@app.route('/waec', methods=['POST','GET'])
def waecregistration():
    form = WaecRegistrationForm()
    if form.validate_on_submit():
        pic = 'default.png'
        if form.picture.data:
            print('YO!!!!!!!!! IT IS OVER HERE!!!')
            pic= save_picture(form.picture.data)
        waecregistration = WaecRegistration(name=form.name.data, dob=form.dob.data, prevSchool=form.prevSchool.data, completed=form.completed.data, course1=form.course1.data, grade1=form.grade1.data, 
        course2=form.course2.data, grade2=form.grade2.data, 
        course3=form.course1.data, grade3=form.grade3.data, 
        course4=form.course4.data, grade4=form.grade4.data,
        course5=form.course5.data, grade5=form.grade5.data,
        course6=form.course6.data, grade6=form.grade6.data,
        email=form.email.data, phone=form.phone.data, parentname=form.parentName.data, parentphone=form.parentPhone.data, course="form.course.data", image_file=pic)
        db.session.add(waecregistration)
        db.session.commit()
        api_key = "jwqJEAkDUyxdK9ltLsIz2E0kH" #Remember to put your own API Key here
        phone = "‭0550701304‬" #SMS recepient"s phone number
        message = "You have recieved from a new waec application from Neges Educational Consult. Please check your dashboard for more information ."
        sender_id = "negesEduCon" #11 Characters maximum
        send_sms(api_key,"0550701304",message,sender_id)
        rec_message ="Thank you for registering to Neges Educational Consult. If you have any difficult, you can reach us on ‭+233550701304‬"
        send_sms(api_key,form.phone.data,rec_message,sender_id)
        print('Form Submitted Successfully')
        flash(f'Your registration was successful. Please check your messages ', 'success')
        return redirect(url_for('home'))
    return render_template('waecregistration.html', form=form)

@app.route("/waecstudents")
def waecstudents():
    students = WaecRegistration.query.all()
    print(students)
    return render_template('waecstudents.html', students=students)

@app.route("/waecstudent/<int:id>")
def waecstudent(id):
    student = WaecRegistration.query.filter_by().first()
    print(student)
    return render_template("waecstudent.html", student=student)

@app.route("/addcourse", methods=['POST','GET'])
def addcourse():
    form = AddCourse()
    if form.validate_on_submit():
        print('Form has validated successfully')
        course = Courses(name=form.name.data, description=form.description.data)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses'))
    return render_template('addcourse.html', form=form)

@app.route("/courses")
def courses():
    courses = Courses.query.all()
    return render_template('courses.html',courses=courses) 


@app.route("/delete/<int:id>")
def delete(id):
    course = Courses.query.filter_by(id=id).first()
    db.session.delete(course)
    db.session.commit()
    print(course)
    return redirect(url_for('courses'))

@app.route("/viewcourse/<string:course>")
def viewcourse(course):
    print(course)
    # course = Courses.query.filter_by(name = course).all()
    # print(course)
    students = Registration.query.filter_by(course = course).all()
    return render_template("viewcourse.html", students=students, course=course)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)