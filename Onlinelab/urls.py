"""Onlinelab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from Onlinelab.Views import  test_view



urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'', TemplateView.as_view(template_name="index.html")),

    # 提交打分表格
    # path('admin/', admin.site.urls),

    url(r'^login', test_view.login),
    url(r'^get_info', test_view.userinfo),

    url(r'^message/count', test_view.message_count),
    url(r'^save_error_logger', test_view.save_error_logger),
    url(r'^post_score_table', test_view.post_score_table),
    url(r'^get_score_table', test_view.get_score_table),
    # test


    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
