import profile
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_owner_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world')
    #success_url = reverse_lazy('accountapp:detail') pk가 없어서 안됨 대신 아래 방법
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
    
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False) # 임시로 폼에서 불러온 데이터 저장
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

@method_decorator(profile_owner_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    #success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
    