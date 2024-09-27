from rest_framework import routers
from . views import MemberViewset

router = routers.DefaultRouter()

router.register('members', MemberViewset, basename='Member')

urlpatterns = router.urls
