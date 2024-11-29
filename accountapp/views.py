from django.shortcuts import render
from django.http import HttpResponse

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

        #HelloWorld.objects.all() # 모두 가져옴

        #return render(request, 'accountapp/hello_world.html', context={'text':temp})
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output':new})#객체 내보냄
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'GET method'})

