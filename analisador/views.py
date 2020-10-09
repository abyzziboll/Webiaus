from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html',{})

def cadastrar_usuario(request):
    return render(request,'cadastrar-usuario.html',{})

def analise_grafico(request):
    return render(request,'analise-grafico.html',{})

def redefinir_senha(request):
    return render(request,'redefinir-senha.html',{})

def upload_arquivo(request):
    return render(request,'upload-arquivo.html',{})