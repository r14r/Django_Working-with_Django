from django import forms
from .models import CRUDModel


# creating a form
class CRUDForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = CRUDModel

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
