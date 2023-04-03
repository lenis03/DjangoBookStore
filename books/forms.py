from django import forms
from .models import Comment, Book


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend',)


class BookCreateForm(forms.ModelForm):
    class Meta:
        model =Book
        fields = ['title', 'description', 'author', 'price', 'cover', 'publishers', 'translator']
