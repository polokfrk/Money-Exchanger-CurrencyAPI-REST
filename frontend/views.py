from django.shortcuts import render
from urllib.request import Request, urlopen
import json

from bs4 import BeautifulSoup
import requests


# Create your views here.


def list(request):

    return render(request, 'frontend/list.html')
