from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
# werkzeug 툴 사용
from werkzeug.utils import redirect

from pybo import db
# 답변 폼 추가
from pybo.forms import AnswerForm
from pybo.models import Diary, Answer

#  답변 블루프린트 제작
bp = Blueprint('answer', __name__, url_prefix = '/answer')



# form이 POST 방식인 bp.route 애너테이션 (똑같은 폼 형식 필요)
@bp.route('/create/<int:diary_id>', methods=('POST',))
def create(diary_id):
    form = AnswerForm()
    diary = Diary.query.get_or_404(diary_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        diary.answer_set.append(answer)
        db.session.commit()
        return redirect('{}#answer_{}'.format(url_for('diary.detail', diary_id=diary_id), answer.id))
    return render_template('diary/diary_detail.html', diary=diary, form=form)

@bp.route('/modify/<int:answer_id>', methods=('GET','POST'))
# @login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('diary.detail', diary_id=answer.diary.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now() # 수정일자
            db.session.commit()
            return redirect('{}#answer_{}'.format(url_for('diary.detail', diary_id=answer.diary.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)

@bp.route('/delete/<int:answer_id>')
# @login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    diary_id = answer.diary.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('diary.detail', diary_id=diary_id))

@bp.route('/vote/<int:answer_id>/')
# @login_required
def vote(answer_id):
    _answer = Answer.query.get_or_404(answer_id)
    _answer.voter.append(g.user)
    db.session.commit()
    return redirect(url_for('diary.detail', diary_id=_answer.diary.id))

