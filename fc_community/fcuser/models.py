from django.db import models

# Create your models here.

#모델 만들기 
class Fcuser(models.Model):
    username = models.CharField(max_length=64,
                                    verbose_name='사용자명')
    password = models.CharField(max_length=64,
                                    verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')

    def __str__(self):
        #내가 가지고 있는 username을 반환(db에 보이게)하게 한다.
        return self.username

    #db이름 변경
    class Meta:
        db_table = 'paeng_fcuser'

        #맨 앞에 보이는(주제) 이름 바꾸기
        verbose_name = '장고 공부'
        verbose_name_plural = '장고 공부'