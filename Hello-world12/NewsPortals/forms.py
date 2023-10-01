from django import forms
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from .models import Post


class PostForm(forms.ModelForm):
    heading = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = ['author', 'category', 'heading', 'text', 'rating']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")

        if text is None:
            raise ValidationError(
                "Напишите текст"
            )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user