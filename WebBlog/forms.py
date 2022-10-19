from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class form_historias(forms.Form):
    titulo = forms.CharField(max_length=40)
    nombreCreador = forms.CharField(max_length=40)
    cuerpoHistoria = forms.CharField(max_length=9999)
    fechaHistoria = forms.DateField()

class UserRegisterForm(UserCreationForm): #basicamente agarra el form original de django(UserCreationForm) y lo personalizo con fields nuevos
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    #aunque las variables empiezen con minusculas, en la web se ven con la inicial en mayuscula
    #salvo que se use label.
    usuario = forms.CharField(widget = forms.TextInput(attrs={'placeholder': "Usuario"}))
    email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': "Email"}))
    nombre = forms.CharField(widget = forms.TextInput(attrs={'placeholder': "Nombre"}))
    apellido = forms.CharField(widget = forms.TextInput(attrs={'placeholder': "Apellido"}))
    contraseña = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': "Contraseña"}))

    class Meta:
        model = User
        fields = ["usuario", "email", "nombre", "apellido", "contraseña"]
        help_texts = {k: "" for k in fields}

class UserChangePW(PasswordChangeForm):
    #estas variables de abajo, tienen que tener el nombre del form original de django, para poder asignarles un label en español
    old_password = forms.CharField(label="Contraseña anterior", widget = forms.PasswordInput(attrs={'placeholder': "Contraseña anterior"}))
    new_password1 = forms.CharField(label="Nueva contraseña",widget = forms.PasswordInput(attrs={'placeholder': "Contraseña nueva"}))
    new_password2 = forms.CharField(label="Repita la contraseña",widget = forms.PasswordInput(attrs={'placeholder': "Repita contraseña"}))
    
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]
        help_texts = {k: "" for k in fields}

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField()