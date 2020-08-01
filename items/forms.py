from django import forms


class SearchQueryForm(forms.Form):
    query = forms.CharField(max_length=20)
    