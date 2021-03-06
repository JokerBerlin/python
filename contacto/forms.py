from django import forms

class FormularioContactos(forms.Form):
    asunto = forms.CharField(max_length=5)
    email = forms.EmailField(required=False, label='Tu correo electronico')
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())
        if num_palabras < 4:
            raise forms.ValidationError('Se requiere mas de 4 palabras')
        return mensaje
