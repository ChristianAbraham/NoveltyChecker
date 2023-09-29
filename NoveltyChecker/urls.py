from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),
    path("report/", views.report, name="report"),
    path("search-result/", views.searchResult, name="searchResult"),
    path("search/", views.search, name="search"),
]