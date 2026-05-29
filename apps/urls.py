from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ActivityListCreateView, ActivityDetailView

urlpatterns = [
    # Auth Endpoints
    path('users/register/', RegisterView.as_view(), name='api_register'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),

    # Activity Management CRUD Endpoints
    path('activities/', ActivityListCreateView.as_view(), name='activity_list_create'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
]





