from django.shortcuts import render
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactMessage(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'MESSAGE SENT SUCCESFULLTY')
        else:
            messages.error(request, 'ERROER WHY SENDING MESSAGE')
    else:
        form = ContactMessage()
    return render(request, 'index.html', {'form': form})                
