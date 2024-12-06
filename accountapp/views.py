from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_owner_required
from accountapp.forms import AccountUpdateForm

from articleapp.models import Article

# 클래스 base view
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home') # 로그인 성공하면 재연결
    # 함수형 뷰 reverse() 클래스형 뷰 reverse_lazy()
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(login_required, name='dispatch')
@method_decorator(account_owner_required, name='dispatch')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home') 
    template_name = 'accountapp/update.html'

@method_decorator(login_required, name='dispatch')
@method_decorator(account_owner_required, name='dispatch')
class AccountDeleteView(DetailView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
