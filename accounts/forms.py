from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'age', 'email', )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email', )
