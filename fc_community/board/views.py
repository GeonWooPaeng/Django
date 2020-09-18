from django.shortcuts import render, redirect
from django.core.paginator import Paginator 
from django.http import Http404
from fcuser.models import Fcuser
from tag.models import Tag
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_detail(request, pk):
    # 글 상세보기
    # 예외 처리
    try: 
        board = Board.objects.get(pk=pk)#입력받은 id의 글을 받아온다.
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board':board})

def board_write(request):
    #사용자가 있는지 확인
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        # 로그인한 사용자가 자동으로 글쓰게 하기
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            

            board = Board() 
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save() 

            # 태그 부분
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                if not tag:
                    continue 

               # Tag.objects.get_or_create(name=tag, writer=writer)(조건: tag의 이름,작성자가 모두 같은 경우면 가져오고 아니면 생성을 해라)
               # _tag: 생성된 개체, _: 새로운건지 원래 있던건지 여부
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') #모든것을 -정렬로 가지고 오겠다 => 최신것을 먼저 가지고 오겠다.
    
    # 이전, 다음 버튼 설정
    page = int(request.GET.get('p', 1)) #p라는 형태로 받고 없으면 1
    paginator = Paginator(all_boards, 2) #한 페이지당 2개씩 보여준다.
    
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards':boards})

