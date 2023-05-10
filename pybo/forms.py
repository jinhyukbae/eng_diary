# pybo에 질문 등록시 사용
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 일기 폼 만들기
class DiaryForm(FlaskForm):
    subject = TextAreaField('제목', validators = [DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators = [DataRequired('내용은 필수 입력 항목입니다.')])
    tags = TextAreaField('태그', validators=[DataRequired('태그를 입력해요')])
# 답변 폼 만들기
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])

# 유저 생성 폼 만들기
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    nickname = StringField('닉네임', validators=[DataRequired()])
    name = StringField('이름', validators=[DataRequired()])
    dayofbirth = StringField('생년월일', validators=[DataRequired()])

# 로그인 폼 제작
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

# 공지사항 폼 만들기
class NoticeForm(FlaskForm):
    subject = StringField('제목', validators = [DataRequired()])
    content = TextAreaField('내용', validators = [DataRequired()])