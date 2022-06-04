from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from django.urls import path

app_name = "bookstuff"

from book_app import views as book_app_views

urlpatterns=[
    url(r'^testHeaders/', book_app_views.test_headers, name='testHeaders'),

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('create_user/', book_app_views.SupportStuffCreate.as_view(),name='create_user'),
    path('login_user/', book_app_views.SupportStuffLoginView.as_view(),name='login_user'),

    path('create_book/', book_app_views.CreateBookView.as_view(),name='create_book'),
    path('update_book/', book_app_views.UpdateBookView.as_view(),name='update_book'),
    
    path('create_offer/', book_app_views.CreateOfferView.as_view(),name='create_offer'),
    path('update_offer/', book_app_views.UpdateOfferView.as_view(),name='update_offer'),
    
]
