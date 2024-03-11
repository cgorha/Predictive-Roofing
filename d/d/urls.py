from django.contrib import admin
from django.urls import path, include
from project.views import UserDetailAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/hi/', UserDetailAPIView.as_view(), name='myuser-detail'),
]


