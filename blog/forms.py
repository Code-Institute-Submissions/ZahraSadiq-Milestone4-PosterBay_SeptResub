from django import forms
from .models import Post 


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = Post.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in category]

        self.fields['post'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
