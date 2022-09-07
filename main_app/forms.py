from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import Comment

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['name', 'desc', 'email']