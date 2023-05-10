# 회원가입 기능을 위한 블루프린트 구현
from flask import Blueprint, url_for, render_template, flash, request, session, g
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data,
                        nickname=form.nickname.data,
                        name=form.name.data,
                        dayofbirth=form.dayofbirth.data)
            db.session.add(user)
            db.session.commit()

            login_user(user, remember=True)
            return redirect(url_for('auth.login'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            login_user(user, remember=True)
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/logout/')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('main.index'))


from flask import Flask, render_template, request
from flask_dance.contrib.google import make_google_blueprint, google

# ...

# google_bp = make_google_blueprint(client_id="136279422951-4nr61veh2kajbg1tcqaggnc7uqh1hl38.apps.googleusercontent.com",
#                                    client_secret="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",
#                                    scope=["profile", "email"])
# from flask_dance.consumer import OAuth2ConsumerBlueprint
# google_bp = OAuth2ConsumerBlueprint("google", __name__,
#                                         client_id="136279422951-4nr61veh2kajbg1tcqaggnc7uqh1hl38.apps.googleusercontent.com",
#                                         client_secret="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",
#                                         scope=["profile", "email"],
#                                         redirect_uri="http://127.0.0.1:5000/auth/google/login/callback")
#
#
# app = Flask(__name__)
# app.secret_key = "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"
# app.register_blueprint(google_bp, url_prefix="/auth")
#
# @google_bp.route("/google/login/callback")
# def googlelogin():
#     if not google.authorized:
#         return redirect(url_for("google.googlelogin"))
#     resp = google.get("/oauth2/v2/userinfo")
#     assert resp.ok, resp.text
#     email = resp.json()["email"]
#     # 로그인 처리 로직 구현
#     return redirect(url_for("main.index"))
#
# # 구글 로그인
# if __name__ == "__main__":
#     app.run(debug=True)
