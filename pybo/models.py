from pybo import db


# 추천 기능 - 따로 테이블 생성
diary_voter = db.Table(
    'diary_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('diary_id', db.Integer, db.ForeignKey('diary.id', ondelete='CASCADE'), primary_key=True)
)


# 리비전 파일이 자동으로 업그레이드
class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date= db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'), nullable=True)
    user = db.relationship('User', backref = db.backref('diary_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    tags = db.Column(db.String(400), nullable=True)
    voter = db.relationship('User', secondary=diary_voter, backref=db.backref('diary_voter_set')) # 추천인
    vote_count = db.Column(db.Integer, default=0, nullable=True)



answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    diary_id = db.Column(db.Integer, db.ForeignKey('diary.id', ondelete='CASCADE'))
    diary = db.relationship('Diary', backref = db.backref('answer_set', cascade = 'all, delete-orphan'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(10), unique=True, nullable = False)
    password = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    dayofbirth = db.Column(db.String(8), nullable=False)
    is_active = db.Column(db.Boolean(), default=True) # is_active 속성
    def get_id(self): # get_id 오류 해결용
        return str(self.id)


# 공지사항
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
