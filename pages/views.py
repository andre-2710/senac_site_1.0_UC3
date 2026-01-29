from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', {
        'mensagem': 'Bem-Vindo ao site.'
    })

def sobre(request):
    return render(request, 'pages/sobre.html', {})

def contato(request):
    return render(request, 'pages/contato.html', {})

def ajuda(request):
    return render(request, 'pages/ajuda.html', {})