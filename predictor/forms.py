from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.IntegerField()
    cp = forms.IntegerField()
    trestbps = forms.IntegerField()
    chol = forms.IntegerField()
    fbs = forms.IntegerField()
    restecg = forms.IntegerField()
    thalach = forms.IntegerField()
    exang = forms.IntegerField()
    oldpeak = forms.FloatField()
    slope = forms.IntegerField()