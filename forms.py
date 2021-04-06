from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    dob = StringField('Date Of Birth', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators = [DataRequired()])
    parentName = StringField('Guardian Name', validators = [DataRequired()])
    parentPhone = StringField('Guardian Phone Number', validators = [DataRequired()])
    course = StringField('Course')
    submit = SubmitField('Register')

class AddCourse(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Course')

class WaecRegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    dob = StringField('Date Of Birth', validators=[DataRequired()])
    prevSchool = StringField('Previous School Attended', validators=[DataRequired()])
    completed = StringField('Year Completed', validators=[DataRequired()])
    # Courses
    course1 = StringField('Course 1', validators=[DataRequired()])
    grade1 = StringField('Grade', validators=[DataRequired()])
    course2 = StringField('Course 2', validators=[DataRequired()])
    grade2 = StringField('Grade', validators=[DataRequired()])
    course3 = StringField('Course 3', validators=[DataRequired()])
    grade3 = StringField('Grade', validators=[DataRequired()])
    course4 = StringField('Course 4', validators=[DataRequired()])
    grade4 = StringField('Grade', validators=[DataRequired()])
    course5 = StringField('Course 5', validators=[DataRequired()])
    grade5 = StringField('Grade', validators=[DataRequired()])
    course6 = StringField('Course 6', validators=[DataRequired()])
    grade6 = StringField('Grade', validators=[DataRequired()])
    # End 
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators = [DataRequired()])
    parentName = StringField('Guardian Name', validators = [DataRequired()])
    parentPhone = StringField('Guardian Phone Number', validators = [DataRequired()])
    course = StringField('Course')
    picture = FileField('Add a picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Register')

class NursingRegistrationForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    otherNames = StringField('Other Names', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    dateOfBirth = StringField('Date Of Birth', validators=[DataRequired()])
    placeOfBirth = StringField('Place Of Birth', validators=[DataRequired()])
    telephone = StringField('Telephone Number', validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    district = StringField('District', validators=[DataRequired()])
    country = StringField('Date Of Birth', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    languages = StringField('Languages', validators=[DataRequired()])
    medicalCondition = StringField('Medical Conditions ', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    regionDistrict = StringField('Region District', validators=[DataRequired()])
    digitalAddress = StringField('Digital Address', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    # Guardian Information
    guardianName = StringField('Name Of Guardian', validators=[DataRequired()])
    phoneNumber = StringField('Phone Number', validators=[DataRequired()])
    guardianAddress = StringField('Guardian Address', validators=[DataRequired()])
    # Academic Details
    dateOfBirth = StringField('Date Of Birth', validators=[DataRequired()])
    indexNo = StringField('Index Number', validators=[DataRequired()])
    examsYear = StringField('Exams Year', validators=[DataRequired()])
    waecCourse = StringField('Waec Course', validators=[DataRequired()])
    # Subjects and courses!!!
    submit = SubmitField('Register')
    






    
