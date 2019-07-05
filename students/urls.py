from rest_framework import routers
from .api import ClassNameViewset, ParentViewset, StudentViewset


router = routers.DefaultRouter()
router.register('api/classname', ClassNameViewset, 'classname')
router.register('api/parent', ParentViewset, 'parent')
router.register('api/student', StudentViewset, 'student')


urlpatterns = router.urls
