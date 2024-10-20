from django.urls import reverse_lazy
from django.views import generic

from . import models, forms

class SignUpView(generic.CreateView):
    form_class = forms.CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
