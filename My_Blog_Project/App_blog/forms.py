from django import forms
from App_blog.models import Blog, Comment

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
