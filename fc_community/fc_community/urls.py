"""fc_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


# admin 하위에 있는 것은 다 admin.site.urls로 연결하겠다.
# => 주소 뒤에다 admin을 붙이면 장고의 관리자 도구를 사용할 수 있다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fcuser/', include('fcuser.urls'))
    
]
