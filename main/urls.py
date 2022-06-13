from django.urls import path

from .views import index, other_page, profile, user_activate
from .views import BBLoginView, BBLogoutView
from .views import ChangeUserInfoView, BBPasswordChangeView, DeleteUserView
from .views import RegistreUserView, RegisterDoneView
from .views import user_activate


app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/',
         user_activate, name='register_activate'),
    path('accounts/register/done/',
         RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegistreUserView.as_view(), name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/',
         BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/',
         ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
