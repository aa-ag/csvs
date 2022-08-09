from django import forms

class NameForm(forms.Form):
    initials = forms.CharField(label='Your initials', max_length=2)