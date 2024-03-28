from django.forms import ModelForm, widgets, ValidationError
from webapp import models


class PublicForm(ModelForm):
    class Meta:
        model = models.Public
        fields = ['description', 'img_files']
        widgets = {
            'description': widgets.Textarea(attrs={
                'class': 'my-3 form-control', 'style': 'width: 200px'},
            )}


class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']
        widgets = {
            'comment': widgets.Textarea(attrs={
                'class': 'my-3 form-control comment-form',
                'style': 'higth: 20px; border: none;'
            })
        }
