from django.shortcuts import redirect, render
from django.core.paginator import Paginator

import quote_site
from .forms import AuthorForm, QuoteForm
from .models import Quote, Tag, Author

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    tags = Tag.objects.all()
    topTenTags: list = sorted(tags, key=lambda tag: (tag.quotes.all().count(), tag.name), reverse=True)

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

    return render(request, "quote_site/index.html", {"quotes": quotes, "topTenTags": topTenTags})

def author_detail(request, id):
    author = Author.objects.get(pk=id)

    return render(request, "quote_site/author_detail.html", {"author": author})

def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_site:index')

        return render(request, 'quote_site/add_author.html', {'form': form})

    return render(request, "quote_site/add_author.html", {'form': AuthorForm()})

def add_quote(request):

    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_site:index')

        return render(request, 'quote_site/add_quote.html', {'form': form})

    return render(request, "quote_site/add_quote.html", {'form': QuoteForm()})

