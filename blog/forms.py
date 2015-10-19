from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']


class SearchForm(forms.Form):
    tag = forms.CharField(max_length=50)
