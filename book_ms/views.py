from django.shortcuts import render

from .models import Book, Category

def home(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, 'home.html', context)



def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


