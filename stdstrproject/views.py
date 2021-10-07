from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Product
from.models import Product_laptop
from.models import Product_tablet
from.models import Product_uniform
from.models import Product_stationery
from.models import Cart
from.models import Pdf
from django.contrib.auth.models import User, auth
from django.urls import reverse
# Create your views here.
def index(request):
    
    return render(request, 'index.html')
def book(request):
    products = Product_uniform.objects.all()
    params = {'product': products}
    return render(request, 'book.html', params)

def uniform(request):
    products = Product_uniform.objects.all()
    params = {'product': products}
    return render(request, 'uniform.html', params)

def tablet(request):
    products = Product_uniform.objects.all()
    params = {'product': products}
    return render(request, 'tablet.html', params)

def pdf(request):
    pdfs = Pdf.objects.all()
    params = {'pdf': pdfs}
    return render(request, 'pdf.html', params)


def laptop(request):
    products = Product_uniform.objects.all()
    params = {'product': products}
    return render(request, 'laptop.html', params)


def stationery(request):
    products = Product_uniform.objects.all()
    params = {'product': products}
    return render(request, 'stationery.html', params)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print("no login")
            return redirect('login')
    else:
     return render(request, 'login.html')
def registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(first_name=first_name, last_name=last_name,username = username, password=password1, email=email )
        user.save();
        return redirect('/')
    else:
     return render(request, 'registration.html')




def cart(request):
    cart = Cart.objects.all()[0]
    params = { 'cart' : cart}
    return render(request, 'cart.html', params)
def logout(request):
    auth.logout(request)
    return redirect('/')
def checkout(request):
    return render(request,'checkout.html')

