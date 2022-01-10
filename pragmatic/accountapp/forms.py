from django import forms

from accountapp.models import Post


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name name', max_length=7)

class PostForm(forms.Form):
	title = forms.CharField()

# ModelForm.save 인터페이스를 흉내내어 구현
	def save(self, commit=True):
		post = Post(**self.cleaned_data)
		if commit:
			post.save()
		return post
