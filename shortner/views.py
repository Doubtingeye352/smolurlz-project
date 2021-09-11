from django.shortcuts import render, redirect
import uuid
from .models import Url
import pyperclip




# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        
        try:
            copy = request.POST.get('text')
            pyperclip.copy(copy)
            pyperclip.paste()
            
        except:
            return render(request,'finished.html', {'final': "https://smolurlz.herokuapp.com/"+uid})
        return render(request, 'finished.html', {'final': "https://smolurlz.herokuapp.com/"+uid})

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
