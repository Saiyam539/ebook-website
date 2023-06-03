from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'index.html')

def loginuser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method=='POST':
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'You are now loged in')
            return redirect('/')
        
        else:
            messages.success(request,f'Username or password is incorrect')
            return render(request,'login.html') 
        
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    messages.success(request,f'You are logged out')
    return redirect('loginuser')

def signinuser(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.method=='POST':
            User.objects.create_user(username,email,password)
            messages.success(request,f'Account created Successfully ')
            return redirect('/loginuser')
    except Exception as e:
        messages.error(request, "Username already exists. Please choose a different username.")
    return render(request,'signin.html')

def show_book(request):
    autobiography_book = Books.objects.filter(book_genre=2)
    thriller_book = Books.objects.filter(book_genre=1)
    children_book = Books.objects.filter(book_genre=4)
    mythology_book = Books.objects.filter(book_genre=5)
    testings = Books.objects.filter(book_genre=7)
    context = {
        'autobiography_book':autobiography_book,
        'thriller_book':thriller_book,
        'children_book':children_book,
        'mythology_book':mythology_book,
        'testing':testings
    }
    return render(request,'show_book.html',context)

def view_book(request,id):
    book = Books.objects.get(id=id)
    
    context = {
        'book':book
    }
    return render(request,'view_book.html',context)

def download_pdf(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    response = FileResponse(open(book.pdf_file.path, 'rb'), as_attachment=True)
    return response

@login_required(login_url='/loginuser')
def add_wish_list(request,id):
    book = get_object_or_404(Books, pk=id)
    Wishes.objects.create(user=request.user,book=book)
    messages.success(request, "Added To Wish List")
    return redirect('view_book', id=id)

@login_required(login_url='/loginuser')
def show_wish_list(request):
    wishlist = Wishes.objects.filter(user=request.user)
    is_empty = wishlist.count() == 0 if wishlist else True
    context = {
         'wishlist':wishlist,
         'is_empty':is_empty,
         'user':request.user

    }
    return render(request,'wishlist.html',context)

def delete_items(request,id):
    wishlist = Wishes.objects.get(id=id)
    wishlist.delete()
    return redirect('/view_wish_list')
        