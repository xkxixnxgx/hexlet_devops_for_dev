from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from webapp.comment.forms import CommentAddForm
from webapp.comment.models import Comment
from webapp import db
from datetime import datetime

blueprint = Blueprint('comment', __name__, url_prefix='/comment')


@blueprint.route('/')
@blueprint.route('/<int:id_picture>', methods=['GET', 'POST'])
def comment_add(id_picture):
    title = 'Comment_add'
    if current_user.is_authenticated:
        comment_form = CommentAddForm()
        return render_template('comment/comment_add.html', id_picture=id_picture, title=title, form=comment_form)
    return redirect(url_for('user.login'))


@blueprint.route('/process_comment_add/')
@blueprint.route('/process_comment_add/<id_picture>', methods=['GET', 'POST'])
def process_comment_add(id_picture):
    form = CommentAddForm()
    if current_user.is_authenticated:
        picture_id = id_picture
        # comment = form.comment.data
        comment = 'Пока не работает ;)'
        new_comment = Comment(picture_id=picture_id, comment=comment)
        db.session.add(new_comment)
        db.session.commit()
        flash('Комментарий успешно добавлен.')
        return redirect(url_for('picture.pictures'))
    else:
        flash('Вы не авторизованы. Пожалуйста залогиньтесь.')
        return redirect(url_for('user.login'))




