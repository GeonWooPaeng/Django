from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm
# Create your views here.

def home(request):
    #로그인 기능
    user_id = request.session.get('user') # session에서 user정보 가져오기 
    if user_id:
        #로그인 했을 시
        fcuser = Fcuser.objects.get(pk=user_id) 
        return HttpResponse(fcuser.username)

    return HttpResponse('Home!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')


def login(request):
    #로그인 기능
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)

    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '값을 모두 입력해주세요'
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             # 등록된 것과 비밀번호 일치 여부, 로그인 처리 
    #             # 세션 관리
    #             request.session['user'] = fcuser.id
    #             # 홈으로 가야된다.
    #             return redirect('/')
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'

    #     return render(request, 'login.html', res_data)

    # 로그인 form
    if request.method == 'POST':
        form = LoginForm(request.POST) #form에 post 데이터를 넣어준다.
        if form.is_valid(): #form이 정상인지 확인
            #세션 코드(session)
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm() 
    return render(request, 'login.html', {'form': form})


def register(request):
    # register.html사이트에서 입력한 값으로 django adminstration(db)에 저장하기 
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        #html에서의 name값으로 정보전달
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail',None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # if password != re_password:
        # 다른 홈페이지에서 발생
        #     return HttpResponse('비밀번호가 다릅니다.')

        #render함수에 값 전달하기
        #같은 홈페이지에서 발생
        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        
        elif password != re_password:
            #비밀번호랑 비밀번호 확인이 다를 경우
            res_data['error'] = '비밀번호가 다릅니다.'

        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password) #비밀번호 암호화된 상태로 들어간다.
            )

            fcuser.save()
        return render(request, 'register.html', res_data)
