# sales/views.py
from django.shortcuts import render

def home(request):
    """
    Home page view for the sales app
    - Accepts HttpRequest object
    - Returns HttpResponse with rendered template
    """
    return render(request, 'sales/home.html')