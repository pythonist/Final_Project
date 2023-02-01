from flask_wtf import Form 
# from wtforms.fields import StringField,  TextAreaField,SubmitField
from wtforms import StringField, BooleanField, TextAreaField,SubmitField
from wtforms.validators import InputRequired,ValidationError

from wtforms import StringField, BooleanField, TextAreaField

class ContactForm(Form):
  name = StringField("Name",  [InputRequired("Please enter your name.")])
  email = StringField("Email",  [InputRequired("Please enter your email address.")])
  subject = StringField("Subject",  [InputRequired("Please enter a subject.")])
  message = TextAreaField("Message",  [InputRequired("Please enter a message.")])
  submit = SubmitField("Send")
