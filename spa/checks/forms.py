from django import forms

class NameForm(forms.Form):
    sample_size = forms.DecimalField(
        label='Sample size',
        min_value=1
    )

    file = forms.FileField(
        label="Upload your file",
    )