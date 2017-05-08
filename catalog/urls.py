from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^services/$', views.BookListView.as_view(), name='books'),
    url(r'^service/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^business/$', views.AuthorListView.as_view(), name='authors'),  

    url(r'^genre/$', views.GenreListView.as_view(), name='genre'),  
    url(r'^genres/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),  
    url(r'^businesses/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]


urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^borrowed/$', views.LoanedBooksAllListView.as_view(), name='all-borrowed'), #Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [   
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]


# Add URLConf to create, update, and delete authors
urlpatterns += [  
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [  
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
]
