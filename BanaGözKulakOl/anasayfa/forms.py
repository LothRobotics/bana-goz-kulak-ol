from django import forms

class UpdateUserForm(forms.Form):
    your_name = forms.CharField(label='Adınız', max_length=100)
    your_surname = forms.CharField(label='Soyadınız', max_length=100)
    email = forms.CharField(label='E-Posta', max_length=100)
    username = forms.CharField(label='Kullanıcı Adı', max_length=100)