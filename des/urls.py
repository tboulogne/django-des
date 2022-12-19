# -*- coding: utf-8 -*-
from django.urls import re_path
from des import views


urlpatterns = [
    re_path(r'^send-test-email', views.send_test_email, name = 'des-test-email'),
]

__all__ = ['urlpatterns']
