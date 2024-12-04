from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.http import JsonResponse

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__iregex=query) | Q(description__iregex=query))
    else:
        books = Book.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(list(books.values()), safe=False)
    else:
        return render(request, 'books/book_list.html', {'books': books})
