from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Fcuser
# Create your views here.

def register(request):
    # register.html사이트에서 입력한 값으로 django adminstration(db)에 저장하기 
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        #html에서의 name값으로 정보전달
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # if password != re_password:
        # 다른 홈페이지에서 발생
        #     return HttpResponse('비밀번호가 다릅니다.')

        #render함수에 값 전달하기
        #같은 홈페이지에서 발생
        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        
        elif password != re_password:
            #비밀번호랑 비밀번호 확인이 다를 경우
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password) #비밀번호 암호화된 상태로 들어간다.
            )

            fcuser.save()
        return render(request, 'register.html', res_data)