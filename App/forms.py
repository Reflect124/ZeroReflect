from django import forms


class ContactForms(forms.Form):
    name = forms.CharField(label="", max_length=55, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Full Name'}))
    phone = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Contact Number'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address'}))
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Valuable Comments'}))