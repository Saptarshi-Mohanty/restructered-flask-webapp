from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class SearchPage(FlaskForm):
    first_name = StringField(name='First name', validators=[DataRequired(), Length(min=2, max=15)])
    submitbutton = SubmitField(name='Search')
    dropdown = SelectField(u'Filter by :-', choices=[('None', 'Default view'),('sbn', 'Sort by name'), ('sbr', 'Sort by rating')])