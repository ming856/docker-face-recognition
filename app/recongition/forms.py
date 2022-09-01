from django import forms
from recongition.models import *
  
class recognitions_Form(forms.ModelForm):
    # img = forms.ImageField(label = 'Choose your image', help_text = 'The image should be cool.')
    class Meta:
        model = face
        fields = ['img']