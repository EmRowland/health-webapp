from django import forms


class BlogSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False)