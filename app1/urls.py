from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='home'),
    path('signinuser',signinuser,name='signin'),
    path('loginuser',loginuser,name='loginuser'),
    path('logout',logoutuser,name='logout'),
    path('show_book',show_book,name='show_book'),
    path('view_book/<int:id>/',view_book,name='view_book'),
    path('book/<int:book_id>/download/', download_pdf, name='download_pdf'),
    path('add_wish/<int:id>/',add_wish_list,name='add_wish'),
    path('view_wish_list',show_wish_list,name='view_wish_list'),
    path('delete/<int:id>/',delete_items,name='delete_item')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)