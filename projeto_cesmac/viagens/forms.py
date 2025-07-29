from django import forms
from django.contrib.auth.models import User
from .models import Viagem, UserProfile


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['origem', 'destino', 'horario', 'preco', 'vagas']
        widgets = {
            'horario': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'origem': forms.TextInput(attrs={'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'vagas': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class UserProfileForm(forms.ModelForm):
    genero = forms.ChoiceField(
        choices=UserProfile._meta.get_field('genero').choices,
        widget=forms.RadioSelect(),
        required=True
    )
    tipo_usuario = forms.ChoiceField(
        choices=UserProfile._meta.get_field('tipo_usuario').choices,
        widget=forms.RadioSelect(),
        required=True
    )

    class Meta:
        model = UserProfile
        fields = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'telefone', 'genero', 'tipo_usuario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data["password1"])
            user.save()
        return user
