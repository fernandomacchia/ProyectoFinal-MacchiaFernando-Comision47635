from django import forms
from pagina_blog.models import Noticias 

class NoticiaFormulario(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        super(NoticiaFormulario, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget = HiddenInput()

    class Meta:
        model = Noticias
        fields = ['usuario','titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen','imagen_texto']
        ordering = ['-fecha_publicacion']



class EditNoticiasForm(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    class Meta:
        model = Noticias
        fields = ['titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen','imagen_texto']
        ordering = ['-fecha_publicacion']