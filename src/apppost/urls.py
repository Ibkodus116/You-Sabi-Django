from django.urls import path
from .views import postview,formsview,editview,deleteview,readview

urlpatterns = [
    path('', postview ,name='home'),
    path('new/', formsview ,name='form'),
    path('edit/<post_id>/', editview ,name='edit'),
    path('delete/<post_id>/', deleteview ,name='delete'),
    path('view/<post_id>/', readview ,name='view'),
]