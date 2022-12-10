from django import forms

from .models import Place, Topic, Entry

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ["title"]

        widgets ={
            "title": forms.TextInput(attrs = {"class": "form-control", "placeholder" : "Use Title Case Format"})
        }

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title"]

        widgets ={
            "title": forms.TextInput(attrs = {"class": "form-control", "placeholder" : "Use Title Case Format"})
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = [
            "place",
            "topic",
            "title",
            "details"
        ]

        widgets ={
            "place": forms.Select(attrs = {"class": "form-select"}),
            "topic": forms.Select(attrs = {"class": "form-select"}),
            "title": forms.TextInput(attrs = {"class": "form-control", "placeholder" : "Use Title Case Format"}),
            "details": forms.Textarea(attrs = {"class": "form-control", "rows": 5}),
        }