from flask.ext.wtf import form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
# getting data from form
class signIn(Form):
    email = StringField('what is your name?', validators=[Required])
    pwd = StringField('what is your password?', validators=[Required])
    submit = SubmitField('submit')

