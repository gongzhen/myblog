from flask.ext.wtf import Form
from wtforms.fields.html5 import URLField
from wtforms.validators import url

from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Required, Length, EqualTo
from wtforms import ValidationError

class LoginForm(Form):
	username = StringField('Username', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('remember_me', default=False)
	submit = SubmitField('Log In')

class EditProfileForm(Form):
	username = StringField('Username', validators=[Length(0, 64)])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role', coerce=int)
	submit = SubmitField('Submit')
	
