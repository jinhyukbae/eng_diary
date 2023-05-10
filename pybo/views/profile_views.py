# 회원수정 기능 구현
from flask import Blueprint, url_for, render_template, flash, request, session, g, redirect
from werkzeug.utils import redirect
from flask_login import login_required, current_user
from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm
from pybo.models import User, Diary
from sqlalchemy import create_engine # 이 코드는 DB에 대기시간을 넣기 위해 사용함
engine = create_engine('sqlite:///pybo.db', pool_pre_ping=True, pool_timeout=20) # 대기 TRUE, 대기시간 20초

bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/My_profile/', methods=('GET', 'POST'))
def My_profile():
    username = g.user.username
    return render_template('profile/My_Profile.html', username=username)


@bp.route('/Account_settings/', methods=('GET', 'POST'))
def Account_settings():
    # 나의 정보 수정 요청 확인
    if request.method == 'POST' and current_user == g.user:
        changed = False  # 변경 여부가 있는지 확인

        # 6개 정보의 변경여부 확인
        username = request.form.get('username')
        nickname = request.form.get('nickname')
        email = request.form.get('email')
        name = request.form.get('name')
        dayofbirth = request.form.get('dayofbirth')
        password = request.form.get('password')

        # 현재 사용자 정보 연동
        user = User.query.get(current_user.id)

        # 아이디 입력 여부 및 유효성 검사
        if username:
            if len(username) < 2:
                flash("아이디는 1자 이상으로 입력해야 합니다.", category="error")
                return redirect(request.url)
            elif username != user.username:
                user.username = username
                db.session.commit()
                g.user.username = username
                changed = True


        # 이메일 입력 여부 및 유효성 검사
        if email:
            if "@" not in email:
                flash("이메일에는 @가 포함되어야 합니다.", category="error")
                return redirect(request.url)
            elif not any(ext in email for ext in [".com", ".net", ".co.kr", ".or.kr", ".go.kr", ".kr"]):
                flash("이메일 주소를 올바른 형식으로 입력해주세요", category="error")
                return redirect(request.url)
            elif email != user.email:
                user.email = email
                db.session.commit()
                g.user.email = email
                changed = True

        # 닉네임 입력 여부 및 유효성 검사
        if nickname:
            if len(nickname) < 1 or len(nickname) > 4:
                flash("닉네임은 1자 이상, 4자 이하로 입력해야 합니다.", category="error")
                return redirect(request.url)
            elif nickname != user.nickname:
                user.nickname = nickname
                db.session.commit()
                g.user.nickname = nickname
                changed = True

        # 이름 입력 여부 및 유효성 검사
        if name:
            if len(name) < 1 or len(name) > 11:
                flash("이름은 1자 이상, 10자 이하로 입력해야 합니다.", category="error")
                return redirect(request.url)
            elif name != user.name:
                user.name = name
                db.session.commit()
                g.user.name = name
                changed = True


        # 생년월일 입력 여부 및 유효성 검사
        if dayofbirth:
            if dayofbirth != user.dayofbirth:
                user.dayofbirth = dayofbirth
                db.session.commit()
                g.user.dayofbirth = dayofbirth
                changed = True

        # 비밀번호 입력 여부 및 유효성 검사
        if password:
            if len(password) < 4 or len(password) > 12:
                flash("비밀번호는 4자 이상, 12자 이하로 입력해야 합니다.", category="error")
                return redirect(request.url)
            elif password != user.password:
                user.password = password
                db.session.commit()
                g.user.password = password
                changed = True

        # 변경사항이 있다면 redirect 함
        if changed:
            flash('정보가 변경되었습니다.', category="primary")
            return redirect(url_for('profile.Account_settings'))
        else:
            flash('변경사항이 없습니다.', category="error")
            db.session.rollback()
            return redirect(request.url)

    return render_template('profile/Account_Settings.html')