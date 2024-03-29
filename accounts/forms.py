from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    #email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
        'username'
        ,'email'
        ,)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # user.first_name = self.cleaned_data['first_name']
        # user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # user.stripe_id
        if commit:
            print(user.email)
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email'
            ,'first_name'
            ,'last_name'
            ,'password')
        exclude = ()
