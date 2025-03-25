from django import forms
from .models import Post

# Form for creating and updating posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Link form to the Post model
        fields = '__all__'  # Include all fields from the Post model

# Form for adding and updating comments (uses forms.Form instead of ModelForm)
class commentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})  # TextArea input for comment content
    )