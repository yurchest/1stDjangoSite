from django import forms
from .models import Contact

class ContactFormCv(forms.ModelForm):

	class  Meta:
		model = Contact
		fields = ('name', 'email', 'text',)
		widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }