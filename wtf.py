from wtforms import EmailField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class Com(FlaskForm):
    email = EmailField('Email',validators=[DataRequired()])
    text = TextAreaField('Comments',validators=[DataRequired()])
    submit = SubmitField('Send')