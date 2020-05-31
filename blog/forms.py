from django import forms
from tinymce import TinyMCE
from .models import Post, Category, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    categories  = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, help_text="Choose categories", queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'short_content', 'content', 'date_posted', 'image', 'categories') #author is request.user

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )