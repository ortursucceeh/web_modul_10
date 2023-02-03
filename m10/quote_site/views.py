from django.shortcuts import render
from .models import Quote, Tag, Author
from django.core.paginator import Paginator
import quote_site
# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    
    tag_name = request.GET.get('tag_name')
    if tag_name:
        try:
            tag_id = Tag.objects.get(name=tag_name.capitalize()).id
            quotes = quotes.filter(tags__in=[tag_id])    
        except quote_site.models.Tag.DoesNotExist as e:
            quotes = []

    paginator = Paginator(quotes, 4)
    page = request.GET.get('page')
    quotes = paginator.get_page(page)

    return render(request, "quote_site/index.html", {"quotes": quotes})

def author_detail(request, id):
    author = Author.objects.get(pk=id)

    return render(request, "quote_site/author_detail.html", {"author": author})


def add_quote(request):
    return render(request, "quote_site/add_quote.html")

def add_author(request):
    return render(request, "quote_site/add_quote.html")