from django import forms
from .models import Idea
from apps.devtools.models import DevTool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'image', 'content', 'interest', 'devtool']
    
    devtool = forms.ModelChoiceField(
        queryset=DevTool.objects.all(),
        empty_label="개발툴 선택",
        widget=forms.Select(attrs={'class': 'form-select'})
    )