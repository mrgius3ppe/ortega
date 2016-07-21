from django import forms 

class CommentForm(forms.Form):
	content_type=forms.CharField(widget=forms.HiddenInput)
	object_id=forms.IntegerField(widget=forms.HiddenInput)
	content=forms.CharField(label="Comentario",widget=forms.Textarea(attrs={'class': 'form-control','rows':'2','placeholder': 'Ingresa tus comentarios'}))

