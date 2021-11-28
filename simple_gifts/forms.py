from django import forms

class AssignerForm(forms.Form):
    names = forms.CharField(widget=forms.Textarea)
    emails = forms.CharField(widget=forms.Textarea)
    inclusions = forms.CharField(widget=forms.Textarea)
    exclusions = forms.CharField(widget=forms.Textarea)
