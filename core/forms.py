from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = models.EmailField(max_length=250)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email):
            raise ValidationError("このメールアドレスは登録済みですよっ！")
        return email    