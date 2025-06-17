from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags',]
        widgets= {
            'tags': forms.CheckboxSelectMultiple(),
            # 'featured_image': forms.ImageField()
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'featured_image':
                field.widget.attrs.update({'class': 'input input--file'})
            else:
                field.widget.attrs.update({'class': 'input'})
