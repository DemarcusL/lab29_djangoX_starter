#  control all our models for forms
from django.forms import ModelForm, fields
# know what model we want to base this form on
from .models import Snack

class SnackForm(ModelForm):
      # The meta data is used to set what the form will hold.
      class Meta:
            model = Snack
            fields = ['name','purchaser','description']