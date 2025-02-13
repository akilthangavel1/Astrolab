from django import forms



class PersonAddForm(forms.Form):
    pass

class PersonEditForm(forms.Form):
    pass

class PersonMatchForm(forms.Form):
    pass

# Form for signing in
# class SignInForm(forms.Form):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)
