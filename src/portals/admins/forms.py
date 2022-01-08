from django import forms

from .models import (
    ProjectType
)


class ProjectTypeForm(forms.ModelForm):
    class Meta:
        model = ProjectType
        fields = '__all__'

