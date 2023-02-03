from django.shortcuts import render
from .models import Quote, Tag, Author
# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    
    return render(request, "quote_site/index.html", {"quotes": quotes})

def author_detail(request, id):
    author = Author.objects.get(pk=id)

    return render(request, "quote_site/author_detail.html", {"author": author})


def add_quote(request):
    pass

def add_author(request):
    pass