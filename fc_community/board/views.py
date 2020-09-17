from django.shortcuts import render
from .models import Board 
# Create your views here.
def board_list(request):
    boards = Board.objects.all().order_by('-id') #모든것을 -정렬로 가지고 오겠다 => 최신것을 먼저 가지고 오겠다.
    return render(request, 'board_list.html', {'boards':boards})

