from django import forms
from myapp.models import Movie


class MovieForm(forms.Form):

        title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

        year=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

        runtime=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control border border-info"}))

        language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

        genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))

        director_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))



class MovieModelForm(forms.ModelForm):
        
        class Meta:
                model=Movie
                #fields=__all__
                exclude=("id",)

        widgets={
                "title":forms.TextInput(attrs={"class":"form-control border border-info"}),
                "year":forms.TextInput(attrs={"class":"form-control border border-info"}),
                "runtime":forms.TextInput(attrs={"class":"form-control border border-info"}),
                "language":forms.TextInput(attrs={"class":"form-contol border border-info"}),
                "genre":forms.TextInput(attrs={"class":"form-control border border-info"}),
                "director_name":forms.TextInput(attrs={"class":"form-cntrol border border-info"}),
        }