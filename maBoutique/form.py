from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'description')
        titre = forms.CharField(max_length=150)
        description = forms.Textarea()