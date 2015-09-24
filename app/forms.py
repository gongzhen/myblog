from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, EqualTo
from wtforms import ValidationError

class LoginForm(Form):
	username = StringField('Username', validators=[Required(), Length(1, 64)])
	password = PasswordField('Password', validators=[Required()])
<<<<<<< HEAD
	remeber_me = BooleanField('remember_me', default=False)
=======
	remeber_me = BooleanField('remeber_me', default=False)
>>>>>>> 63191c73a005cb04086134b607445927951da0d6
	submit = SubmitField('Log In')
	
