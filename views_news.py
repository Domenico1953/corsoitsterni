from django.shortcuts import get_object_or_404, render
from news.models import Article, Journalist

"""    MASTER    """

def article_detail_view(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {"article": article } 
    return render(request, "news/detail_view.html", context)

def list_view(request):
    articles = Article.objects.all()  # creo un query set
    journalists = Journalist.objects.all()  # creo un query set
    context = {"articles": articles, "journalists": journalists } 
    return render(request, "news/list_view.html", context)
