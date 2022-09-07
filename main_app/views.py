from django.shortcuts import render, redirect
from newsapi import NewsApiClient
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Comment
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    apiKey = NewsApiClient(api_key= "f630b32438fe426088d3e9631d48efa1")
    headLines = apiKey.get_top_headlines(sources = 'associated-press')
    articles = headLines['articles']
    desc = []
    news = []
    img = []

    for index in range(len(articles)):
        article = articles[index]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    my_list = zip(news, desc, img)

    return render(request, 'home.html', context={'my_list': my_list})

def category(request):
    api_key = NewsApiClient(api_key= "f630b32438fe426088d3e9631d48efa1")
    head_Lines = api_key.get_sources(category='sports')
    categories = head_Lines['sources']
    desc = []
    name = []
    country = []

    for index in range(len(categories)):
        category = categories[index]
        desc.append(category['description'])
        name.append(category['name'])
        country.append(category['name'])
    my_list2 = zip(name, desc, country)

    return render(request, 'category.html', context={'my_list2': my_list2})
