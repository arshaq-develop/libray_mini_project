"""
URL configuration for libraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/admin', views.AdminHomeView.as_view(), name='admin_home'),
    path('home/admin/books', views.ListBooks.as_view(), name='listbooks_view'),
    path('', views.ReaderHomeView.as_view(), name='reader_home'),
    path('reader/book', views.BookListView.as_view(), name='readerbook_view'),
    path('reader/book/detail/<int:id>', views.BookDetailView.as_view(), name='bookdetail_view'),
    path('login', views.UserLoginView.as_view(), name='login_view'),
    path('logout', views.LogoutView.as_view(), name='logout_view'),
    path('register', views.UserRegisterView.as_view(), name='register_view'),
    path('upload', views.BookUploadView.as_view(), name='bookupload_view'),
    path('list/student', views.ListStudentLogedin.as_view(), name='liststudent_view'),
    path('home/admin/books/delete/<int:id>', views.BookDeleteView.as_view(), name='bookdelete_view'),
    path('home/admin/books/update/<int:id>', views.BookUpdateView.as_view(), name='bookupdate_view'),
    path('home/admin/student/delete/<int:id>', views.AdminStudentDeleteView.as_view(), name='studentdelete_view'),
    path('book/search', views.BookSearchView.as_view(), name='booksearch_view'),
    path('book/rent', views.RazorPayDaysView.as_view(), name='razorday_view'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
