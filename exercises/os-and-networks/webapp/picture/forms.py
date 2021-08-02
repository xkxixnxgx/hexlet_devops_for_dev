from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class PicturesForm(FlaskForm):
    name = StringField('Название изображения', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Загрузить', render_kw={"class": "btn btn-primary"})


class Picture_addForm(FlaskForm):
    name = StringField('Название изображения', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Загрузить', render_kw={"class": "btn btn-primary"})