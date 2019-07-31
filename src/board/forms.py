from  django import forms
from .models import BoardPost

class BoardPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)

class BoardPostModelForm(forms.ModelForm):
    class Meta:
        model = BoardPost
        fields = ['title', 'slug', 'content']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        instance = self.instance
        #print(instance)
        #print(dir(self))
        qs = BoardPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) #-> id=instance.id
        if qs.exists():
            raise forms.ValidationError('This title has already been used')
        return title