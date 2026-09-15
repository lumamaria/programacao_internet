from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models

# Create your views here.
def categorias_lista_view(request):
    categorias = models.Categoria.objects.all()

    print("List Method:", request.method)

    return render(request, "categoria/lista.html", {
        "categorias": categorias
    })

def categoria_detalhe_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)

    print("Detail Method:", request.method)

    return render(request, "categoria/detalhe.html", {
        "categoria": categoria,
    })

def categoria_create_view(request):
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            models.Categoria.objects.create(
                nome=nome
            )
            return redirect("noticias:categorias")
    else:
        form = forms.CategoriaForm()

    return render(request, "categoria/form.html", {
        "form": form,
    })

def categoria_update_view(request, categoria_id):
    categoria = models.Categoria.objects.get(id=categoria_id)

    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            categoria.nome = form.cleaned_data["nome"]
            categoria.save()
            return redirect("noticias:categorias")
    else:
        form = forms.CategoriaForm(initial={"nome": categoria.nome})

    return render(request, "categoria/form.html", {
        "form": form,
        "categoria": categoria,
    })

def tags_lista_view(request):
    tags = models.Tag.objects.all()

    return render(request, "tag/lista.html", {
        "tags": tags
    })

def tag_detalhe_view(request, tag_id):
    tag = models.Tag.objects.get(id=tag_id)

    return render(request, "tag/detalhe.html", {
        "tag": tag,
    })

def noticias_lista_view(request):
    noticias = models.Noticia.objects.all()

    return render(request, "noticia/lista.html", {
        "noticias": noticias
    })

def noticia_detalhe_view(request, noticia_id):
    noticia = models.Noticia.objects.get(id=noticia_id)

    return render(request, "noticia/detalhe.html", {
        "noticia": noticia,
    })

