from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .forms import CommentForm, BookCreateForm
from .models import Book


class BookListViews(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'
@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': book_comments,
        'comment_form': comment_form
    })


# class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
#     model = Book
#     fields = ['title', 'description', 'author', 'price', 'cover', 'publishers', 'translator']
#     template_name = 'books/book_create.html'
#
#     def test_func(self):
#         obj = self.get_object()
#         return obj.user == self.request.user

@login_required
def book_create_view(request):
    if request.method == 'POST':
        book_create_form = BookCreateForm(request.POST)
        if book_create_form.is_valid():
            new_book = book_create_form.save(commit=False)
            new_book.user = request.user
            new_book.save()
            return redirect('book_list')
    else:
        book_create_form = BookCreateForm()
    return render(request, 'books/book_create.html', context={'form': book_create_form})


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):

    model = Book
    fields = ['title', 'description', 'author', 'price', 'cover', 'publishers', 'translator']
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
