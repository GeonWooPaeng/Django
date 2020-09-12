from django.contrib import admin
from .models import Fcuser
# Register your models here.

class FcuserAdmin(admin.ModelAdmin):
    # 필드를 변화시키는 방법
    list_display = ('username','password')

admin.site.register(Fcuser, FcuserAdmin)