# 장고에서 기본 제공해주는 form이 없어서 기존에있던 모델을 폼으로 변환시키는 방법을 사용


from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']