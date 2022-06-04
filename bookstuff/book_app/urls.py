from django.conf.urls import url
from django.urls import path

app_name = "bookstuff"

from book_app import views as book_app_views

urlpatterns=[
    url(r'^testHeaders/', book_app_views.test_headers, name='testHeaders'),
    
    #path('login_user/', book_app_views.LoginUserView.as_view(),name='login_user'),
    #path('create_post/', book_app_views.CreatePostView.as_view(),name='create_post'),
    #path('like_post/', book_app_views.PostLikeView.as_view(),name='like_post'),
]
