from django.shortcuts import render
from django.db.models.functions import Lower

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    
    # Extension 
    num_titles = Book.objects.annotate(title_lower=Lower('title')).values('title_lower').distinct().count()
    num_genres = Genre.objects.annotate(name_lower=Lower('name')).values('name_lower').distinct().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_titles': num_titles,
        'num_genres': num_genres,
    }
    

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    
class BookDetailView(generic.DetailView):
    model = Book