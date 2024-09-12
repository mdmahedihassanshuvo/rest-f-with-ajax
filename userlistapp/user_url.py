from django.urls import path
from .views import user_list,UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'), 
    path('', user_list, name='user_list_html'), 
]
