from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list),
    path('<int:pk>/', product_detail),
    path('create/', product_create),
    path('<int:pk>/update/', product_update),
    path('<int:pk>/delete/', product_delete),
]