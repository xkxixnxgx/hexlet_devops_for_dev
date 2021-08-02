from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User
from webapp.user.decorators import user_required
from webapp.picture.forms import PicturesForm
from webapp.model import db

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/register')
def register():
    title = "Регистрация"
    if current_user.is_authenticated:
        return redirect(url_for('user.login'))
    form = RegistrationForm()
    return render_template('user/register.html', page_title=title, form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('user.register'))


@blueprint.route('/login')
def login():
    title = "Авторизация"
    if current_user.is_authenticated:
        return redirect(url_for('picture.pictures'))
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('picture.pictures'))
        else:
            flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы разлогинились.', 'success')
    return redirect(url_for('picture.pictures'))


@blueprint.route('/user')
@user_required
def user_index():
    if current_user.is_admin:
        return redirect(url_for("picture.pictures"))
    else:
        return redirect(url_for("main.main"))


