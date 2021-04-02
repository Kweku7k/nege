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
    picture = FileField('Add a picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Register')