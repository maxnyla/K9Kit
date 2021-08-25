from django import forms
from .models import Tip


class TipForm(forms.ModelForm):
    """ Create a form for owner users to add tip posts """

    class Meta:
        model = Tip
        fields = ['tip_title', 'tip_body', 'tip_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
