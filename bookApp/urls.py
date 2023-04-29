from django.urls import path
from.import views


urlpatterns = [

path('',views.loginPage,name='loginPage'),
path('user/',views.user,name='user'),
path('userdelete/<int:id>',views.userdelete,name='userdelete'),
path('booklist',views.book,name='bookList'),


path('bookdelete/<int:id>',views.bookDelete,name='bookDelete'),
path('addbook/',views.addForBook,name="addbook"),
path('updatebook/<int:id>',views.updatebook,name='updatebook'),
path('writerList/',views.writer,name='writerList'),
path('addwriter/',views.addwriter,name='addwriter'),
path('deletewriter/<int:id>',views.deletewriter,name='deletewriter'),
path('logout/',views.logoutPage,name='logoutPage'),
path('favBook/',views.favBook,name='favBook'),
path('fav_book_delete/<int:id>',views.fav_book_delete,name='fav_book_delete')
]