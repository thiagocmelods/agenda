from django import forms
from .models import Contatos


class FormContatos(forms.ModelForm):
    class Meta:
        model = Contatos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormContatos, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            

        self.fields['nome'].widget.attrs.update({'autofocus': 'autofocus'})
