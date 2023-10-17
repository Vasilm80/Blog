from django import forms


class CommentForms (forms.form):
    autor = forms.CharField(max_length=60,
                            widget=forms.TextInput(attrs={

                            }))