from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
    Create a form for owner users to add newsletters
    """

    class Meta:
        model = Newsletter
        fields = ['newsletter_title', 'newsletter_body', 'newsletter_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
