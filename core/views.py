import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Anime

def lista_animes(request):
    animes = Anime.objects.all().order_by('-criado_em')
    return render(request, 'lista.html', {'animes': animes})

def buscar_api(request):
    resultados = []
    query = request.GET.get('q', '')
    if query:
        url = f"https://kitsu.io/api/edge/anime?filter[text]={query}&page[limit]=6"
        headers = {'Accept': 'application/vnd.api+json'}
        try:
            resposta = requests.get(url, headers=headers, timeout=5)
            if resposta.status_code == 200:
                dados = resposta.json().get('data', [])
                for item in dados:
                    atributos = item.get('attributes', {})
                    resultados.append({
                        'mal_id': item.get('id'),
                        'title': atributos.get('canonicalTitle', 'Sem título'),
                        'images': {'jpg': {'image_url': atributos.get('posterImage', {}).get('small', '')}}
                    })
        except Exception as e:
            print(f"--- Erro API Kitsu: {e} ---")
            
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})

def adicionar_anime(request):
    if request.method == 'POST':
        anime, created = Anime.objects.get_or_create(
            mal_id=request.POST.get('mal_id'),
            defaults={
                'titulo': request.POST.get('titulo'),
                'imagem_url': request.POST.get('imagem_url')
            }
        )
        if created:
            messages.success(request, 'Anime adicionado com sucesso!')
        else:
            messages.info(request, 'Este anime já está na sua lista.')
    return redirect('lista_animes')

def editar_anime(request, id):
    anime = get_object_or_404(Anime, id=id)
    if request.method == 'POST':
        anime.status = request.POST.get('status')
        anime.nota = request.POST.get('nota')
        anime.save()
        messages.success(request, 'Anime atualizado com sucesso!')
        return redirect('lista_animes')
    return render(request, 'editar.html', {'anime': anime})

def excluir_anime(request, id):
    anime = get_object_or_404(Anime, id=id)
    if request.method == 'POST':
        anime.delete()
        messages.error(request, 'Anime removido da sua lista.')
    return redirect('lista_animes')