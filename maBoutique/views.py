from django.shortcuts import render
from django.http import HttpResponse
from .form import ArticleForm
from .models import Article

def home(request):
    return render(request, "index.html")
    #return render(request, "accueil.html")
    #return HttpResponse('<html><body><p>Bienvenue !</P></body></html>')


def article_list(request):
    article = Article.objects.all()
    context = {'article_list': article}
    return render(request, "article_list.html", context)


def article_detail(request, id):
    each_article = Article.objects.get(id=id)
    context = {'article_detail': each_article}
    return render(request, "article_detail.html", context)


def article_delete(request, id):
    each_article = Article.objects.get(id=id)
    each_article.delete()
    return article_list(request)

def articleForm(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            description = form.cleaned_data['description']
            form.save()
            return article_list(request)
    else:
        # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ArticleForm()	# Nous créons un formulaire vide
        return render(request, 'form.html', locals() )

