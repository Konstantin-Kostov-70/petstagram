from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", 'email',)


class UserLoginForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True, "placeholder": "Username",
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "placeholder": "Password"}),
    )


class UserEditForm(forms.ModelForm):

    user_photo = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'class': 'label-input',
                   'placeholder': 'Chose file'}),
    )
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username', 'user_photo', 'email', 'gender')
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'username': 'Username',
                  'email': 'Email',
                  'gender': 'Gender',
        },

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                    'class': 'label-input'
                }

            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                    'class': 'label-input',
                }

            ),

            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                    'class': 'label-input',
                }

            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'label-input',
                }

            ),

        }
