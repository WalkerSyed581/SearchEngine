from django.shortcuts import render
from .forms import SearchEngine
from lexicon import *
from forward_index.forward_index import *
from inverted_index.inverted_index import *
from config import *
from searching.searching import Searching


# Create your views here.

# Get questions and display them

def index(request):
    context = dict()
    if request.method == 'POST':
            form = SearchEngine(request.POST)
            if form.is_valid():
                files = list()
                makePaths()
                searcher = Searching()
                try:
                    results = searcher.search(form.cleaned_data["your_query"])
                except:
                    context = {"form":form,"error": "Invalid Query: {}".format(form.cleaned_data["your_query"]) }
                    return render(request,'myEngine/index.html',context)
                context = {"form":form,"results":results}
    else:
        form = SearchEngine()
        context = {"form": form}
            
    return render(request, 'myEngine/index.html',context)

def buildIndex(request):
    context = dict()
    if request.method == 'POST':
            form = SearchEngine(request.POST)
            if form.is_valid():
                files = list()
                makePaths()
                searcher = Searching()
                try:
                    results = searcher.search(form.cleaned_data["your_query"])
                except:
                    context = {"form":form,"error": "Invalid Query: {}".format(form.cleaned_data["your_query"]) }
                    return render(request,'myEngine/index.html',context)
                context = {"form":form,"results":results}
    else:
        buildForwardIndex()
        buildInvertedIndex()
        form = SearchEngine()
        context = {"form": form}
    return render(request,'myEngine/index.html',context)