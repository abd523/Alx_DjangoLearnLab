from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from .models import Activity
from .serializers import UserRegisterSerializer, ActivitySerializer
from .permissions import IsActivityOwner

# --- User Auth Views ---
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer


# --- Activity Filtering Engine ---
class ActivityFilter(filters.FilterSet):
    activity_type = filters.CharFilter(field_name="activity_type", lookup_expr="iexact")
    start_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Activity
        fields = ['activity_type', 'start_date', 'end_date']


# --- Activity CRUD Endpoints ---
class ActivityListCreateView(generics.ListCreateAPIView):
    """
    Handles GET (List all user activities with filters/sorting/pagination)
    and POST (Create a new activity for the logged-in user).
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ActivityFilter

    def get_queryset(self):
        # Strict Isolation: Users only see their own logged activities
        user = self.request.user
        queryset = Activity.objects.filter(user=user)
        
        # Implement URL query sorting parameters (e.g., /api/activities/?ordering=-date)
        ordering = self.request.query_params.get('ordering', '-date')
        if ordering in ['date', '-date', 'duration', '-duration', 'calories_burned', '-calories_burned']:
            queryset = queryset.order_by(ordering)
            
        return queryset

    def perform_create(self, serializer):
        # Automatically tie the newly created activity record to the logged-in user
        serializer.save(user=self.request.user)


class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (Detail view), PUT/PATCH (Update), and DELETE for a single activity.
    Enforces strict object ownership checks.
    """
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsActivityOwner]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)