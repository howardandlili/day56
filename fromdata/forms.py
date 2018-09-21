#!/user/bin/env python
__author__ = 'Howie'
from django import forms as fforms
from django.forms import fields

class UserForm(fforms.Form):
    username = fields.CharField(required=True,max_length=32)
    email = fields.EmailField(required=True,max_length=32)
