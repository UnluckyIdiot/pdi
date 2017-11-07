from django.shortcuts import render, get_object_or_404
from blog.models import Article
from django.contrib import auth
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    articles = Article.objects.all()
    username = auth.get_user(request).username
    context = {"articles": articles, "username": username}
    return render(request, 'blog/home.html', context)


@login_required
def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    username = auth.get_user(request).username
    return render(request, 'blog/article.html', {'article': article,
                                                 'username': username,
                                                 })


@login_required
def about(request):
    username = auth.get_user(request).username
    return render(request, 'blog/about.html', {'username':username})