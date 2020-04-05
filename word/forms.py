from django import forms
from word.models import Word

class AddForm(forms.ModelForm):
	class Meta:
		model = Word
		fields = ["main_word", "mean_word"]