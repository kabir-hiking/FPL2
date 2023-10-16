from django import forms

class DataForm(forms.Form):
    feature1 = forms.FloatField()
    # feature2 = forms.FloatField()
    # Add other features as needed
