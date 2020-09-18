from django import forms 
from .models import Fcuser 
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        },
        max_length=32, label="사용자 이름")

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호")

    #비밀번호가 일치하는지 확인
    def clean(self):
        cleaned_data = super().clean() 
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password: #값이 들어 있을때 
            #예외처리
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '아이디가 없습니다.')
                return 
                
            if not check_password(password, fcuser.password):
                # 검증
                self.add_error('password', '비밀번호를 틀렸습니다.') #특정 field에 error를 넣는 함수
            
            else:
                #id를 views.py에 보내주기
                self.user_id = fcuser.id



