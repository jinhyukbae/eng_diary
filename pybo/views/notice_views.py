from flask import Blueprint, render_template
from pybo.models import Notice

bp = Blueprint('notice', __name__, url_prefix='/')

@bp.route('/notice_list/')
def noticelist():
    notice_list = Notice.query.order_by(Notice.id.desc())
    return render_template('diary/notice_list.html', notice_list=notice_list)

@bp.route('/notice_list/<int:notice_id>/')
def notice_detail(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    return render_template('diary/notice_detail.html', notice=notice)