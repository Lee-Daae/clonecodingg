from django.urls import path
from profileapp.views import ProfileCreateView, ProfileUpdateView


app_name = "profileapp"

urlpatterns = [
    #path('hello_world/', hello_world, name='hello_world'),

    #path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]