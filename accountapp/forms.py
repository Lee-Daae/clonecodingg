
from django.contrib.auth.forms import UserCreationForm

# 상속받아서 폼 커스터마이징
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
