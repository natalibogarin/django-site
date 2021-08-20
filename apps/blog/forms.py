from django import forms
from django.forms import widgets
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'content')

        widgets ={
            'title': forms.TextInput(attrs={'class':'textIntputClass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.Form):
        model = Comment
        fields = ('author', 'comment_body',)

        author = forms.CharField(
            max_length=60,
            widget=forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingresa tu nombre"
            })
        )
        comment_body = forms.CharField(widget=forms.Textarea(
            attrs={
                "class": "form-control comment-textarea",
                "id":"comment",
                "placeholder": "Dinos que piensas, dejanos un comentario!"
            })
        )
