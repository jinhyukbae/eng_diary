from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import MetaData
import config
from flaskext.markdown import Markdown

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": 'uq_%(table_name)s_%(column_0_name)s',
    "ck": 'ck_%(table_name)s_%(column_0_name)s_%',
    "fk": 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    "pk": 'pk_%(table_name)s'
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)  # flask 뷰 기본
    
    # ORM을 적용하기 위해서 SQLite와 SQLAlchemy 사용
    app.config.from_object(config)


    #  ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트로 라우팅함수 관리함
    from .views import main_views, diary_views, answer_views, auth_views, query, notice_views, tts, grammar, tag, profile_views
    app.register_blueprint(main_views.bp)
    # 블루프린트에 diary_views도 적용
    app.register_blueprint(diary_views.bp)
    # 답변 기능을 위한 블루프린트 등록
    app.register_blueprint(answer_views.bp)
    # 회원가입 기능을 위한 블루프린트 등록
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(notice_views.bp)
    app.register_blueprint(tts.bp)
    app.register_blueprint(grammar.grammar)
    app.register_blueprint(profile_views.bp)
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown(엔터키를 쳐야 하는 상황)
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    # 구글 소셜 로그인
    from flask_dance.contrib.google import make_google_blueprint, google

    google_bp = make_google_blueprint(
        client_id="136279422951-4nr61veh2kajbg1tcqaggnc7uqh1hl38.apps.googleusercontent.com",
        client_secret="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",
        scope=["profile", "email"],
        offline=True,
        redirect_to="google.login",
    )
    app.register_blueprint(google_bp, url_prefix="/login")

    from .models import User
    # flask-login 적용
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id) # primary key

    return app

