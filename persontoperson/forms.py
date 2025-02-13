from django import forms
from .models import birthchartdb


# creating a form
class GeeksForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = birthchartdb

        # specify fields to be used
        fields = '__all__'