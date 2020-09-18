from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,
                                verbose_name='제목')
    contents = models.TextField(verbose_name='내용') #길이 제한 없다
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                                verbose_name='작성자') #db에서의 모델과 연결하는 방법(fcuser의 Fcuser모델과 연결하겠다.)
                                # on_delete=models.CASCADE은 사용자가 탈퇴하면 사용자 글 모두 지우겠다.
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                verbose_name='등록시간')

    
    def __str__(self):
        return self.title 

    class Meta:
        db_table = 'paeng_board'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'