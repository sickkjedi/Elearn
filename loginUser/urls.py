from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.RegisterUser.as_view(), name='register'),
    path('accounts/users', views.ListUser.as_view(), name='users'),
    path('accounts/users/edit/<int:pk>', views.EditUser.as_view(), name='edit_user'),
    path('accounts/users/edit/<int:pk>/verified', views.VerifyUser.as_view(), name='verified'),
    path('accounts/users/edit/<int:pk>/suspend', views.SuspendUser.as_view(), name='suspend'),
    path('accounts/register', views.CreateView.as_view(), name='create'),
]
