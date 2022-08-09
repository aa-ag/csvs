from django import forms

class NameForm(forms.Form):
    sample_size = forms.DecimalField(
        label='Sample Size',
        min_value=1
    )