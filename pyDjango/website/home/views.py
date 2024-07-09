from datetime import datetime
from django.shortcuts import render

def index(request):
    current_datetime = datetime.now()
    context = {
        'current_datetime': current_datetime,
    }
    return render(request,"index.html",context)
# Create your views here.
