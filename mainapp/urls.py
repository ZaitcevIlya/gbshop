from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'
urlpatterns = [
    path('', mainapp.products, name='product'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('home/', mainapp.products, name='home'),
    path('office/', mainapp.products, name='office'),
    path('classic/', mainapp.products, name='classic')
]
