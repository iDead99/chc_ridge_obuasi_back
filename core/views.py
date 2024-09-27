from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Member
from .serializers import MemberSerializer

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'last_name', 'email', 'date_registered']
    search_fields = ['first_name', 'last_name', 'email', 'phone',
                     'residence', 'gps_address', 'occupation', 'date_registered']

    def get_permissions(self):
        if self.request.method == 'POST':
            # Allow any user to create new members
            return [permissions.AllowAny()]
        else:
            # Only admin users can perform GET or other operations
            return [permissions.IsAdminUser()]
