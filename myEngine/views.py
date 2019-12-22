from django.shortcuts import render
from .forms import SearchEngine
from lexicon import *
from forward_index.forward_index import *
from inverted_index.inverted_index import *
from config import *
from searching.searching import *


# Create your views here.

# Get questions and display them

def index(request):
    if request.method == 'POST':
            form = SearchEngine(request.POST)
            if form.is_valid():
                files = list()
                print(form.cleaned_data["your_query"])
    
            
    else:
        form = SearchEngine()
            
    return render(request, 'myEngine/index.html',{'form':form})