from django.shortcuts import render
from .models import Quote, Tag
# Create your views here.
def index(request):

    quotes = Quote.objects.all()
    
    return render(request, "quote_site/index.html", {"quotes": quotes})