#!/user/bin/env python
__author__ = 'Howie'
from django import forms as fforms
from django.forms import fields

class UserForm(fforms.Form):
    username = fields.CharField(required=True,max_length=32)
    email = fields.EmailField(required=True,max_length=32)
    city = fields.ChoiceField(
        choices=[(1,'广州'),(2,'上海'),(3,'北京')],
        initial=2,
    )
