from django.shortcuts import render, redirect
from book_authors_app.models import Books, Authors

def index(request):
    # main de la actividad
    return render(request, 'index.html')
    
def authors(request): 
    # página con los autores, add_authors permite agregar autores al listado
    books = Books.objects.all()
    authors = Authors.objects.all()
    context = {
        'books': books,
        'authors': authors
    }
    return render(request,'authors.html', context)

def books(request): 
    # página con los libros, add_books permite agregar libros al listado
    books = Books.objects.all()
    authors = Authors.objects.all()
    context = {
        'books': books,
        'authors': authors,
    }
    return render(request, 'books.html', context)

def author(request, idauthor): 
    # página de un autor específico, add_book permite agregar libros a ese autor
    author = Authors.objects.get(id=idauthor)
    books = Books.objects.all()
    context = {
        'books': books,
        'author': author
    }
    return render(request, 'author.html', context)

def book(request,idbook):
    # página de un libro en específico, add_author permite agregar autores al libro
    book = Books.objects.get(id=idbook)
    authors = Authors.objects.all()
    context = {
        'book':book,
        'authors': authors
    }
    
    return render(request, 'book.html', context)

def add_authors(request):
    # en la página de los libros, permite agregar un autor
    books = Books.objects.all()
    authors = Authors.objects.all()
    context = {
        'books': books,
        'authors': authors
    }
    author_firstname = request.POST['firstname']
    author_lastname = request.POST['lastname']
    author_notes = request.POST['notes']
    
    Authors.objects.create(first_name=author_firstname, last_name=author_lastname, notes=author_notes)
    
    return redirect("/authors", context)

def add_book(request):
    # función: permite agregar autores a un libro específico, en la página del libro)
    books = Books.objects.all()
    book_id = request.POST['id']
    idauthor = request.POST['idauthor']
    author = Authors.objects.get(id=idauthor)
    book = Books.objects.get(id=book_id)
    context = {
        'author': authors,
        'books': books,
        'book_id': book_id,
        'author': author,
    }
    author.books.add(book)
    return redirect("/authors", context)

def add_author(request):
    # función: permite agregar autores a un libro específico, en la página del libro)
    authors = Authors.objects.all()
    author_id = request.POST['id']
    idbook = request.POST['bookid']
    book = Books.objects.get(id=idbook)
    author = Authors.objects.get(id=author_id)
    context = {
        'book': book,
        'authors': authors,
        'author_id': author_id,
        'author': author,
    }
    book.authors.add(author)
    return redirect("/books", context)

def add_books(request):
    book_title = request.POST['title']
    book_desc = request.POST['desc']
    
    Books.objects.create(title=book_title, desc=book_desc)
    return redirect("/books")

def del_books(request):
    book_id = request.POST['book_id']
    
    del_book = Books.objects.get(id=book_id)
    del_book.delete()
    return redirect("/books")

