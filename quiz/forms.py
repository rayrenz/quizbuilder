from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'ng-model': 'vm.username',
            'class': 'form-control'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'ng-model': 'vm.password',
            'class': 'form-control'
        }
    ))
