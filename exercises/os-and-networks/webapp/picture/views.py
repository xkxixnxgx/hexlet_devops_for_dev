from flask import Blueprint, render_template, url_for, flash, redirect, request
from webapp import db
from webapp.picture.models import Picture
from webapp.comment.models import Comment
from webapp.picture.forms import PicturesForm
from webapp.comment.forms import CommentAddForm
from flask_login import current_user
import os

blueprint = Blueprint('picture', __name__, url_prefix='/picture')


@blueprint.route('/', methods=['GET', 'POST'])
def pictures():
    if current_user.is_authenticated:
        title = "Pictures"
        form = Picture.query.filter(Picture.user_id == current_user.id)
        comment_form = Comment.query.filter(Comment.picture_id == Picture.id)
        return render_template('picture/picture.html', page_title=title, form=form, comment_form=comment_form)
    else:
        flash('Вы не вошли как пользователь. Пожалуйста залогиньтесь.', 'warning')
        return redirect(url_for('user.login'))


@blueprint.route('/picture_add', methods=['GET', 'POST'])
def picture_add():
    if current_user.is_authenticated:
        title = "Picture_add"
        form = PicturesForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.user_email = form.user_email.data
            db.session.commit()
            flash('Your profile has been updated', 'success')
            return redirect(url_for('picture.pictures'))
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.user_email.data = current_user.user_email
        image_file = url_for('static', filename='profile_pics/' + current_user.picture)
        return render_template('picture/picture_add.html', page_title=title, image_file=image_file, form=form)
    else:
        flash('Вы не вошли как пользователь. Пожалуйста залогиньтесь.', 'warning')
        return redirect(url_for('user.login'))


@blueprint.route('/load_picture', methods=['GET', 'POST'])
def load_picture(file_name):
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        directory_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        name = file_name.split('.')[0]
        url = directory_project + '/static/' + file_name
        file_exist = Picture.query.filter(Picture.url == url).count()
        if not file_exist:
            new_picture = Picture(name=name, url=url)
            db.session.add(new_picture)
            db.session.commit()

