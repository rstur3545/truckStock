from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class PartForm(FlaskForm):
    partnumber = StringField('partnumber', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    quantity = IntegerField('quantity')
    description = StringField('description',widget=TextArea())
    submit = SubmitField('Submit')

class QueryForm(FlaskForm):
    partnumber = StringField('partnumber')
    location = StringField('location')
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    idd = IntegerField('ID')
    partnumber = StringField('partnumber', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    quantity = IntegerField('quantity')
    description = StringField('description',widget=TextArea())
    submit = SubmitField('Submit')

class DeleteIdform(FlaskForm):
    idd = IntegerField('ID', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteLocationform(FlaskForm):
    location = StringField('location', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    