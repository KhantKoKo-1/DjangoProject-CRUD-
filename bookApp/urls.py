from django.urls import path
from.import views


urlpatterns = [

path('',views.home,name='home'),
path('user/',views.user,name='user'),
path('userdelete/<int:id>',views.userdelete,name='userdelete'),
path('booklist',views.book,name='bookList'),

path('bookdelete/<int:id>',views.bookDelete,name='bookDelete'),
path('addbook/',views.addForBook,name="addbook"),
path('updatebook/<int:id>',views.updatebook,name='updatebook'),
path('writerList/',views.writer,name='writerList'),
path('addwriter/',views.addwriter,name='addwriter'),
path('deletewriter/<int:id>',views.deletewriter,name='deletewriter')

]