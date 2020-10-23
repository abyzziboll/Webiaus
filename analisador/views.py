from django.shortcuts import render
from analisador.models import Usuario
from .forms import UsuarioForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def login(request):
    return render(request,'login.html',{})

def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.nome = request.nome
            usuario.email = request.email
            usuario.senha = request.password
            usuario.funcao = request.sel1
            usuario.save()
            return redirect('home')
    else:
        form = UsuarioForm()
    return render(request,'cadastrar-usuario.html',{'form':form})

def analise_grafico(request):
    return render(request,'analise-grafico.html',{})

def redefinir_senha(request):
    return render(request,'redefinir-senha.html',{})

def upload_arquivo(request):
    return render(request,'upload-arquivo.html',{})