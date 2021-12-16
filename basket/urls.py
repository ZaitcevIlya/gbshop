from django.urls import path
import basket.views as basket

app_name = 'basket'

urlpatterns = [
    path('', basket.view, name='view'),
    path('add/<int:pk>/', basket.add, name='add'),
    path('remove/<int:pk>/', basket.remove, name='remove')
]