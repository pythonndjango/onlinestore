from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm   #su dung usercreattion form de tao fomr trong django
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product,Manufacturer
# Create your views here.
# code login
def home(request):
    count = User.objects.count()
    return render (request, 'home.html',
                    {'count':count})

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')                       #llink ra trang home
    else:
        form = UserCreationForm()
    return render(request, 
                  'registration/signup.html',
                  context= {'form':form})



# code san phamc
class ProductDetaiView(DetailView):
    model = Product
    template_name = "products-detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "products-list.html"
