from django.shortcuts import render, redirect
from django.views import View
from libApp.forms import LoginForm, UserRegisterForm, BookUploadForm, BookUpdateForm
from django.views.generic import TemplateView, CreateView, FormView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, settings
from django.contrib import messages
from libApp.models import Books
from django.utils.decorators import method_decorator
from libApp.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
import razorpay

# Create your views here.

class ReaderHomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    
# @method_decorator(login_required, name='dispatch')
# class ReaderBookView(View):
#     def get(self, request, *args, **kwargs):
#         print(request.user)
#         return render(request, 'reader_book.html')

@method_decorator(login_required, name='dispatch') 
class BookListView(ListView):
    model = Books
    template_name = 'reader_book.html'
    context_object_name = 'book'


class AdminHomeView(ListView):
    model = Books
    template_name = 'admin_home.html'
    context_object_name = 'book'

class UserRegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            # send_mail('City Library', 'Your Account is registered Successfuly', settings.EMAIL_HOST_USER, {email})
            return redirect('login_view')
        else:
            return redirect('register_view')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('reader_home')


class UserLoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request,*args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_superuser == 1:
                return redirect('admin_home')
            else:
                login(request, user)
                print(request.user)
                return redirect('readerbook_view')



class BookUploadView(FormView):
    # model = Books
    form_class = BookUploadForm
    template_name = 'book_upload.html'
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        form = BookUploadForm(request.POST, request.FILES)
        # print()
        if form.is_valid():
            form.save()
            return redirect('listbooks_view')
        else:
            return redirect('readerbook_view')

class ListStudentLogedin(ListView):
    # model = User
    # template_name = 'admin_home.html'
    # context_object_name = 'reg'

    def get(self, request, *args, **kwargs):
        us = User.objects.filter(is_superuser =False)
        return render(request, 'list_student.html', {'us':us})
            

class ListBooks(ListView):
    model = Books
    template_name = 'admin_home.html'
    context_object_name = 'book'

class BookUpdateView(UpdateView):
    pk_url_kwarg = 'id'
    model = Books
    form_class = BookUpdateForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('listbooks_view')



class BookDeleteView(DeleteView):
    model = Books
    template_name = 'confirm_cancel.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listbooks_view')


class BookDetailView(DetailView):
    model = Books
    template_name = 'detail_view.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'

    
class BookSearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('search')
        results = Books.objects.filter(Q(bookname__icontains=query) | Q(author__icontains=query))
        if results:
            return render(request, 'search_result.html', {'query':query, 'results':results})
        else:
            messages.success(request, "Oops ! Something went wrong, Looks like we don't have the Book you are looking for.")
            return redirect('readerbook_view')
    
class AdminStudentDeleteView(DeleteView):
    model = User
    pk_url_kwarg = 'id'
    template_name = 'confirm_cancel.html'
    success_url = reverse_lazy('liststudent_view')

class RazorPayDaysView(TemplateView):
    template_name = 'razorpay_days.html'

    def post(self, request, *args, **kwargs):
        if Books.status == 'Available':
            rental_days = int(request.POST.get('rental_days'))
            per_day = 5
            total_amount = per_day * rental_days

        else:
            messages.error(request, "Sorry the Book is Not Available")
            return redirect('readerbook_view')

        