
from django.urls import path
from project import views

app_name='project'

urlpatterns = [
    path('base/',views.origin, name = 'base'),
    # path('cat/',views.Cats.as_view(), name = 'cat'),
    path('home/',views.Home.as_view(), name = 'home'),
    path('catcreate/',views.CatCreate.as_view(), name = 'catcreate'),
    path('blogcreate/',views.BlogCreate.as_view(), name = 'blogcreate'),
    path('blogdetails/<pk>/',views.Detail.as_view(), name = 'detail'),
    path('catdetails/<pk>/',views.CatDetails.as_view(), name = 'catdetail'),
    path('blogupdate/<pk>/',views.BlogUpdate.as_view(), name = 'update'),
    path('blogdelete/<pk>/',views.BlogDelete.as_view(), name = 'delete'),
    path('registration/', views.registration , name = 'registration'),
    path('login/', views.sign_in , name = 'login'),
    path('logout/', views.sign_out , name = 'logout'),
    path('',views.index, name = 'index')

]
