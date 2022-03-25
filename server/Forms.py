from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    email = EmailField('', 
                        validators=[InputRequired(), Email(message='Invalid email!'), Length(max=50)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField('', 
                            validators=[InputRequired(), Length(min=6, max=80)],
                            render_kw={"placeholder": "Password"})

class SignUpForm(FlaskForm):
    name = StringField('', 
                        validators=[InputRequired(), Length(min=2, max=50)],
                        render_kw={"placeholder": "Name"})
    email = EmailField('', 
                        validators=[InputRequired(), Email(message='Invalid email!'), Length(max=50)],
                        render_kw={"placeholder": "Email"})
    password = PasswordField('', 
                            validators=[InputRequired(), Length(min=6, max=80)],
                            render_kw={"placeholder": "Password"})

class TrainingForm(FlaskForm):
    file = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'heic'], 'Images only!')
    ])