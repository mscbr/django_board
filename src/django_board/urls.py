"""django_board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path  # regexp path

from .views import (
    home_page,
    about_page,
    contact_page,
    example_page,
)
from board.views import (
    board_post_detail_page
)

urlpatterns = [
    path('', home_page),
    re_path(r'^about/$', about_page),
    path('board/<str:slug>/', board_post_detail_page),
    #re_path(r'^blog/(?P<post_id>\w+)/$', board_post_detail_page),
    path('example/', example_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
