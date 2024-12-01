from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# Create your views here.
def hello_world(request):
    #return HttpResponse('Hello')
    #return render(request, 'base.html')
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new = HelloWorld() # 모델
        new.text = temp
        new.save() # db에 저장됨

        hello_world_list = HelloWorld.objects.all() # 모두 가져옴

        #return render(request, 'accountapp/hello_world.html', context={'text':temp})
        #return render(request, 'accountapp/hello_world.html', context={'hello_world_output':new})#객체 내보냄
        #return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        #return render(request, 'accountapp/hello_world.html', context={'text':'GET method'})
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})

# 클래스 base view
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 로그인 성공하면 재연결
    # 함수형 뷰 reverse() 클래스형 뷰 reverse_lazy()
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') 
    template_name = 'accountapp/update.html'

class AccountDeleteView(DetailView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

