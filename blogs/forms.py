from django import forms
from blogs.models import Post, Comments


class PostFOrm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
