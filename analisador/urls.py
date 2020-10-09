from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name="login"),
    path('cad_usu',views.cadastrar_usuario,name="cad_usu"),
    path('analise_grafico',views.analise_grafico,name="analise_grafico"),
    path('redefinir_senha',views.redefinir_senha,name="redefinir_senha"),
    path('upload_arquivo',views.upload_arquivo,name="upload_arquivo")
]
