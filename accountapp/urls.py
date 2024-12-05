from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
from articleapp.views import ArticleListView

app_name = "accountapp"

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    #path('hello_world/', hello_world, name='hello_world'), 기본 페이지를 위에거로 수정해서 주석처리

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # 몇번 유저의 객체에 접근할것인지
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]