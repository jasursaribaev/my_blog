from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from users.models import CustomUser

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
    def save(self, commit=True):
      user = super().save(commit)
      user.set_password(self.cleaned_data['password1'])
      user.save()
      return user
      # user = super(UserRegisterForm, self).save(commit=False)
      # user.email = self.cleaned_data['email']
      # if commit:
      #   user.save()
      # username = self.cleaned_data['username']
      # first_name = self.cleaned_data['first_name']
      # last_name = self.cleaned_data['last_name']
      # email = self.cleaned_data['email']
      # password1 = self.cleaned_data['password1']
      # password2 = self.cleaned_data['password2']
      # user = User.objects.create(
      #   username=username,
      #   first_name=first_name,
      #   last_name=last_name,
      #   email=email,
      # )
      # user.set_password(password1)
      # user.save()
      # return user
      #Komil1234K
      
# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'placeholder': 'Username',
#                                                              'class': 'form-control',
#                                                              }))
#     password = forms.CharField(max_length=50,
#                                 required=True,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password',
#                                                                   'class': 'form-control',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))
    
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'image')