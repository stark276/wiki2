from django.urls import path
from accounts.views import SignUpView

# app_name = accounts

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
]