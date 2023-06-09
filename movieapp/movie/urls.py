from django.urls import path
from movie import views
app_name="movie"

urlpatterns = [
path('',views.index,name='index'),
path('movie/<int:item_id>/',views.detail,name='detail'),
path('add',views.add,name='add'),
path('update/<int:item_id>/',views.update,name='update'),
path('delete/<int:item_id>/',views.delete,name='delete'),


]


