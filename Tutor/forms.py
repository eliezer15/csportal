from django import forms
from Tutor.models import Post

class PostForm(forms.ModelForm):
    Email = forms.EmailField()
    Compensation = forms.IntegerField()
    Password = forms.CharField(widget= forms.PasswordInput())
    Added = forms.DateTimeField(widget=forms.HiddenInput, required=False)
    Uploaded= forms.DateTimeField(widget=forms.HiddenInput, required=False)
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Post
