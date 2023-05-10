from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
from flask_login import login_required, current_user

# 게시판 질문 목록 템플릿 준비
from pybo.models import Diary

bp = Blueprint('main', __name__, url_prefix='/')

# 라우팅 함수 매핑
@bp.route('/hellopage')
def hello_pybo():
    return 'Hello0*0, Pyboooo!'

# 블루프린트에 라우팅 함수 추가-인덱스 페이지임
@bp.route('/')
def index():
    # 현재 일기쓰기 프로젝트에 맞게 첫 페이지를 대체 ▼
    return render_template('diary/index.html')
    # url_for 로 질문목록과 상세기능은 대체 ▼ > 리다이렉트 기능 사용
    # return redirect(url_for('diary._list'))
    # diary_list = Diary.query.order_by(Diary.create_date.desc())
    # 템플릿 파일을 화면으로 렌더링
    # return render_template('diary/diary_list.html', diary_list=diary_list)
    # return render_template('diary/answer_list.html', answer_list = answer_list)


# diary_list에서 요청된 url에 대응할 수 있도록 라우팅 함수 추가
@bp.route('/detail/<int:diary_id>/')
def detail(diary_id):
    diary = Diary.query.get_or_404(diary_id)
    return render_template('diary/diary_detail.html', diary=diary)



# notice_list에서 요청된 url에 대응할 수 있도록 라우팅 함수 추가
@bp.route('/notice_list/<int:notice_id>/')
def notice_detail(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    return render_template('diary/notice_detail.html', notice=notice)


