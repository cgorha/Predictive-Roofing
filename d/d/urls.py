from django.contrib import admin
from django.urls import path, include
from project.views import UserDetailAPIView

from project import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/hi/', UserDetailAPIView.as_view(), name='myuser-detail'),
    path('leads/', views.LeadListCreate.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', views.LeadDetail.as_view(), name='lead-detail'),
    path('api/messages/', views.send_sms, name='send_sms'),
    path('api/v1/calendar/', views.calendarEventListCreate.as_view(), name='calendar-list-create'),
]


