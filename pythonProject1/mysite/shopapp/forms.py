from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm (UserCreationForm):

##       label='',
   #     max_length=30,
  #      min_length=5,
   #     required=True,
  #      widget=forms.TextInput(
  #          attrs={
   #             "placeholder": "Username",
   #             "class": "form-control"
   #         }
   #     )
   # )

   # password1 = forms.CharField(
 #       label='',
  #      max_length=30,
   #     min_length=8,
  #      required=True,
  #      widget=forms.PasswordInput(
   #         attrs={
   #             "placeholder": "Password",
     #           "class": "form-control"
     #       }
     #   )
   # )

    password2 = forms.CharField(
        label='',
        max_length=30,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')